# bravetart-alert:
## a baked good lover's script
I love Stella Parks's recipes, and I want to know when they're published. With this scraper, I'm notified of any new Bravetart recipes on Serious Eats.

###this project utilizes:
```
python
BeautifulSoup
requests
crontab
yagmail
```

###automatic runs:
I'm using crontab to schedule this script to run once a day at noon. This is done with a cron task:
```
* 12 * * * [navigate to python] [navigate to stella_parks_alert.py]
```
These paths will differ between machines, as will the task schedulers available. The scheduled time is arbitrary: I chose the middle of the day to raise the probability that my computer isn't asleep and once a day so as to avid unnecessary runs.

###email set up:
To send emails to myself once a new article goes up, I chose to use yagmail. [Yagmail](https://github.com/kootenpv/yagmail/blob/master/README.md) is specific to gmail, and logs into your gmail account by using your keyring. Since I am scheduling tasks, I can't confirm my password in the console to send emails. To get around this, you can provide your username and password instead. If you choose not to automate this scraper, you only need to register the account once with
```
import yagmail
yagmail.register('mygmailusername', 'mygmailpassword')
```

###first time run:
The previous_title.txt file contains the title from the most recent time that my machine has run the script, and due to the frequency of the tasks that should only result in 1 new recipe each time. However, the previous_title.txt kept in this repo could be dramatically out of date. In this case, the script only sends an email containing the newest 15 recipes!
