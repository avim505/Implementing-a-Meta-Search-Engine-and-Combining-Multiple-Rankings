import random
import pandas as pd
from tkinter import *
from tkinter import ttk
import csv
from sklearn.metrics import average_precision_score

# Create a list of CSV files
csv_files = []
csv_files.append("output-york07-ga-01.csv")
csv_files.append("output-york07-ga-02.csv")
csv_files.append("output-york07-ga-03.csv")
csv_files.append("output-york07-ga-04.csv")
csv_files.append("output-york07-ga-05.csv")

# Shuffle the list of filenames to get a random sample of 3 files
random.shuffle(csv_files)
csv_sample = csv_files[:3]

# Creating a dataframe for each result set
search1 = pd.read_csv(csv_sample[0])
search2 = pd.read_csv(csv_sample[1])
search3 = pd.read_csv(csv_sample[2])
#Display which files the search engine is using
print("Using sheets:", csv_sample[0] , csv_sample[1], csv_sample[2])

# MAP Calculation
def get_avg_precision(rank_list, number_docs):
    avg_precision = 0
    num_relevant_docs = 0
    for i in range(len(rank_list)):
        if rank_list[i] in number_docs:
            num_relevant_docs += 1
            avg_precision += num_relevant_docs / (i+1)
    if num_relevant_docs > 0:
        avg_precision /= num_relevant_docs
    else:
        avg_precision = 0
    return avg_precision

# Code for the GUI using tkinter
root = Tk()
root.title("Top 1,000 Retrieval Results")
root.geometry("500x500")

# create a main frame for the GUI
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# create a canvas to hold the search results
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas to use the scrollbar
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# create a second frame to hold the search results within the canvas
second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


# create a label for the search entry field
search_label = Label(root, text="Search TopicID or Doc ID")
search_label.pack()

# create a text entry field for the user to enter a search phrase
phrase = IntVar()
search_doc = Entry(root, textvariable=phrase, width=50)
search_doc.pack()


