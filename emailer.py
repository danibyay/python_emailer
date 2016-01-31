#DANIELA BECERRA
#This is an emailer app, to send emails to the spam van customers in
#automated way
import requests

def get_emails():
    #create a new dictionary for the emails
    emails = {}

    #open the file
    try:
        email_file = open('emails.txt', 'r')
        #insert the actual emails in our list without \n
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    #open and read file for schedules
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Guadalajara,mx&units=metric&appid=81f527ece7b1f5d6b47c23d1d6767c3d'
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    print(weather_json)

def main():
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    get_weather_forecast()

main()
