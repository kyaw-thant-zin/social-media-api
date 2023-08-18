


class PlaywrightService:
    _browser = None

    def __init__(self):
        if not PlaywrightService._browser:
            self._start_browser() # launch the browser

    def _start_browser(self):
        PlaywrightService._browser = '' # set the browser

    