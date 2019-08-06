# Alexandra Plukis
# July 28, 2019
# I just love Stella Parks's recipes and writing, is that so wrong?

# import BeautifulSoup and requests to be able to read the HTMl information
# from Serious Eats
from bs4 import BeautifulSoup
import requests
import yagmail

receiver = "youremail@gmail.com"
name = "yourname"
posts = []
titles = []
urls = []

# get the most recent title that
# was input on the last execution
with open('your/path/previous_title.txt', 'r') as file:
    previous = file.read()

# this is Stella Park's page on Serious Eats where all of her
# articles are found
r = requests.get('https://www.seriouseats.com/editors/stella-parks')
soup = BeautifulSoup(r.content, 'html.parser')

# the section of the page where all articles are listed in module form
post_section = soup.find('section', {'class': "block block-primary block-no-nav block-has-kicker", 'id': 'posts'})

# making a list of each individual post (article)
posts = (post_section.find_all('div', {'class': "metadata"}))

#titles[0] will be the most recent title by Parks
for post in posts:
    # save each title and url to a list of all available articles
    # (without clicking "see more")
    titles.append(post.find('h4', {'class':"title"}).contents[0])
    urls.append((post.find('a', {'class': 'module__link'})).get('href'))

i = 0
# if the most recent title is the one that was most recent on the
# last execution, no new articles :-( )
# if titles[i] == previous:
# can have some alert system set up, but I do not want any
# more emails than necessary
# otherwise, new articles!! We want to list all of them for binge reading
# if there are multiple articles (but stopping if we've reached the end of
# the list containing the titles scraped)
if titles[i] != previous:
    body = "Hi " + name + "!" + "\n\tHere's what's new:\n"
    while ((i < len(titles)) and (titles[i] != previous)):
        body += ('%d.) %s\n%s\n' % ((i + 1), titles[i], urls[i]))
        i += 1
    body += "That's all, enjoy!"
    yag = yagmail.SMTP('yourusername', 'yourpassword')
    yag.send(
        to=receiver,
        subject="New Bravetart Recipe",
        contents=body,
    )
    # reqriting our file to store the most recent article written!
    with open('your/path/previous_title', 'w') as file:
        file.write(titles[0])
