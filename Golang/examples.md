```go
// Get IP address
  ip, _, err := net.SplitHostPort(c.Request.RemoteAddr)
	if err != nil {
		response.SendJSONMessage(c, http.StatusInternalServerError, err.Error())
		return
	}
```
