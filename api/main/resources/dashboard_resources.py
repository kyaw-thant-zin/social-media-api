from flask_restful import Resource

class DashboardIndexResource(Resource):
    def get(self):
        return {'message': 'Dashboard index!'}