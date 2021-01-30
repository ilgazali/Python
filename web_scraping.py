#Muhammet Ali ILGAZ
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

#(STEP-1) I sent a request to the news site whose data we want to pull.
url = "https://www.cnnturk.com/dunya/zirvedeki-isim-degisti-iste-dunyanin-en-zengini"
r = requests.get(url)

#(STEP-2) I parsed all data pulled by using BeautifulSoup Module.
soup = BeautifulSoup(r.content,"html.parser")

title = soup.find("h1",attrs={"class":"detail-title"}).span.text

date = soup.find("div",attrs={"class":"detail-metadata"}).small.span.text

text1 = soup.find("h2",attrs={"class":"detail-description m-b-lg"}).text
text2 = soup.find("div",attrs={"class":"photo-section no-title"}).p.text
text3 = soup.find("div",attrs={"class":"photo-section no-title",
                               "in-view":"photoInView(2, $inview, $inviewpart, $event)"}).p.text

category = soup.find("div",attrs={"class":"breadcrumb detail-breadcrumb"}).select("span:nth-of-type(2)")[0].find("a").text

text = text1 +"\n" +text2 +"\n" + text3

news = pd.Series(text)
titles = pd.Series(title)
dates = pd.Series(date)
categories = pd.Series(category)

print("---------------ALL PARSED DATA---------------")
print("Category: ",categories[0])
print("Date: ",dates[0])
print("Title: ",titles[0])
print("News: ",news[0])
print()


#(STEP-3) I saved all the data to the same dataframe.
df = pd.DataFrame({"Category":categories,"Title":titles,"News":news,"Date":dates})
print("---------------DATAFRAME---------------")
print(df)
print("---------------------------------------")
#I created a csv file in the same place as the python file.
df.to_csv('data.csv', index=False, encoding='utf-8')
#Please review the data.csv file generated after running the code in the compiler by importing it into the compiler and check all the data I parsed.




#(STEP-3) word separation in texts of title and news
title_words = df['Title'].apply(lambda x: str(x).split())
text_words = df['News'].apply(lambda x: str(x).split())


#(STEP-4) I converted all words to lowercase so that they are not case sensitive
news_words_list = []
title_words_list = []

for txt in text_words[0]:
    news_words_list.append(txt.lower())

for txt in title_words[0]:
    title_words_list.append(txt.lower())

#(STEP-5) I created a function that remove all punctuation marks in words to calculate the frequency
def remove_punctuations(words):
    wordsWithoutSymbols = []
    symbols = ",'."
    for word in words:
        for symbol in symbols:
            if symbol in word:
                word = word.replace(symbol,"")
        if (len(word)>0):
             wordsWithoutSymbols.append(word)
    return wordsWithoutSymbols


news_words_list = remove_punctuations(news_words_list)
title_words_list = remove_punctuations(title_words_list)

#(STEP-6) I created a function to calculate the word frequency

def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]

common_words_news = get_top_n_words(news_words_list, 25)
common_words_title = get_top_n_words(title_words_list,25)

#(STEP-7)--PLOTING-- I saved the new data I created into separate dataframes and plot them.
#to plot frequency of words in news text
df1 = pd.DataFrame(common_words_news, columns = ['Words', 'Frequency'])
plt.bar(df1["Words"],df1["Frequency"],label="Frequency Size",color='r')
plt.title("Frequency of Words in News Text")
plt.xlabel("Words")
plt.xticks(rotation=80)
plt.ylabel("Frequency")
plt.legend()
plt.show()

#to plot frequency of words in title
df1 = pd.DataFrame(common_words_title, columns = ['Words', 'Frequency'])
plt.bar(df1["Words"],df1["Frequency"],label="Frequency Size",color='b')
plt.title("Frequency of Words in Title")
plt.xlabel("Words")
plt.xticks(rotation=80)
plt.ylabel("Frequency")
plt.legend()
plt.show()