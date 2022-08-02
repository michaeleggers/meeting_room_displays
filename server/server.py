from o365_calendar import Calendar, EventMock
from dongle import Dongle
from display_cluster import DisplayCluster

calendar = Calendar()
dongle = Dongle()

try:
    displays = DisplayCluster(dongle)
    print("server.py: displays: ", displays)

    while True:
        displays.set_date()

        for room in displays.rooms():
            displays[room].set_events(calendar.get_events())

        displays.suspend()

except KeyboardInterrupt:
    pass
finally:
    dongle.disconnect()
