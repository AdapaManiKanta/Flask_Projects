from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

# CREATE A FLASK APP
app = Flask(__name__)

# HOME PAGE route
@app.route("/")
def main():
    query = request.args.get("query", "latest")

    # Proper string formatting
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

    # Make request and parse JSON
    response = requests.get(url)
    news_data = response.json()
    # print(news_data)  # You can log this or pass it to a template
    articles = news_data.get('articles',[])
    return render_template("index.html", articles=articles)  # Replace with render_template if needed

# Proper entry point
if __name__ == "__main__":
    app.run(debug=True)
