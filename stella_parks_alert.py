from bs4 import BeautifulSoup
import requests

a_urls = []
urls_to_check = []

r_technique = requests.get('https://www.seriouseats.com/techniques')
soup_technique = BeautifulSoup(r_technique.content, 'html.parser')

latest = soup_technique.find('section', {'class':"block block-primary block-has-featured block-has-kicker", 'id':"the-latest"})
recipe_modules = latest.find_all('div', {'class':"module"})

for recipe in recipe_modules:
    a_urls.append(recipe.find_all('a', {'class':"module__link"}))
for i in range(0, len(a_urls)):
    urls_to_check.append(a_urls[i][1].get('href'))

rs = []
soups = []
i = 0

for url in urls_to_check:
    rs.append(requests.get(url))
    soups.append(BeautifulSoup(rs[i].content, 'html.parser'))
    name = soups[i].find('div', {'class':"author-byline brief"})
    print(name.find('a', {'class': 'name'}).contents[0])
    title = soups[i].find('div',  {'class':"entry-header-inner"})
    print(title.find('h1', {'class':"title"}).contents[0])
    i += 1
