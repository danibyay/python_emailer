import smtplib

def send_emails(emails, schedule, forecast):
    #Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    #start TLS encryption
    server.starttls()
    #login  python12!@
    from_email= 'flyingthroughpython@gmail.com'
    #password = input('Enter password')
    #server.login(from_email, password)
    #LOGIN DOESNT WORk

    #send mails to the list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the circus!\n\n'
        message += 'Hi, ' + name + '!\n\n'
        message += forecast + '\nAnd our schedule is the following:\n'
        message += schedule + '\n\n'
        message += 'See you there! \n\n'
        #server.sendmail(from_email, from_email, 'hello this is a try, im just a codeschool student')
        print('From: '+ from_email +',\nTo: '+ to_email + '\n' + message)

    #disconnect
    server.quit()


#instead of sending the emails, I print it to the console
#because due to security, gmail won't let me actually login
#via the terminal
