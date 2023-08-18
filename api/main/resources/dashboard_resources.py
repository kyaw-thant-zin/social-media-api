
from flask_restful import Resource
from api.main.middleware.auth import authenticate

from playwright.sync_api import Playwright, sync_playwright

from api.main.services import SocialMediaService

class DashboardIndexResource(Resource):

    method_decorators = [authenticate]

    def get(self):
        userProfile = SocialMediaService.ig.get_profile('test user')
        print(userProfile)
        return {'message': 'Test Dashboard index!'}