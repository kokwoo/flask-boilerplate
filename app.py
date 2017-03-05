from gevent.wsgi import WSGIServer
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

try:
	print "starting server in port 5000"
	http_server = WSGIServer(("127.0.0.1", 5000), app)
	http_server.serve_forever()
except KeyboardInterrupt:
	print "exiting gracefully"
