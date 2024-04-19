import loguru
from flask_cors import CORS
from flask import request, jsonify
from flask import Flask
from flask import Flask, request, render_template

from chatgpt_api.helpers.tools import load_json
from chatgpt_api.helpers.tools import Tools
from chatgpt_api.views.ChatGPT import ChatGPTView

from dotenv import load_dotenv
load_dotenv()


loguru.logger.info("Starting ChatGPT API")

app = Flask(__name__)
CORS(app)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024

ChatGPT = ChatGPTView()

@app.route("/")
@app.route("/index")
def index():
   return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def ChatGPT_loadmessage():
    json = load_json(request.json)
    return ChatGPT.send_message(json)


@app.route('/version', methods=['GET'])
def version():
    return jsonify(version=1.0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)