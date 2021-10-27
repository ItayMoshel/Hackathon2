import csv
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Movie scraper")

root.iconbitmap('imdb.ico')

genre_label = Label(root, text="Search by Genre.")
genre_label.grid(row=0, column=0)

input_genre = Entry(root)
input_genre.grid(row=1, column=0)

st = ScrolledText(root, width=100, height=25)
st.grid(row=0, column=1, rowspan=19)


def clearst():
    st.delete('0.0', END)
    input_genre.delete(0, 'end')


def search_by_genre():
    if st.compare("end-1c", "==", "1.0"):
        word = input_genre.get()
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
                        st.insert('1.0', "Title: " + title + " Year: " + year + " Score: " + imdb_score + "\n\n")
                        # lob = Label(root, text="Title: " + title + " Year: " + year + " Score: " + imdb_score)
                        # input_func.insert(0, "Title: " + title + " Year: " + year + " Score: " + imdb_score)
                    else:
                        st.insert('1.0', word.upper() + " Not found.")
                        break

    else:
        if not st.compare("end-1c", "==", "1.0"):
            clearst()
            word = input_genre.get()
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
                            st.insert('1.0', "Title: " + title + " Year: " + year + " Score: " + imdb_score + "\n\n")
                        else:
                            st.insert('1.0', word.upper() + " Not found.")
                            break


my_button = Button(root, text="Search", command=search_by_genre)
my_button.grid(row=2, column=0)

duration_label = Label(root, text="Search by duration.")
duration_label.grid(row=3, column=0)

input_duration1 = Entry(root)
input_duration1.insert(0, "Less then: ")
input_duration1.grid(row=4, column=0)

input_duration2 = Entry(root)
input_duration2.insert(0, "More then:")
input_duration2.grid(row=5, column=0)


def search_by_duration():
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
                                  "Title: " + title + " Movie length: " + time + " Genre: " + genre + "Year " + year + " Score: " + imdb_score + "\n\n")
                    else:
                        st.insert('1.0', 'invalid input. please input numbers only.')

    else:
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
                            log = Label(root,
                                        text="Title: " + title + " Movie length: " + time + " Genre: " + genre + "Year " + year + " Score: " + imdb_score)
                            st.insert('1.0',
                                      "Title: " + title + " Movie length: " + time + " Genre: " + genre + "Year " + year + " Score: " + imdb_score + "\n\n")


my_button2 = Button(root, text="Search", command=search_by_duration)
my_button2.grid(row=6, column=0)

# clear_button = Button(root, text="Clear")
# clear_button.pack()


clear_btn = Button(root, text="Clear", command=clearst)
clear_btn.grid(row=7, column=0)

quit_button = Button(root, text="Exit", command=root.quit)
quit_button.grid(row=8, column=0)

labelitem1 = Label(root, text="")
labelitem2 = Label(root, text="")
labelitem3 = Label(root, text="")
labelitem4 = Label(root, text="")
labelitem5 = Label(root, text="")
labelitem6 = Label(root, text="")
labelitem7 = Label(root, text="")
labelitem8 = Label(root, text="")
labelitem9 = Label(root, text="")
labelitem10 = Label(root, text="")

labelitem1.grid(row=10, column=0)
labelitem2.grid(row=11, column=0)
labelitem3.grid(row=12, column=0)
labelitem4.grid(row=13, column=0)
labelitem5.grid(row=14, column=0)
labelitem6.grid(row=15, column=0)
labelitem7.grid(row=16, column=0)
labelitem8.grid(row=17, column=0)
labelitem9.grid(row=18, column=0)
labelitem10.grid(row=19, column=0)

root.mainloop()
