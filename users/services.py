import requests
import json

from numpy.distutils.fcompiler import none


def get_user():
    url = 'http://localhost:8080/phppy/API.php?data=user'
    # headers = {'Accept':'application/json', 'Content-Type':'application/json'}
    # params = {'username': username, 'first_name': first_name}
    r = requests.get(url)
    data=str(r)
    user_list = json.dumps(data)
    if user_list:
        return user_list
    else:
        return none