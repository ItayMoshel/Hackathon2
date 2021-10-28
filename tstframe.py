import csv
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Movie scraper")
root.configure(background='#A4B8C4')
root.iconbitmap('imdb.ico')

# Frame for control panel
frame1 = LabelFrame(root, bg="#A4B8C4")
# Frame for Content
frame2 = LabelFrame(root, text="IMDB", bg="#6E8387", fg="white", font=("Ariel", 25))
frame1.grid(row=0, column=0, padx=10)
frame2.grid(row=0, column=1, padx=5)

genre_label = Label(frame1, text="Search by Genre.", bg='#A4B8C4')
genre_label.grid(row=0, column=0, pady=0)

input_genre = Entry(frame1)
input_genre.grid(row=1, column=0)

st = ScrolledText(frame2, width=100, height=40, bg="#6E8387", fg="white", font=("Ariel", 15))
st.pack()


# Function for clearing Scrolled text.
def clearst():
    st.delete('0.0', END)


# Searching by genre.
def search_by_genre():
    # Checks if scrolled text is empty
    # if st.compare("end-1c", "==", "1.0"):
    if len(st.get("1.0", "end-1c")) == 0:
        word = input_genre.get()
        with open('top50_movies.csv', 'r') as db:
            reader = csv.reader(db, delimiter=',')
            # Skipping the first line from DB
            header = next(reader)
            if header is not None:
                for line in reader:
                    movie_title = line[1]
                    genre = line[2]
                    year = line[3]
                    imdb_score = line[5]
                    if word.capitalize() in genre:
                        st.insert('1.0', "Title: " + movie_title + ", Year: " + year + ", Score: " + imdb_score + ".\n\n")
                    else:
                        if word.capitalize() not in genre:
                            st.insert('1.0', word.upper() + " Not found.")
                            break

    # Checks if the scrolled text is empty, if it is not, it clears it.
    elif not len(st.get("1.0", "end-1c")) == 0:
        clearst()
        word = input_genre.get()
        with open('top50_movies.csv', 'r') as db:
            reader = csv.reader(db, delimiter=',')
            header = next(reader)
            if header is not None:
                for line in reader:
                    movie_title = line[1]
                    genre = line[2]
                    year = line[3]
                    imdb_score = line[5]
                    if word.capitalize() in genre:
                        st.insert('1.0', "Title: " + movie_title + ", Year: " + year + ", Score: " + imdb_score + ".\n\n")


my_button = Button(frame1, text="Search", command=search_by_genre, bg='#A4B8C4')
my_button.grid(row=2, column=0)

duration_label = Label(frame1, text="Search by duration.", bg='#A4B8C4')
duration_label.grid(row=3, column=0, pady=10)

input_duration1 = Entry(frame1)
input_duration1.insert(0, "Less then: ")
input_duration1.grid(row=4, column=0)

input_duration2 = Entry(frame1)
input_duration2.insert(0, "More then:")
input_duration2.grid(row=5, column=0)


# Searching by movie duration.
def search_by_duration():
    # Checks if scrolled text is empty
    if st.compare("end-1c", "==", "1.0"):
        duration1 = int(input_duration1.get())
        duration2 = int(input_duration2.get())
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
                        st.insert('1.0',
                                  "Title: " + title + ", Movie length: " + time + ", Genre: " + genre + ", Year: " + year + ", Score: " + imdb_score + ".\n\n")

    else:
        # Checks if the scrolled text is empty, if it is not, it clears it.
        if not st.compare("end-1c", "==", "1.0"):
            clearst()
            duration1 = int(input_duration1.get())
            duration2 = int(input_duration2.get())
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
                            st.insert('1.0',
                                      "Title: " + title + ", Movie length: " + time + ", Genre: " + genre + ", Year: "+ year + ", Score: " + imdb_score + ".\n\n")


my_button2 = Button(frame1, text="Search", command=search_by_duration)
my_button2.grid(row=6, column=0)

# clear_button = Button(root, text="Clear")
# clear_button.pack()


clear_btn = Button(frame1, text="Clear", command=clearst, bg='#A4B8C4')
clear_btn.grid(row=7, column=0, pady=10)

quit_button = Button(frame1, text="Exit", command=root.quit, bg='#A4B8C4')
quit_button.grid(row=10, column=0, pady=10)

root.mainloop()
