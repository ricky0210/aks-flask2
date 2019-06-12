import platform
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    합계 = sum(range(100000000))
    return "서버 호스트 : {}, 합계 : {}".format(platform.node(), 합계)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
