from flask import Flask, render_template
from flask import Flask, render_template,request, redirect
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask (__name__)

data = dict()
reviews = ['Good Condition & Excellent Product ❤️', 'Not as Expected','Actually didn’t expect it to be this good. My main purpose in buying this was to listen to songs and the quality when it comes to listening to songs is really good.']
positive = 78
negative = 4

@app.route("/")
def index():

    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    return render_template('index.html', data = data)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    preprocessed_text = preprocessing(text)
    vectorized_text = vectorizer(preprocessed_text)
    prediction = get_prediction(vectorized_text)

    if prediction == 'negative':
        global negative
        negative +=1
    else:
        global positive
        positive +=1

    reviews.insert(0,text)
    return redirect(request.url)

if __name__ == "__main__":
    app.run()
