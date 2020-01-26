from google_cal import setup_cal
import datetime


def calculate_length(start, end):
    start_time = start.split('T')[1][:5]
    end_time = end.split('T')[1][:5]

    start_time_m = int(start_time.split(
        ':')[0]) * 60 + int(start_time.split(':')[1])
    end_time_m = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])

    return end_time_m - start_time_m


def format_events(events):
    formated_events = []
    for event in events:
        formated_event = {
            'summary': event['summary'], 'description': event['description'], 'id': event['id']}
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

def group_events(formated_events):
    grouped_events = {'Reading': [], 'Work': [], 'School': [], 'Exercising': [], 'Other': []}
    
    for event in formated_events: 
        if event['summary'] in grouped_events:
            grouped_events[event['summary']].append(event)
        else:
            grouped_events['Others'].append(event)

    return grouped_events 


def get_events(from_date, to_date):
    service = setup_cal.get_calendar()

    # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # timeMin=now *in events().list
    # pylint: disable=no-member
    events_result = service.events().list(calendarId='primary', timeMin=from_date, timeMax=to_date,
                                          maxResults=100, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    # format and group events to custom form
    formated_events = format_events(events)
    grouped_events = group_events(formated_events)

    return grouped_events
