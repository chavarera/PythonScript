import webbrowser,smtplib
import getpass  #this module help to  user password witout echo anything this work only in shell (when you run your program from command prompt or direct shell)
def get_Email():

    services=['yahoo','gmail','outlook','hotmail']
    while True:
        mail_id=input('Email : ')
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos=mail_id.find('@')
            dotcom_pos=mail_id.find('.com')
            sp=mail_id[symbol_pos+1:dotcom_pos]
            if sp in services:
                return mail_id,sp
                break
            else:
                print('We dont provide service for '+ sp)
                print('We provide services for gmail, yahoo, outlook, hotmail')
                print('Try Again...')
                continue
        else:
            print('Invalid email Try again :')
            continue

def set_SMTP_Domain(sp):
    if sp=='gmail':
        return 'smtp.gmail.com'
    elif sp=='yahoo':
        return 'smtp.mail.yahoo.com'
    elif sp=='outlook' or sp=='hotmail':
        return 'smtp-mail.outlook.com'
print('Sending Email Program')
user_mail,sp=get_Email()
password=getpass.getpass("Password: ")
while True:
    try:
        smtp_domain=set_SMTP_Domain(sp)
        conn=smtplib.SMTP(smtp_domain,587)
        conn.ehlo()
        conn.starttls()
        conn.login(user_mail,password)
    except:
        if sp=='gmail':
            print('Login Unsucessfull there may be possible two reason  ')
            print('1.You typed wrong username or password')
            print('2.allow lesssecure apps in google')
            print('want to lesssecureapps allow in gmail yes or no')
            op=input()
            if(op=='yes'):
                webbrowser.open('https://myaccount.google.com/lesssecureapps')
            else:
                print('https://myaccount.google.com/lesssecureapps go here and mannually and sllow it')
                print('please retype username and password again')
                user_mail,sp=get_Email()
                password=getpass.getpass("Password: ")
                continue
        else:
            print('login unsucessfull')
            print('please retype username and password again')
            user_mail,sp=get_Email()
            password=getpass.getpass("Password: ")
            continue
    else:
        print('login susssessfull ')
        break
print('Enter Receiver Email:')
receiver_mail,sp=get_Email()
subject=input('Subject : ')
message=input('Message : ')
conn.sendmail(user_mail,receiver_mail,'Subject : '+str(subject) + '\n\n' + str(message))
print('Email Sent Successfully')
conn.quit()
