import nltk
from textblob import TextBlob

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
    
def main():
    print("Welcome! to This is Sentiment Analysis Tool By Marwan Abdulmanna")
    while true:
        text = input("Enter Text to Analyze Sentiment: (or 'quit to exit)")
        if text.lower() == 'quit':
            break
        sentiment = analyze_sentiment(text)
        print(sentiment)

if __name__ == "__main__":
    main()