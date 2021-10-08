import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls055386972/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# # You now can query the `soup` object!
# soup.title.string
# soup.find("h1")
# soup.find_all("a")

movie_elements = soup.find_all("div", class_="lister-item-content")

movies = []

for movie_element in movie_elements:
    title = movie_element.find("h3", class_="lister-item-header").find("a").string
    duration = movie_element.find("span", class_="runtime").string.rstrip(" min")
    movies.append(
        {
            "title": title,
            "duration": duration,
        }
    )

pprint(movies)
