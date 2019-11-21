import flask
import requests

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
  agent = {'User-Agent': flask.request.headers.get('User-Agent')}

  if flask.request.method == 'GET':
    r = requests.get(path, headers=agent)
    if r.ok:
      return r.text
  elif flask.request.method == 'POST':
    payload = flask.request.form
    r = requests.post(path, data=payload, headers=agent)
    if r.ok:
      return r.text
  return ""

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

