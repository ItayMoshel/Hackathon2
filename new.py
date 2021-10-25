import csv
import random


def search_by_genre():
    word = input('Enter genre:\n')
    with open('top50_movies.csv', 'r') as db:
        reader = csv.reader(db, delimiter=',')
        header = next(reader)
        if header is not None:
            for line in reader:
                title = line[1]
                genre = line[2]
                year = line[3]
                imdb_score = line[5]
                if word.capitalize() in genre:
                    print(f"Title: {title}, Year: {year}, Score: {imdb_score}")


search_by_genre()


def search_by_score():
    score = input("Enter score:\n")
    with open('top50_movies.csv', 'r') as db:
        reader = csv.reader(db, delimiter=',')
        header = next(reader)
        if header is not None:
            for line in reader:
                title = line[1]
                genre = line[2]
                year = line[3]
                imdb_score = line[5]
                if imdb_score > score:
                    print(f"Title: {title}, Year: {year}, Genre: {genre}, Score: {imdb_score}")


search_by_score()


def search_by_duration():
    duration1 = int(input("Duration(in minutes): less then; \n"))
    duration2 = int(input("Duration(in minutes): more then;\n"))
    with open('top50_movies.csv', 'r') as db:
        reader = csv.reader(db, delimiter=',')
        header = next(reader)
        if header is not None:
            for line in reader:
                title = line[1]
                genre = line[2]
                year = line[3]
                time = line[4]
                imdb_score = line[5]
                if duration2 < int(time) < duration1:
                    print(f"Title: {title}, Duration: {time}, Year: {year}, Genre: {genre}, Score: {imdb_score}")


search_by_duration()
