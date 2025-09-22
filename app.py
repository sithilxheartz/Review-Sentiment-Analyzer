from flask import Flask, render_template
from flask import Flask, render_template,request, redirect
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask (__name__)
logging.info('Flask server started')

data = dict()
reviews = ['Good Quality & Excellent Product ❤️','Actually didn’t expect it to be this good. My main purpose in buying this was to listen to songs and the quality when it comes to listening to songs is really good.', 'Not as Expected']
positive = 78
negative = 4

@app.route("/")
def index():

    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    logging.info('==== Open Home Page ====')

    return render_template('index.html', data = data)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    logging.info(f'Text: {text}')

    preprocessed_text = preprocessing(text)
    logging.info(f'Preprocessed Text: {preprocessed_text}')
    vectorized_text = vectorizer(preprocessed_text)
    logging.info(f'Vectorized Text: {vectorized_text}')
    prediction = get_prediction(vectorized_text)
    logging.info(f'Prediction: {prediction}')

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
