module JWTAuth
  class << self
    # We could also do a GET to https://onample.auth0.com/.well-known/jwks.json
    # We should store this in memory and init at rails startup
    def decode(token: nil, algorithm: 'RS256', verify_flag: true, certificate: nil)
      JWT.decode(token, public_key(certificate), verify_flag, { algorithm: algorithm })
    rescue => e
      Rails.logger.error "#{e.class}: #{e.message}"
      raise
    end

    private

    # TODO: Need error checking here to make sure the certificate string is parsable
    def public_key(certificate)
      certificate ||= default_certificate
      OpenSSL::X509::Certificate.new(certificate).public_key
    end

    def default_certificate
      File.open("#{Rails.root}/vendor/auth0/onample.pem", "r")
    end
  end
end
