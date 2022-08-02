# from O365 import Connection, Account, FileSystemTokenBackend, MSOffice365Protocol
import datetime
import os

import config

class HourMock():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

class EventMock():
    def __init__(self, subject, start, end):
        self.subject = subject
        self.start = HourMock(start, 0)
        self.end = HourMock(end, 0)


class Calendar():

    def __init__(self):
        self._authenticate()

    def _authenticate(self):
        # token_backend = FileSystemTokenBackend(token_path=os.path.dirname(os.path.realpath(__file__)))
        # connection = Connection(config.credentials, scopes=['basic', 'Calendars.Read'], token_backend=token_backend)
        # connection.refresh_token()
        # account = Account(config.credentials, scopes=['basic', 'Calendars.Read'], token_backend=token_backend)

        # if not account.is_authenticated:
        #     if account.authenticate():
        #         print('Authenticated!')
        #     else:
        #         print('Authentication failed!')
        #         return
        # self._schedule = account.schedule()
        print("Authentication dummy...")

    def get_events(self):
        """
        Return todays events for a given room.
        """
        # today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # start_time = today + datetime.timedelta(hours=8)
        # end_time = today + datetime.timedelta(hours=18)
        # calendar = self._schedule.get_calendar(calendar_name=room)
        # q = calendar.new_query('start').greater_equal(start_time)
        # q.chain('and').on_attribute('end').less_equal(end_time)
        return [EventMock("dummy appointment", 13, 14)]
