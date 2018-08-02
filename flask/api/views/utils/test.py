from flask_restful import Resource
from celery_q.worker import celery

class HealthCheck(Resource):
    def get(self):
        task = celery.send_task('tasks.add', args=[4,5], kwargs={})
        return { 'message': 'current status ok' }
