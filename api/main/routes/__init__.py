from flask_restful import Api

# Resources
from api.main.resources.dashboard_resources import DashboardIndexResource

def register_routes(api):
    api.add_resource(DashboardIndexResource, '/dashboard')


api = Api()