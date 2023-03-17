# install virtual python env
# in project directory enter <python -m venv venv
# -m flag allow start venv as load module
# syntaxis is: python (flag) (image of python) (source name of image dir)
# work like bind mounts
# To activate venv (run project venv) print <source venv/bin/activate>
# Now you can install libraries in virtual env
# To leave venv project terminal print <deactivate> cmd
from datetime import datetime
from flask import Flask, render_template, request
import json

class Bot:
    def __init__(self):
        self.isBot = 1

    def check_updates(messages_list):
        isBot = 1
        last_msg = messages_list[len(messages_list) - 1]
        if last_msg['isBot'] != 1:
            match last_msg['text']:
                case 'hi':
                    text = 'Hello there!'
                case 'bye':
                    text = 'See you!'
            time = datetime.now()
            json_time = time.strftime('%H:%M')
            bot_msg = {
                    'text' : text,
                    'sender' : 'bot',
                    'time' : json_time,
                    'isBot' : isBot
            }
            messages_list.append(bot_msg)
            saveInfo(messages_list, db_name)

def loadInfo(db_name):
    with open(db_name, 'r') as db:
        db_info = json.load(db)
    return db_info['messages']

def saveInfo(db_info, db_name):
    data = {'messages' : db_info}
    with open(db_name, 'w') as json_file:
        json.dump(data, json_file)
    return 0

app = Flask(__name__)
db_name = 'db.json'
messages_list = loadInfo(db_name)

@app.route('/chat')
def displayChat():
    return render_template('form.html')

@app.route('/get_messages')
def getMessages():
    return {'messages' : messages_list}

@app.route('/send_message')
def sendMessage():
    isBot = 0
    sender = request.args['name']
    text = request.args['text']
    time = datetime.now()
    json_time = time.strftime('%H:%M')
    msg = {
        'text' : text,
        'sender' : sender,
        'time' : json_time,
        'isBot' : isBot
    }
    messages_list.append(msg)
    saveInfo(messages_list, db_name)
    Bot.check_updates(messages_list)

app.run(host='0.0.0.0', port=80)


# messages_list = []

# def addMessage (sender, text):
#     new_msg = {
#         'name' : sender,
#         'content' : text,
#         'date' : datetime.now()
#     }
#     messages_list.append(new_msg)

# def printMessage (message):
#     print(f'{message["name"]}: {message["content"]}\n{message["date"]}')

# for i in range(4):
#     msg = input()
#     if i % 2 == 0:
#         name = 'Steve'
#     else:
#         name = 'Alan'
#     addMessage(name, msg)

# for i in range(len(messages_list)):
#     printMessage(messages_list[i])