# define a function to perform the search
def Metasearch():
    # Creating a dataframe for the querired topic from searchengine 1
    Topic = []
    DocID = []
    Rank = []
    Okapi = []
    Offset = []
    Bytes = []
    TagID = []
    for i in range(len(search1.index)):
        if (search1.Topic[i] == int(phrase.get())):
            Topic.append(search1.Topic[i])
            DocID.append(search1.DocID[i])
            Rank.append(search1.Rank[i])
            Okapi.append(search1.Okapi[i])
            Offset.append(search1.Offset[i])
            Bytes.append(search1.Bytes[i])
            TagID.append(search1.TagID[i])

        elif (search1.DocID[i] == int(phrase.get())):
            Topic.append(search1.Topic[i])
            DocID.append(search1.DocID[i])
            Rank.append(search1.Rank[i])
            Okapi.append(search1.Okapi[i])
            Offset.append(search1.Offset[i])
            Bytes.append(search1.Bytes[i])
            TagID.append(search1.TagID[i])

        elif (search1.Okapi[i] == int(phrase.get())):
            Topic.append(search1.Topic[i])
            DocID.append(search1.DocID[i])
            Rank.append(search1.Rank[i])
            Okapi.append(search1.Okapi[i])
            Offset.append(search1.Offset[i])
            Bytes.append(search1.Bytes[i])
            TagID.append(search1.TagID[i])

    df1 = pd.DataFrame({'Topic': Topic,
                        'DocID': DocID,
                        'Rank': Rank,
                        'Okapi': Okapi,
                        'Offset': Offset,
                        'Bytes': Bytes,
                        'TagID': TagID})

    # Creating a dataframe for the querired topic from searchengine 2
    Topic2 = []
    DocID2 = []
    Rank2 = []
    Okapi2 = []
    Offset2 = []
    Bytes2 = []
    TagID2 = []
    for j in range(len(search2.index)):
        if (search2.Topic[j] == int(phrase.get())):
            Topic2.append(search2.Topic[j])
            DocID2.append(search2.DocID[j])
            Rank2.append(search2.Rank[j])
            Okapi2.append(search2.Okapi[j])
            Offset2.append(search2.Offset[j])
            Bytes2.append(search2.Bytes[j])
            TagID2.append(search2.TagID[j])

        elif (search2.DocID[j] == int(phrase.get())):
            Topic2.append(search2.Topic[j])
            DocID2.append(search2.DocID[j])
            Rank2.append(search2.Rank[j])
            Okapi2.append(search2.Okapi[j])
            Offset2.append(search2.Offset[j])
            Bytes2.append(search2.Bytes[j])
            TagID2.append(search2.TagID[j])

        elif (search2.Okapi[j] == int(phrase.get())):
            Topic2.append(search2.Topic[j])
            DocID2.append(search2.DocID[j])
            Rank2.append(search2.Rank[j])
            Okapi2.append(search2.Okapi[j])
            Offset2.append(search2.Offset[j])
            Bytes2.append(search2.Bytes[j])
            TagID2.append(search2.TagID[j])

    df2 = pd.DataFrame({'Topic': Topic2,
                        'DocID': DocID2,
                        'Rank': Rank2,
                        'Okapi': Okapi2,
                        'Offset': Offset2,
                        'Bytes': Bytes2,
                        'TagID': TagID2})

    # Creating a dataframe for the querired topic from searchengine 3
    Topic3 = []
    DocID3 = []
    Rank3 = []
    Okapi3 = []
    Offset3 = []
    Bytes3 = []
    TagID3 = []

    for k in range(len(search3.index)):
        if (search3.Topic[k] == int(phrase.get())):
            Topic3.append(search3.Topic[k])
            DocID3.append(search3.DocID[k])
            Rank3.append(search3.Rank[k])
            Okapi3.append(search3.Okapi[k])
            Offset3.append(search3.Offset[k])
            Bytes3.append(search3.Bytes[k])
            TagID3.append(search3.TagID[k])

        elif (search3.DocID[k] == int(phrase.get())):
            Topic3.append(search3.Topic[k])
            DocID3.append(search3.DocID[k])
            Rank3.append(search3.Rank[k])
            Okapi3.append(search3.Okapi[k])
            Offset3.append(search3.Offset[k])
            Bytes3.append(search3.Bytes[k])
            TagID3.append(search3.TagID[k])

        elif (search3.Okapi[k] == int(phrase.get())):
            Topic3.append(search3.Topic[k])
            DocID3.append(search3.DocID[k])
            Rank3.append(search3.Rank[k])
            Okapi3.append(search3.Okapi[k])
            Offset3.append(search3.Offset[k])
            Bytes3.append(search3.Bytes[k])
            TagID3.append(search3.TagID[k])

    df3 = pd.DataFrame({'Topic': Topic3,
                        'DocID': DocID3,
                        'Rank': Rank3,
                        'Okapi': Okapi3,
                        'Offset': Offset3,
                        'Bytes': Bytes3,
                        'TagID': TagID3})

    # Results that match the query across three search engines
    df1.to_csv('df1.csv')
    df2.to_csv('df2.csv')
    df3.to_csv('df3.csv')

    # Combining the search results from 3 different search engines
    final = pd.concat([df1, df2, df3])
    final.to_csv('final.csv')

    # Sorting the okapi scores for each document from greatest to least and reranking
    SortedList = final.sort_values('Okapi', ascending=False)
    #reset index to 0-based indexing
    SortedList = SortedList.reset_index(drop=True)
    #assign new ranks based on okapi column
    SortedList['Rank'] = SortedList.index + 1
    # Printing the top 1000 results based on the okapi score for each query
    SortedList.head(1000).to_csv('final1000.csv', index=False)

    # Read CSV file and add labels to second frame
    with open('final1000.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            label = Label(second_frame, text=row)
            label.pack()


# Create the search button
myButton = Button(root, text="Search", command=Metasearch)
myButton.pack()

# Start the main event loop
root.mainloop()
