import random
import string
import requests
from bs4 import BeautifulSoup
# from dataclasses import dataclass

# Base URL to be scrapped
url = "https://www.imdb.com/chart/top"

# Data class to store the info


# @dataclass
# class Movie:
#     title: str
#     year: int
#     rating: float
#     actors: list

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
    # Selecting the ratings
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    # Generating the data from the scrapped elements
    movies_list = movie_list_generator(movie_tags, rating_tags)


# A class to give out the


def movie_list_generator(movie_tags, rating_tags):
    movies_dict = {}

    for i in range(len(movie_tags)):
        movie = movie_tags[i]
        # Use the find method to identify elements
        innerTag = movie.find('a')
        movie_name = innerTag.text
        # Attributes within is stored as a list.
        actor_list = innerTag['title']
        year = movie.find("span", class_='secondaryInfo').text
        # The values are by default stored in string
        rating = float(rating_tags[i]['data-value'])
        # Round to one decimal place
        rating = round(rating, 1)

        movies_dict[movie_name] = (rating, year, actor_list)

    return movies_dict


if __name__ == '__main__':
    main()
