# Question-Answering-System-for-Webpages-content-Analysis

For the text analysis tasks, clustering each document in a collection into a certain number of topics or to find the Top N most related documents in a collection per a given user query. Here, we are given 5 documents. Out of which, we are to find 6 keywords and the count of each keywords in each of the documents. This is used for the Question-Answering system, where the user enters the search queries/keywords and the algorithm finds the matching words and their counts respectively by parsing through each of the document.

Below are the 5 documents that are to be used for this task.
Doc1: http://cis.csuohio.edu/~sschung/
Doc2: https://en.wikipedia.org/wiki/Engineering
Doc3: http://my.clevelandclinic.org/research
Doc4: https://en.wikipedia.org/wiki/Data_mining
Doc5; https://en.wikipedia.org/wiki/Data_mining#Data_mining

From these documents, the user needs to find the following words count for each of the documents. 
"engineering", "research", "data", "mining", "data mining", "machine learning"

For searching the frequency of each word from each documents, I have created a function with takes the website link that we need to crawl through. Creating the function helps to
give multiple links and makes the task much more easier.

# documentSimilarity.py

It consist of the function that compares the keywords occurence in a particular document with it's occurence in the remaining documents one by one to generate the Similarity Matrix of each keywords. 
