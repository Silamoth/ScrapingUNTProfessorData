import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_open = open("professors.txt", "r")
professors_strings = file_open.read().strip().split('\n')
file_open.close()

names = []
ratings = []
numRatings = []

#Exclude professors for which no ratings are available
for prof_string in professors_strings:
    if "N/A" not in prof_string:
        temp = prof_string.split('/')
        names.append(temp[0])
        ratings.append(temp[1])
        numRatings.append(temp[2])

professors = pd.DataFrame()
professors['Name'] = names
professors['Rating'] = ratings
professors['NumRatings'] = numRatings
professors['Rating'] = [float(x) for x in professors['Rating']]

ax, fig = plt.subplots()

plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.grid(True)
plt.title("Average Ratings of UNT Professors on RateMyProfessors.com")
professors['Rating'].hist()
print(professors['Rating'].describe())
text = "Mean: " + str(round(professors['Rating'].mean(), 3)) + "\nMedian: " + str(professors['Rating'].median())

ax.text(.05, .93, text, fontsize = 8)
