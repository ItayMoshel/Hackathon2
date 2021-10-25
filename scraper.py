import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd


def top50_scraper():
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

    top50_movies = pd.DataFrame({
        'movie': titles,
        'Genre': genres,
        'year': years,
        'movie_length': time,
        'imdb_score': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
    })

    # Converting data types.
    top50_movies['votes'] = top50_movies['votes'].str.replace(',', '').astype(int)
    top50_movies['movie_length'] = top50_movies['movie_length'].str.extract('(\d+)').astype(int)
    top50_movies['year'] = top50_movies['year'].str.extract('(\d+)').astype(int)
    top50_movies['metascore'] = top50_movies['metascore'].astype(int)

    # Saving to file.
    top50_movies.to_csv('top50_movies.csv')


today = str(datetime.date.today())
today.split('-')
year, month, day = today.split('-')


def upcoming_movies_scraper():
    headers = {"Accept-Language": "en-US, en;q=0.5"}

    url = f"https://www.imdb.com/movies-coming-soon/{year}-{month}/?ref_=cs_dt_nx"

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    # Data type lists.
    titles = []
    genres = []

    movie_div = soup.find_all('div', class_="list_item odd")
    for container in movie_div:
        # Name
        name = container.h4.a.text
        titles.append(name)

        # Genre
        genre = container.p.span.text
        genres.append(genre)

    movie_div = soup.find_all('div', class_="list_item even")
    for container in movie_div:
        # Name
        name = container.h4.a.text
        titles.append(name)

        # Genre
        genre = container.p.span.text
        genres.append(genre)

    upcoming = pd.DataFrame({
        'name': titles,
        'genre': genres,
    })

    # Saving to file.
    upcoming.to_csv("upcoming_movies.csv")


top50_scraper()
upcoming_movies_scraper()
