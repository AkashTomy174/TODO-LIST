import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_bbc():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = item.get_text().strip()
        if text and len(text) > 10:  # Filter short texts
            headlines.append(text)
    return headlines[:5] if headlines else ["No headlines found"]

def scrape_cnn():
    url = 'https://www.cnn.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = item.get_text().strip()
        if text and len(text) > 10 and 'CNN' not in text and 'feedback' not in text.lower() and 'stories' not in text.lower() and 'Middle East' not in text and 'Age Of' not in text and 'See The' not in text and 'More US' not in text and 'Climate' not in text and 'Business' not in text and 'Art' not in text and 'Celebrities' not in text and 'Health' not in text and 'Space' not in text and 'Inside' not in text:
            headlines.append(text)
    return headlines[:5] if headlines else ["No headlines found"]

def scrape_reuters():
    url = 'https://www.reuters.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = item.get_text().strip()
        if text and len(text) > 10 and 'Reuters' not in text:
            headlines.append(text)
    return headlines[:5] if headlines else ["No headlines found"]

def scrape_guardian():
    url = 'https://www.theguardian.com/international'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = item.get_text().strip()
        if text and len(text) > 10 and 'Guardian' not in text:
            headlines.append(text)
    return headlines[:5] if headlines else ["No headlines found"]

def scrape_aljazeera():
    url = 'https://www.aljazeera.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = item.get_text().strip()
        if text and len(text) > 10 and 'Al Jazeera' not in text:
            headlines.append(text)
    return headlines[:5] if headlines else ["No headlines found"]

def main():
    news = {
        'BBC': scrape_bbc(),
        'CNN': scrape_cnn(),
        'Reuters': scrape_reuters(),
        'The Guardian': scrape_guardian(),
        'Al Jazeera': scrape_aljazeera()
    }
    with open('news.json', 'w') as f:
        json.dump(news, f, indent=4)
    print("News scraped and saved to news.json")

if __name__ == '__main__':
    main()
