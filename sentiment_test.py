from sentiment import analyze_sentiment

if __name__ == "__main__":
    sample_text = [
        "I love this product! It's amazing and works perfectly.",
        "I hate this! It broke after one use.",
        "It's okay, not great but not terrible either."
    ]

    for text in sample_text:
        result = analyze_sentiment(text)
        print(f"Text: {text}\nSentiment: {result}\n")