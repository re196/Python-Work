3# SCHOOL NOTIFICATION SYSTEM 
class Notification:
    def send_message(self):
        print("Sending notification")



class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email")



class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS")



class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via Mobile App")


email = EmailNotification()
sms = SMSNotification()
app = AppNotification()

notifications = [email, sms, app]

for n in notifications:
    n.send_message()