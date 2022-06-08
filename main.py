import random
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

# The main function


def main():
    # Ping the website
    response = requests.get(url)
    html = response.text

    # Look for the html element with the movie info
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Select the table data which contains movie info
    movie_tags = soup.select('td.titleColumn')
    movie_0 = movie_tags[0]

    movie_0_year = movie_0.find("span", class_='secondaryInfo').text
    print(movie_0_year)


if __name__ == '__main__':
    main()
