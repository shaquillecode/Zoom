'''zoom.py'''
import time
import webbrowser
import schedule


def meeting():
    '''
    This function will open the zoom meeting
    '''
    # zoom_link variable contains value of a link( Zoom Invite Link )
    zoom_link = "https://dfa.zoom.us/j/88233250411"

    # This open method from the webbrowser module will launch your meeting
    # Adjust your settings of the default web browser/zoom app
    # On your local machine to allow automatic launch
    webbrowser.open(f"{zoom_link }")

def open_link(link):
    '''
    Pass in any link to this function
    Have it open that link on the web browser
    '''
    webbrowser.open(link)

# Run your whole college with Populi
POPULI = "https://populi.co/"
open_link(POPULI)


#Schedule your function to run at a certain time.
schedule.every().monday.at("14:00").do(meeting)
schedule.every().tuesday.at("14:00").do(meeting)
schedule.every().wednesday.at("14:00").do(meeting)
schedule.every().thursday.at("14:00").do(meeting)
schedule.every().friday.at("14:00").do(meeting)


# If it's not the scheduled time?
# I will create an infinite loop that will run until the time is met
# 1800 seconds equals 30 minutes which is my scheduled daily total lunch break
# So I will schedule an automatic zoom meeting return from my lunch break

FLAG = True
NUM = 0

while FLAG:
    if NUM == 1800:
        FLAG = False
    else:
        schedule.run_pending()
        print("Not Yet...")
        time.sleep(1)
        NUM += 1
