
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
import numpy as np
import csv

X_all = []
Y_all = []

with open("sentences.csv", "r", encoding="utf-8") as fp :
    rd = csv.reader(fp)

    for data in rd :
        X_all.append(data[1])

        if int(data[2]) > 5 :
            Y_all.append(1)

        else :
            Y_all.append(0)

X_all, Y_all = np.array(X_all), np.array(Y_all, dtype=np.int64)

print("x : ", len(X_all))

text_dic = CountVectorizer()
text_dic.fit(X_all)

#print(text_dic.vocabulary_)

X_train, X_test, Y_train, Y_test = train_test_split(X_all, Y_all, test_size = 0.2, random_state=1234)
X_train_counts = text_dic.transform(X_train)

nb_model = MultinomialNB()
nb_model.fit(X_train_counts, Y_train)

nb_test_count = text_dic.transform(X_test)
nb_predict_value = nb_model.predict(nb_test_count)

# predict value = 1 (good)
# prodict value = 0 (bad)

#print(list(zip(X_test, nb_predict_value)))
#print(list(zip(nb_predict_value, Y_test)))

scores = cross_val_score(nb_model, nb_test_count, Y_test, cv=5)
print(scores)

input_text = input("확인할 텍스트 : ")
print(nb_model.predict(text_dic.transform(np.array([input_text]))))




