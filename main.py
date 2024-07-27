from bs4 import BeautifulSoup
import requests

rotten_tomatoes = "https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular"

response = requests.get(rotten_tomatoes)

soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all("div", class_ = "flex-container")

for movie in all_movies:
    Movie_Details = {}
    Movie_Details['Movie Title'] = movie.find("rt-img").attrs['alt']
    Movie_Details['Critics Rating'] = movie.find_all('rt-text')[0].text
    Movie_Details['Audience Score'] = movie.find_all('rt-text')[1].text
    Movie_Details['Date Released'] = movie.find_all('span')[2].text.strip()[7:]
    
    print("-" * 50)
    print(f"""Movie Title: {Movie_Details['Movie Title']}
Critics Rating: {Movie_Details['Critics Rating']}
Audience Score: {Movie_Details['Audience Score']}
Date Released: {Movie_Details['Date Released']}""")
    print("-" * 50)