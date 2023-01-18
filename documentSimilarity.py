import re
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from math import *
from sklearn import preprocessing
import math
import mypy
import typing
import requests
import matplotlib

i,j=1,0;
n=[]
fullcontnt=[]
contnt=[]


# ----------------------cosine similarity--------------------
def cosine(list1, list2):

    prod=[0,0,0,0,0,0]
    mod_x=[0,0,0,0,0,0]
    mod_y=[0,0,0,0,0,0]
    for i in range(len(list1)):
        # print(i)
        prod[i] = list1[i] * list2[i]
        mod_x[i] = list1[i] * list1[i]
        mod_y[i] = list2[i] * list2[i]

    print(prod)
    print(mod_x)
    print(mod_y)

    dot_prod = sum(prod)
    mod_sum_x = sum(mod_x)
    mod_sum_y = sum(mod_y)

    print(mod_sum_x)
    print(mod_sum_y)
    print(dot_prod)

    sqrt_mod_x = sqrt(mod_sum_x)
    sqrt_mod_y = sqrt(mod_sum_y)

    print(sqrt_mod_x)
    print(sqrt_mod_y)

    denominator = sqrt_mod_x * sqrt_mod_y

    cos_sim = (dot_prod/denominator)
    print("Cosine Similarity of:",list1, " ", list2, "is " ,cos_sim)


# normalization function
def normalization(a):
    b=[]
    for n in a:
        s =(n-min(a))/(max(a)-min(a))
        b.append(s)
    return b


def webcrwal(link):
    # Fetching the Webpage.......
    content=urllib.request.urlopen(link)
    # Using the BeautifulSoup
    webpg = BeautifulSoup(content, 'lxml')

    # print(webpg)
    # print(webpg.prettify())

    for links in webpg("link"):
        links.decompose()
    # remove scripts if any
    for script in webpg("script"):
        script.decompose()

    text = webpg.text
    text_low = text.lower()
    #print(text)
    # print("----------------------------------------",text, "-------------------------------------------------")


    engineer_count=len(re.findall(r'\Wengineering\W',text_low))
    print("'engineering' word is occuring ",engineer_count," times in doc:", link)

    research_count=len(re.findall(r'\Wresearch\W',text_low))
    print("'research' word is occuring ",research_count," times in doc:", link)

    data_count=len(re.findall(r'\Wdata\W',text_low))
    print("'data' word is occuring ",data_count," times in doc:", link)

    mining_count=len(re.findall(r'\Wmining\W',text_low))
    print("'mining' word is occuring ",mining_count," times in doc:", link)

    datamining_count=len(re.findall(r'\Wdata mining\W',text_low))
    print("'data mining' word is occuring ",datamining_count," times in doc:", link)

    ml_count=len(re.findall(r'\Wmachine learning\W',text_low))
    print("'machine learning' word is occuring ",ml_count," times in doc:", link)

    CSV = [engineer_count, research_count, data_count,mining_count, datamining_count, ml_count]

    with open("count.csv", "a") as file:
        wr = csv.writer(file, dialect='excel')
        wr.writerow(CSV)
        print("Successfully added!!")

if __name__ == '__main__': 
    webcrwal("http://cis.csuohio.edu/~sschung/")
    print("----------------------------------------Crawling Next document.......------------------------------------")
    webcrwal("https://en.wikipedia.org/wiki/Engineering")
    print("----------------------------------------Crawling Next document.......------------------------------------")
    webcrwal("http://my.clevelandclinic.org/research")
    print("----------------------------------------Crawling Next document.......------------------------------------")
    webcrwal("https://en.wikipedia.org/wiki/Data_mining")
    print("----------------------------------------Crawling Next document.......------------------------------------")
    webcrwal("https://en.wikipedia.org/wiki/Data_mining#Data_mining")

    word_count = pd.read_csv("F:/count.csv")
    words = word_count.drop(columns=['data','mining'])
    print(words)
    print(words.columns)


    # Normalize the data attributes for the Iris dataset.
    normalized_X = preprocessing.normalize(words)

    print(normalized_X)
    print(normalized_X[1,:])

    for i in range(5):
        for j in range(5):
            num = normalized_X[i, :]
            den = normalized_X[j, :]
            cosine(num,den)
