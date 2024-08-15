import requests
from win10toast import ToastNotifier

class Instagram_Popup(object):
    def __init__(self, username):
        self.username = username 
        self.current = ''
        self.startet = ''

    def followers(self):
        r = requests.get(f"https://www.instagram.com/{self.username}").text
        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        self.current = int(r[r.find(start)+len(start):r.rfind(end)])
        if self.startet == "":
            self.startet = self.current

    def main(self, notification_rate):
        notification = ToastNotifier()
        self.followers()
        while True:
            self.followers()
            messabe = f"Current: {self.current}\nStart Amount: {self.startet}"
            notification.show_toast(self.username, message, duration = notification_rate)

if __name__ == "__main__":
    username = input(r"Enter Username: ")
    try: 
        notify_rate = int(input("Enter your notification Rate: ")) * 60
    except:
        notify_rate= 5 * 60
    Instagram_Popup(username).main(notify_rate)
