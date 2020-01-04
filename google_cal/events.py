from google_cal import setup_cal
import datetime


def get_events():
    service = setup_cal.get_calendar()

    # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # timeMin=now *in events().list
    # pylint: disable=no-member
    events_result = service.events().list(calendarId='primary',
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events


if __name__ == '__main__':
    get_events()
