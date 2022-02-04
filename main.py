import vk_api
from flask import Flask, request
from vk_api.utils import get_random_id
from os import environ

app = Flask(__name__)

@app.route(environ['BOT_ROUTE'], methods=['POST'])
def bot():
    pass

if __name__ in "__main__":
    app.run(host='0.0.0.0',port=environ['PORT'],debug=False)