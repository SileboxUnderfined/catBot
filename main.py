from flask import Flask, request
from vk_api.utils import get_random_id
from vk_api import VkApi
from os import environ
from keyboards import startKeyboard
from cat import Cat

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return "kek"

    return 'Котобот стартовая страница'

@app.route(environ['BOT_ROUTE'], methods=['POST'])
def bot():
    data = request.get_json(force=True,silent=True)
    if not data or 'type' not in data:
        return 'not ok'

    if data['type'] == 'confirmation':
        return environ['CONFIRM_TOKEN']

    if data['secret'] == environ['SECRET']:
        if data['type'] == 'message_new':
            message = data['object']['message']
            if message['text'] == 'Начать':
                bs.messages.send(message="Используй клавиатуру!",random_id=get_random_id(),user_id=message['from_id'],keyboard=startKeyboard())

            elif message['text'] == "Хочу кота":
                bs.messages.send(message="Лови кота!",random_id=get_random_id(),user_id=message['from_id'],keyboard=startKeyboard(),attachment=cat.getRandomCat(bs))

    return 'ok'

if __name__ in "__main__":
    BotSession = VkApi(token=environ['VK_API_KEY'])
    bs = BotSession.get_api()
    cat = Cat()
    app.run(host='0.0.0.0',port=environ['PORT'],debug=False)