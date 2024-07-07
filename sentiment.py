from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)
# The Line Below Was Used To Download the nltk Data, required to run this only once
# Uncomment the line below and run: 'python3 sentiment.py' after the download ctrl-c then comment the line below 
# nltk.download('punkt')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    fs = format(sentiment, ".2f")
    if sentiment > 0:
        return f"Positive, Rating {fs}"
    elif sentiment < 0:
        return f"Negative, Rating {fs}"
    else:
        return f"Nuetral, Rating {fs}"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyze_sentiment(text)
    return render_template('index.html', sentiment=sentiment, text=text)

if __name__ == "__main__":
    app.run(debug=True)