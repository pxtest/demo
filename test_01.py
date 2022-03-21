# import keyword

# #输出当前版本所有关键字
# print(keyword.kwlist) 

# print('I\'m ok')
#------------------------------------------
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell_world():
    return "hello world"

@app.route('/get',methods=["get"])
def get_():
    return "get请求"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7777)