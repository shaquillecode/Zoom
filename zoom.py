'''zoom.py'''
import time
import webbrowser
import schedule



def open_link(link):
    '''
    Pass in any link to this function
    Have it open that link on the webbrowser.
    '''
    webbrowser.open(link)


def course():
    '''
    Pass in any link to this function
    Have it open that link on the webbrowser.
    '''
    academy = "https://"
    webbrowser.open(f"{academy}")

def foundations():
    '''
    Pass in any link to this function
    Have it open that link on the webbrowser.
    '''
    #Zoom Invite Link goes here:
    zoom_link = "https://"

    #This will open your Zoom Invite Link
    webbrowser.open(f"{zoom_link }")


POPULI = "https://"
open_link(POPULI)
course()
foundations()

#Schedule your function to run at a certain time.

schedule.every().monday.at("10:30").do(foundations())
schedule.every().tuesday.at("10:30").do(foundations())
schedule.every().wednesday.at("10:30").do(foundations())
schedule.every().thursday.at("10:30").do(foundations())
schedule.every().friday.at("10:30").do(foundations())


#What if it's not the scheduled time?

#Create an infinite loop that will run until the time is met.
FLAG = True
NUM = 0

while FLAG:
    if NUM == 3600:
        FLAG = False
    else:
        schedule.run_pending()
        print("Not Yet...")
        time.sleep(1)
        NUM += 1
