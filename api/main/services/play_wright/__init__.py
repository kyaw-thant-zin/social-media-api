import os
from playwright.sync_api import sync_playwright


class PlaywrightService:
    _browser = None
    _browserPath = os.path.abspath('api/browser/chrome/Chromium.app/Contents/MacOS/Chromium')
    _usr_dir = os.path.abspath('api/browser/usr_dir')

    def __init__(self):
        print('self service')
        if not PlaywrightService._browser:
            self._start_browser() # launch the browser

    def _start_browser(self):
        playwright = sync_playwright().start()
        PlaywrightService._browser = playwright.chromium.launch_persistent_context(
            executable_path=self._browserPath, 
            headless=False,
            user_data_dir=self._usr_dir
        ) # set the browser
        print('start the browser')

    def get_browser(self):
        if not PlaywrightService._browser:
            return PlaywrightService._browser #return the browser
        else:
            self._start_browser() # launch the browser

    