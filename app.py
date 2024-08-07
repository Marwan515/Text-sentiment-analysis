from flask import Flask, request, render_template
from sentiment import analyze_sentiment
app = Flask(__name__)

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