from flask import Flask, request

app = Flask(__name__)




@app.route('/<path:path>')
def show_subpath(path):
    idx = path.rfind('/')
    return f'Hello, {path[idx + 1:]}!'


if __name__ == '__main__':
    app.run(debug=True)
