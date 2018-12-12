#   - It returns an empty hash if the request fails
#   - GET is the default method
#   - 'application/json' is the default Content-Type
module HttpRequest
  DEFAULT_KEYS_TO_FILTER = %w[password password_confirmation client_secret secret]

  def call(
    method: :get, 
    base_url: '', 
    path: '', 
    params: {}, 
    data: {}, 
    headers: {}, 
    keys_to_filter: [],
    filtered_string: '[FILTERED]'
  )
    http_method = sanitize_method(method)
    return {} unless http_method.present? && params.is_a?(Hash) && data.is_a?(Hash) && headers.is_a?(Hash)

    conn = http_connection(
      base_url: base_url, 
      keys_to_filter: keys_to_filter, 
      filtered_string: filtered_string
    )
    response = conn.send(http_method, path) do |req|
      req.url path
      req.headers = headers if headers.present?
      req.headers['Content-Type'] = 'application/json' if req.headers['Content-Type'].blank?
      req.params = params if params.present?
      if data.present? && req.headers['Content-Type'] == 'application/json'
        req.body = data.to_json 
      end
    end

    JSON.parse(response.body).with_indifferent_access
  rescue Faraday::ConnectionFailed, JSON::ParserError
    {}
  end

  private

  def sanitize_method(http_method)
    method = http_method.to_s.downcase.to_sym
    method if %i[get put patch post delete].include?(method)
  end

  # Create an HTTP connection object using the Faraday Gem
  # Reference: https://github.com/lostisland/faraday
  # IMPORTANT: The order of these middleware matters!
  # TODO: improve the logger regex
  def http_connection(base_url: , keys_to_filter: , filtered_string:)
    Faraday.new(url: base_url) do |faraday|
      # Log to stdout
      faraday.response :logger do |logger|
        keys = DEFAULT_KEYS_TO_FILTER.merge(keys_to_filter).map { |k| "#{k}\=" }.join("|")
        matcher = Regexp.new "(#{keys})(.+)[&$]"
        logger.filter(matcher, "\1#{filtered_string}")
      end
      faraday.adapter Faraday.default_adapter
    end
  end
end