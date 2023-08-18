from ...playwright import PlaywrightService

class IG:

    def get_profile(self, username):
        playwright_service = PlaywrightService() 
        playwright_service.get_browser()  
        print('get the profile')
        return username