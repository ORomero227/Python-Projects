import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/"
                        "best-movies-2/")

response.raise_for_status()

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movies = soup.find_all(name="h3", class_="title")

with open("movies.txt", "w", encoding="utf8") as movies_files:
    for movie in movies[::-1]:
        movies_files.write(f"{movie.text}\n")
