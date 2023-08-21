from ...play_wright import PlaywrightService

class IG:

    _ig_url = ''
    _ig_usr_url = ''
    _ig_post_limit = 12

    def __init__(self):
        playwright_service = PlaywrightService() 

    def get_profile(self, username):
        browser = PlaywrightService().get_browser()  
        print('get the profile')
        return username