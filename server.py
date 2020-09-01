
from flask import Flask, request
import flask
import json
import botchat
import hyper as hp

app = Flask(__name__)

@app.route("/")
def _hello_world():
	return "Hello world"


@app.route("/botchat-api", methods=["POST","GET"])
def predict():
	data = {"status": False}
	if request.args.get('question'):
		data["status"] = True
	question = request.args.get('question')
	data["question"] = question
	data["answer"] = botchat.onMessage(question)

	return json.dumps(data, ensure_ascii=False)

if __name__ == "__main__":
	print("App run!")
	app.run(debug=False, host=hp.IP, threaded=False)
