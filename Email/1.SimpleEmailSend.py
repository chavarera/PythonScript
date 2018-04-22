#To send Email From Python file you need to import smtplib
import smtplib

#then create connection objects
conn=smtplib.SMTP('smtp.gmail.com',587)
#here SMTP() function takes two input
#1.smtp.gmail.com--this is email address of gmail you can findout other adress on google
#2.587--this is port number of smtp.gmail.com


#now say hello to smtp.gmail.com server
conn.ehlo()


#To send email using encryption then
conn.starttls()

#now login your gmail account using login()
conn.login('username','password')

#Now send email using sendmail(fromadress,toadress,message)
conn.sendmail('fromaddress','toaddress','message')
#this will send a email to toaddress with blank subjects

#send email with subject
conn.sendmail('fromaddress','toaddress','Sub :subject \n\n message here')


#After sending email we need to close connection object
conn.quit()