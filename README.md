# Proxy

This proxy uses the Flask framework and the Requests library to implement a simple web service that listens on /proxy/<url> for either a GET or POST request.

# GET Request

On a GET request, it updates the User-Agent header to the caller's User-Agent and returns the response from the <url>'s server.

# POST Request

On a POST request, it updates the User-Agent header to the caller's User-Agent, adds form data given, and then returns the response from the <url>'s server.
