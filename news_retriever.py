# Use this automated script to stay updated on daily world news anytime, in any language from any country/region. This API allows you to get 50 news articles for free every day.

# World News Fetcher
# pip install requests
import requests
ApiKey = "YOUR_API_KEY"
url = "https://api.worldnewsapi.com/search-news?text=hurricane&api-key={ApiKey}"
headers = {
  'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
print("News: ", response.json())