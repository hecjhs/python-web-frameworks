from flask import Flask
from flask_restful import Resource, Api

from celery_q.worker import celery
import celery.states as states

from views.utils.test import HealthCheck

app = Flask(__name__)
api = Api(app)

class Test(Resource):

    def get(self):
        return {'message': 'ok'}


api.add_resource(HealthCheck, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

