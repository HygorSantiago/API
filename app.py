from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Print(Resource):
    def get(self):
        return {'Deu certo':'Deu certo'},200
        
api.add_resource(Print,
                 '/print')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
    
