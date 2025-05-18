import http

import flask
from flask import Flask, request
import json

app = Flask(__name__)


def get_marks():
    with open('mark.json', 'r') as f:
        marks = json.load(f)
    return marks


def set_marks(marks: list[dict]):
    with open('mark.json', 'w') as f:
        json.dump(marks, f)


def valid(to_check: list[str], d: dict) -> bool:
    for i in to_check:
        if i not in d:
            return False
    return True


@app.post('/mark')
def create_mark():
    print(1)
    json = request.json
    if not valid(['subject', 'mark', 'group', 'fio'], json):
        return flask.Response(
            status=http.HTTPStatus.BAD_REQUEST
        )
    marks = get_marks()
    marks.append(json)
    set_marks(marks)
    return 'OK'


@app.delete('/mark')
def delete_mark():
    json = request.json
    if not valid(['subject', 'group', 'fio'], json):
        return flask.Response(
            status=http.HTTPStatus.BAD_REQUEST
        )
    marks = []
    for mark in get_marks():
        if mark['subject'] != json['subject']:
            marks.append(mark)
            continue
        if mark['group'] != json['group']:
            marks.append(mark)
            continue
        if mark['fio'] != json['fio']:
            continue
    set_marks(marks)
    return 'OK'


@app.put('/mark')
def put_mark():
    json = request.json
    if not valid(['subject', 'group', 'fio'], json):
        return flask.Response(
            status=http.HTTPStatus.BAD_REQUEST
        )
    marks = get_marks()
    for i, mark in enumerate(marks):

        if (mark['subject'] == json['subject']
                and mark['group'] == json['group']
                and mark['fio'] == json['fio']):

            marks[i]['mark'] = json['mark']

    set_marks(marks)
    return 'OK'


app.run(debug=True)
