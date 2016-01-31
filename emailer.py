#DANIELA BECERRA
#This is an emailer app, to send emails to the spam van customers in
#automated way


#create a new list for the emails
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



print(emails)

#min 10:55
