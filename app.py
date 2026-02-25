from flask import Flask, request
from blog.routes.post_routes import post_blueprint

app = Flask(__name__)
app.register_blueprint(post_blueprint)

@app.route("/")
def hello_world():
    return "hello, world"

@app.route("/add", methods=['POST'])
def add():
    data = request.get_json()
    if not all(key in data for key in ('num1', 'num2')):
        return {'error' : 'missing num1 or num2 in request data'}, 400
    
    result = data['num1'] + data['num2']
    return {'result' : result}, 200


if __name__ == "__main__":
    app.run(debug=True)