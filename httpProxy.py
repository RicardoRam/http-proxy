import flask
import requests

app = flask.Flask(__name__)

@app.route('/proxy/<path:path>', methods=['GET', 'POST'])
def _proxy(path):
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

