import imdb
import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import re

for a in range(5):  #Range for no of movies
    movies = ["Barbershop","Captain America","Jack Reacher","Doctor Strange","Moana"]   # 5 Movies list
    extn = ".txt"   #Extention to use in open file command
    movieFile = movies[a]+extn
    fl = open(movieFile,'r')
    lines =  fl.read().splitlines()     #lines creat all the seperate line from given file
    ia = imdb.IMDb()        #To get imdb rating this IMDb() used from import imdb
    s_result = ia.search_movie(movies[a])
    the_unt = s_result[0]
    ia.update(the_unt)
    total_semantics = 0.0
    pos_semantics = 0.0
    neg_semantics = 0.0
    for i in range(len(lines)):         #Scan the given file to count positive and negative sentiments
        total_semantics += 1
        if 'pos:::' in lines[i]:
            pos_semantics += 1
        if 'neg:::'  in lines[i]:
            neg_semantics += 1
    f1 = open('Ratings.txt','a')        #Create file to store our sentiment rating and imdb rating in a line
    f1.write(movieFile.strip('.txt'))
    f1.write("  Positive rating = ")
    f1.write(format((pos_semantics/total_semantics)*30,'.1f'))
    f1.write(" and Negative rating = ")
    f1.write(format((neg_semantics/total_semantics)*10,'.1f'))
    f1.write(" and IMDB rating :")
    f1.write(movies[a])
    f1.write(str(the_unt['rating']))
    f1.write('!\n')
    f1.close()

f=open('Ratings.txt', 'r').read()       #This file is opened where all ratings are
y = map(float,re.findall("\d+\.\d+",f))     # Reads all the rating and use this to map on y axis

plt.axis([0,25, 0,12])

p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc="crimson")
p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc="chartreuse")
p3 = plt.Rectangle((0, 0), 0.1, 0.1, fc="Blue")

l1 = plt.legend((p1,p2), ("Positive rating",'Negative rating'), loc=1)
l2 = plt.legend([p3], ["IMDB Rating"], loc=2)
plt.gca().add_artist(l1)
labels = [' ', 'Barbershop','  ',' ', ' Cap America ','  ',' ', 'Jack Reacher','  ' ,' ', 'Doctor Strange','  ',' ', 'Moana','  ',' ',' ']

x = np.array([0,1,2,5,6,7,10,11,12,15,16,17,20,21,22]) + 1

plt.xticks(x, labels)

plt.bar(left = x, height=y, color=['crimson', 'chartreuse','blue'])

plt.grid(which='both')
plt.ylabel('These are our ratings')
plt.xlabel('These are number of movies')
plt.title("Sentiment analysis using tweets")

plt.show()

fl = open('Ratings.txt', 'w')       # On line 26  f1 = open('Ratings.txt','a') is use which stack the rating, so this is created to have new data all time
fl.write(' ')
fl.close()

