from flask import Flask

app = Flask(__name__)

data_girls = open("../src/girls.json").read()


# 获取女孩信息
@app.route('/girls')
def girls():
    return data_girls


data_hot_showing = open("../src/hot_showing.json").read()


# 获取热门放映信息
@app.route('/hot_showing')
def hot_showing():
    return data_hot_showing


data_hot_movie = open("../src/hot_movie.json").read()


# 获取热门放映信息
@app.route('/hot_movie')
def hot_movie():
    return data_hot_movie
