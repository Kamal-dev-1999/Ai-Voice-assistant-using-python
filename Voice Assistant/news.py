import requests

def get_news():
    api_key = "f3a39d4d-aa69-4907-9f09-e03c935e2348"
    base_url = f"https://eventregistry.org/api/v1/article/getArticles?apiKey={api_key}&resultType=articles&articlesSortBy=date&articlesCount=5"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        
        if "articles" in data:
            articles = data["articles"]["results"]
            news_headlines = [article["title"] for article in articles[:5]]
            return "Here are the top news headlines: " + ". ".join(news_headlines) + "."
        else:
            return "Sorry, I couldn't retrieve the news at this moment."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the news: {e}"
