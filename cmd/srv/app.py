from flask import Flask
import json, os

app = Flask(__name__)

json_data = {}


# 读取文件信息
@app.route('/hot/<file_name>')
def hot(file_name):
    try:
        if json_data.get(file_name) is not None:
            return json_data[file_name]
        with open("../src/" + file_name + ".json", 'r') as f:
            json_data[file_name] = f.read()
            return json_data[file_name]
    except Exception as err:
        return f'{err}'


# 获取热门资源列表
@app.route('/hot/list')
def hot_list():
    return json.dumps([e for e in os.listdir("../src") if e.endswith('.json')])
