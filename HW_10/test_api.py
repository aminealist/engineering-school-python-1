import requests
import json
link = "http://127.0.0.1:5000/mark"

user1 = dict(
    subject='sub1',
    group='g1',
    fio='f i o',
    mark='52'
)

user2 = dict(
    subject='sub1',
    group='g1',
    fio='f i o',
    mark='5'
)


user3 = dict(
    subject='sub3',
    group='g2',
    fio='f i o',
    mark='5'
)

req = requests.post(link, json=user1)
print(req.text)

req = requests.post(link, json=user3)
print(req.text)

req = requests.delete(link, json=user1)
print(req.text)


