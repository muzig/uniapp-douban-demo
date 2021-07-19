from flask import Flask

app = Flask(__name__)

json_data = {}


# 读取文件信息
@app.route('/<file_name>')
def girls(file_name):
    try:
        if json_data.get(file_name) is not None:
            return json_data[file_name]
        with open("../src/"+file_name+".json", 'r') as f:
            json_data[file_name] = f.read()
            return json_data[file_name]
    except Exception as err:
        return f'{err}'
