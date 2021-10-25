import csv


#
#
def search_by_genre():
    word = input('Enter genre:\n')

    with open('top50_movies.csv', 'r') as db:
        reader = csv.reader(db, delimiter=',')
        for line in reader:
            title = line[1]
            genre = line[2]
            year = line[3]
            imdb_score = line[5]
            if word.capitalize() in genre:
                print(f"title: {title}, score: {imdb_score}")


search_by_genre()

with open('top50_movies.csv', 'r') as db:
    reader = csv.reader(db, delimiter=',')
    for line in reader:
        print(line[1], line[2], line[3], line[5])
