#flaskでサーバを起動☆で、render.comでもホスト可能にしてる　render.comだと、ポートを無理やりサーバ立ててこじ開けないと行けないんよ
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Revolt bot Live !!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()