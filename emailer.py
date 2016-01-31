#DANIELA BECERRA
#This is an emailer app, to send emails to the spam van customers in
#automated way
import weather

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


def main():
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    forecast = weather.get_weather_forecast()
    print(forecast)

main()
