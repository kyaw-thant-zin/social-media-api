from flask_restful import Resource
from api.main.middleware.auth import authenticate

class DashboardIndexResource(Resource):

    method_decorators = [authenticate]

    def get(self):
        return {'message': 'Test Dashboard index!'}