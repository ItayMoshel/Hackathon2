import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

# Data type lists.
titles = []
genres = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')
for container in movie_div:
    # Name
    name = container.h3.a.text
    titles.append(name)

    # Genre
    genre = container.find('span', class_="genre").text.strip('\n').strip()
    genres.append(genre)

    # Year
    year = container.h3.find('span', class_="lister-item-year text-muted unbold").text
    years.append(year)

    # Movie's length
    runtime = container.find('span', class_="runtime").text if container.p.find('span', class_='runtime') else '-'
    time.append(runtime)

    # Imdb ratings
    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    # Metascore
    m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
    metascores.append(m_score)

    # Number of votes
    nv = container.find_all('span', attrs={'name': 'nv'})
    vote = nv[0].text
    votes.append(vote)

print(genres)

movies = pd.DataFrame({
    'movie': titles,
    'Genre': genres,
    'year': years,
    'movie_length': time,
    'imdb_score': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
})

movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['movie_length'] = movies['movie_length'].str.extract('(\d+)').astype(int)
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].astype(int)

movies.to_csv('movies.csv')
