from google_cal import setup_cal
import datetime


def calculate_length(start, end):
    start_time = start.split('T')[1][:5]
    end_time = end.split('T')[1][:5]

    start_time_m = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
    end_time_m = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])
    
    return end_time_m - start_time_m


def format_events(events):
    formated_events = []

    for event in events:
        formated_event = {'summary': event['summary'], 'description': event['description']}
        try:
            start = event['start']['dateTime']
            end = event['end']['dateTime']
            date = event['start']['dateTime'].split('T')[0][:10]
            length = calculate_length(start, end)
            
            formated_event['date'] = date
            formated_event['length'] = length
        except:
            date = event['start']['date']
            formated_event['date'] = date

        formated_events.append(formated_event)
    return formated_events
    


def get_events():
    service = setup_cal.get_calendar()

    # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # timeMin=now *in events().list
    # pylint: disable=no-member
    events_result = service.events().list(calendarId='primary', timeMin='2020-01-01T00:00:00.0Z',
                                          maxResults=100, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    formated_events = format_events(events)

    return formated_events

# add id's