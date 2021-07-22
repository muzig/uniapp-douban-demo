import json
import random

import requests
import time
from copyheaders import headers_raw_to_dict


def upload_girls(path):
    ret = []
    with open(path, 'r') as f:
        d = json.loads(f.read())
        for k in d.get('data'):
            ret.append(k.get('images')[0])
    return ret


def upload_img(path):
    ret = []
    with open(path, 'r') as f:
        for k in json.loads(f.read()):
            ret.append(k.get('img'))
    return ret


if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    for k in [
        # upload_girls('../srv/static/girls.json'),
        upload_img("../srv/static/hot_movie.json"),
        upload_img("../srv/static/hot_showing.json"),
        upload_img("../srv/static/hot_teleplay.json")]:
        for img in k:
            name = img.split('/')[-1]
            if '.' not in name:
                name += '.jpg'
            print(name, img)
            resp = requests.get(img, headers=headers)
            resp.encoding = 'utf-8'
            time.sleep(10)
            if resp.status_code == 403:
                continue
            with open('./imgs/' + name, 'wb') as f:
                f.write(resp.content)
                f.close()
