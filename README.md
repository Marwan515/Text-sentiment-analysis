# Sentiment Analysis Tool

## Overview

The **Sentiment Analysis Tool** is a web application that allows users to input text and receive an analysis of the sentiment expressed in that text. The tool determines whether the sentiment is positive, negative, or neutral using natural language processing techniques.

## Features

- **Real-Time Sentiment Analysis:** Input text and receive instant feedback on the sentiment.
- **Simple Web Interface:** Easy-to-use interface for text input and sentiment results.
- **Flask and TextBlob Integration:** Utilizes Flask for the web framework and TextBlob for sentiment analysis.
- Bulma CSS for Styling: Leverages Bulma, a modern CSS framework, to create a clean and responsive user interface.

## Project Structure

- sentiment.py sentiment-analysis-tool
- /templates/index.html # HTML template for the web interface
- app.py # Main Flask application file
- README.md # Project documentation
- requirements.txt # List of dependencies


## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.6+**: The programming language used for the project.
- **pip**: Python package manager for installing dependencies.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/sentiment-analysis-tool.git
    cd sentiment-analysis-tool
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

No additional configuration is necessary for this project. All required libraries are listed in `requirements.txt`.

### Running the Application

1. **Start the Flask Application**:
    ```bash
    python3 app.py
    ```

2. **Access the Application**:
    Open a web browser and go to `http://127.0.0.1:5000/` to use the Sentiment Analysis Tool.

## Usage

1. **Enter Text**:
    On the homepage, input any text you wish to analyze for sentiment.

2. **Analyze**:
    Click the "Analyze" button to submit the text.

3. **View Results**:
    The application will display whether the sentiment is positive, negative, or neutral.

## Example

### Input

- 'I absolutely love this new product! It works great and is very easy to use.'

### Output
- 'Sentiment: Positive, Rating 0.51'

## Project Details

### `app.py`

  ```python
    from flask import Flask, render_template, request

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
  ```
  ```python
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
  ```

### index.html
  ```html
    <!DOCTYPE html>
    <html lang="en" data-theme="dark">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Text Sentiment Analysis</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.1/css/bulma.min.css">
    </head>
    <body>
      <header>
        <div class="container">
          <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="navbar-brand hero">
              <a class="navbar-item" href="/"><h2 class="title is-2">Text-Sentiment-Analysis</h2></a>
            </div>
          </nav>
        </div>
      </header>
      <main class="mt-3">
        <div class="container">
          <form action="/analyze" method="post">
            <div class="field">
              <label class="label">Sentiment Text: </label>
              <div class="control">
                <textarea name="text" class="textarea is-info" rows="4" placeholder="Enter The Text To Calculate sentiment"></textarea>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-dark is-medium is-fullwidth" type="submit">
                  Analyze
                </button>
              </div>
            </div>
          </form>
        </div>
        {% if sentiment %}
          <div class="card container mt-3 mb-3">
            <header class="card-header">
              <p class="card-header-title">Text Sentiment</p>
            </header>
            <div class="card-content">
              <div class="content">
                <h4 class="title is-4">Text: {{ text }}</h4><br/>
                <h4 class="title is-4">Sentiment: {{ sentiment }}</h4>
              </div>
            </div>
          </div>
        {% endif %}
      </main>
      <footer class="footer">
        <div class="content has-text-centered">
          <a href="https://github.com/Marwan515">
            <button class="button is-dark is-medium is-fullwidth pb-0 pt-2 mt-2">
              Text-Sentiment-Analysis By Marwan Abdulmannan <figure class="image is-64x64"><img src="/static/GitHub-logo.png" alt="github logo"></figure>
            </button>
          </a>
        </div>
      </footer>
    </body>
    </html>
  ```

### requirement.txt
- Flask==3.0.3
- textblob==0.18.0.post0
- nltk==3.8.1

## Troubleshooting
- HTML Not Found Error: Ensure index.html is in a templates folder located in the same directory as app.py.
- Dependency Issues: Ensure all dependencies in requirements.txt are installed in your virtual environment.

## Contact
For any questions or suggestions, feel free to contact me at Marwanabdulmannan@gmail.com

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request.

## License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.