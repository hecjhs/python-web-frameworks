from flask_restful import Resource
from celery_q.worker import celery

class HealthCheck(Resource):
    def get(self):
        try:
            task = celery.send_task('tasks.add', args=[4,5], kwargs={})
            message = 'celery ok'
        except:
            message = 'something went wront with celery'
        return { 'message': message }
