import final
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class final_forecast(Resource):
    def get(self, city_name):
        return {'data': final.forecast(city_name)}

api.add_resource(final_forecast, '/final/<city_name>')

if __name__ == '__main__':
     app.run()