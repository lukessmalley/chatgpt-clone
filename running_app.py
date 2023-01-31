
# Importing the necessary libraries
import os, sys
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Function to authenticate the user
def authenticate():
    # Setup the Google Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()
    # If credentials is stored, authenticate
    if not creds or creds.invalid:
        username = input('Enter your Google username: ')
        password = input('Enter your Google password: ')
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, username, password)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service

# Function to add events to the calendar
def add_event(service):
    # Get the name of the event, date and time from user
    event_name = input('Enter the name of the event : ')
    date = input('Enter the date of the event (YYYY-MM-DD) : ')
    time = input('Enter the time of the event (HH:MM) : ')
    # Construct the event
    event = {
        'summary': event_name,
        'start': {
            'dateTime': date + 'T' + time + ':00',
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': date + 'T' + time + ':00',
            'timeZone': 'Asia/Kolkata',
        },
    }
    # Insert the event into the user's calendar
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (created_event.get('htmlLink')))

# Main function
def main():
    # Authenticate the user
    service = authenticate()
    # Add the event to the user's calendar
    add_event(service)

# Execute the program
if __name__ == '__main__':
    main()