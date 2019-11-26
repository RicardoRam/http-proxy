import flask
from flask import Response
import requests
from urllib.parse import urlparse

app = flask.Flask(__name__)

@app.route('/proxy/<path:path>', methods=['GET', 'POST'])
def _proxy(path):
  """Call this proxy API endpoint '/proxy/<path>' by passing in a path that is a
  URL you want to make a request to. Handles either a GET or POST request,
  otherwise, returns an empty string.

  GET: Updates the User-Agent header to the caller's User-Agent and returns the
    updated response received from the <url>'s server.
  POST: Updates the User-Agent header to the caller's User-Agent, adds form
    data given, and returns the updated response received from the <url>'s server.

  :param path: the URL you want to make a request to
  :type path: string
  :return: a modified response depending on the type of request
  :rtype: string
  """
  allHeaders = dict(flask.request.headers)
  parsed_uri = urlparse(path)
  host = parsed_uri.netloc
  allHeaders['Host'] = host

  if flask.request.method == 'GET':
    args = dict(flask.request.args)
    r = requests.get(path, headers=allHeaders, params=args)
    if r.ok:
      return Response(response=r.content, mimetype=r.headers['Content-Type'])
  elif flask.request.method == 'POST':
    payload = dict(flask.request.form)
    r = requests.post(path, data=payload, headers=allHeaders)
    if r.ok:
      return Response(response=r.content, mimetype=r.headers['Content-Type'])
  return ""

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

