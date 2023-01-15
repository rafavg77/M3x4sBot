import feedparser
import requests
from bs4 import BeautifulSoup

class GetNews:

    def thehackernews(self):
        url = 'https://thehackernews.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        tags = soup.findAll('a',{"class": "story-link"})
        
        urls = []
        for tag in tags[:3]:
            if url in tag.get("href"):
                urls.append({"url" : tag.get("href")})
        
        return(urls)


    def threatpost(selft):
        NewsFeed = feedparser.parse("https://threatpost.com/feed/")
        
        urls = []
        for entry in NewsFeed.entries[:3]:
            urls.append({"url" : entry.link})

        return(urls)

    def SANSInternetStormCenter(self):
        NewsFeed = feedparser.parse("https://isc.sans.edu/rssfeed_full.xml")
 
        urls = []
        for entry in NewsFeed.entries[:3]:
            urls.append({"url" : entry.link})
            
        return(urls)

    def getAll(self):
        hackerNews = self.thehackernews()
        threatpost = self.threatpost()
        sansInternetStormCenter = self.SANSInternetStormCenter()

        data = hackerNews.__add__(threatpost).__add__(sansInternetStormCenter)
        return(data)