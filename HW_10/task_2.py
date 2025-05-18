from flask import Flask, request
import json

app = Flask(__name__)


@app.get('/group')
def get_group():
    global a
    if a:
        preface = 'There are ' if len(a) > 1 else 'There is '
        return preface + ', '.join(a) + ' in the group'
    return "The group is empty"

@app.post('/group')
def post_group():
    global a
    print(request.data)
    name = request.json['name']
    a.append(name)
    return "Ok"




if __name__ == '__main__':
    a = []
    app.run(debug=True)
