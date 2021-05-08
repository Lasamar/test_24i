from urllib import request



index = request.urlopen("http://127.0.0.1:8081")
about = request.urlopen("http://127.0.0.1:8081/about")

if index.getcode() != 200:
    raise Exception("Wrong code for index page")

if 'Hello Davide' not in index.read().decode('utf-8'):
    raise Exception("Wrong message for index page")

if about.getcode() != 200:
    raise Exception("Wrong code for about page")
if '+31 20 12345678' not in about.read().decode('utf-8'):
    raise Exception("Telephone number not found in about page")

