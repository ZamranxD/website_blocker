import time
from datetime import datetime as dt

#setting up hosts and redirect path as variables. This following hosts path is for Linux/Mac.
#for windows, your path might be something like this.
#Please change the hosts path variable if you're on windows.
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
#this is the list of domains that you want to block. Feel free to add whichever domain you wish.
website_list = ["www.twitter.com", "twitter.com", "www.instagram.com", "instagram.com"] 


#setting up this while loop so that the script keeps on running as a process continuosly in the background
while True:
    #making a conditional to check what time it is now. 12 and 16 here refer to 12pm and 4pm. You can set these hours as per
    #your routine. The websites will not work during this time.
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        #opening the hosts file and making necessary changes according to the time of the day.
        #I don't recommend you to change the contents of this loop or the one below.
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(2) #this specifies that the script will check for the time every 2 seconds. You can change it to whatever you want.

    #PLEASE SEE THE README FOR INSTRUCTIONS HOW TO RUN THIS SCRIPT AS A BACKGROUND PROCESS SO THAT
    #YOY DON'T HAVE TO RUN IT AGAIN AND AGAIN AS A PYTHON FILE.