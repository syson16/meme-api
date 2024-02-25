from flask import Flask
from flask import request

def create_app():
    app = Flask(__name__)

    remaining_calls = {'dummy-token-1': 10}

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route('/memes')
    def memes():
        #/memes?lat=40.730610&lon=-73.935242&query=food
        lat = request.args.get('lat', '')
        lon = request.args.get('lon', '')
        query = request.args.get('query', '')

        # this is to simulate the token from the user header
        token = request.headers.get('token', 'dummy-token-1')

        payload = {"token": token}

        # the remaining call from the api from another team
        if remaining_calls[token] > 0:
            remaining_calls[token] -= 1
            payload["remaining-calls"] = remaining_calls[token]
        else:
            payload['error'] = 'invalid balance'
        
        return payload #update
    
    return app

