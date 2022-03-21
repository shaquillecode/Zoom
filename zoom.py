"""Zoom Link Bot """
# Some core and some installed packages/modules
# If I have buttons to click on the screen,
# I will have to leverage another module that you have to install using pip called "pyautogui".
import time
import webbrowser
import schedule


def zoom_bot():
    """This will open the Zoom Invite Link"""
    link = "https://dfa.zoom.us/j/87183477990"
    webbrowser.open(f"{link}")

def aws_course():
    """This will open Amazon web services academy on the webbrowser"""
    awsacademy = "https://awsacademy.instructure.com/courses/9010/modules"
    webbrowser.open(f"{awsacademy}")

def sw_course():
    """This will open StudioWeb on the webbrowser"""
    studioweb = "https://school.studioweb.com/"
    webbrowser.open(f"{studioweb}")

def open_link(link):
    """ This will open a link on the webbrowser """
    webbrowser.open(link)

# zoom_bot()
# aws_course()
# sw_course
CLASS = "https://dfa.populiweb.com/internal/common/home.php"
open_link(CLASS)


#Schedule your function to run at a certain time.
schedule.every().monday.at("10:30").do(zoom_bot())
schedule.every().tuesday.at("10:30").do(zoom_bot())
schedule.every().wednesday.at("10:30").do(zoom_bot())
schedule.every().thursday.at("10:30").do(zoom_bot())


#What am I gonna do if it's not the scheduled time?
#Create an infinite loop that will run until the time is met.

while True:
    schedule.run_pending()
    print("Not Yet...")
    time.sleep(1)
