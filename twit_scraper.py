from os import mkdir
import os
from snscrape.modules import twitter
import json
import requests


"""Example:
queries = ['fat frogs']
for query in queries:
    output_dir = f'./tmp/{query.replace(" ", "_")}'
    scraper = scrape_search(query)
    run_scraper(scraper, output_dir)
"""

def download_photos(tweet, folder="./tmp"):
	files = []
	if tweet.media:
		for i, medium in enumerate(tweet.media):
			if isinstance(medium, twitter.Photo):
				r = requests.get(medium.fullUrl)
				file_name = f'{folder}/{tweet.id}.{i}.jpg'
				with open(file_name, 'wb') as fp:
					fp.write(r.content)
					files.append(file_name)
	return files


# Scrapes Twitter search
# Input: Twitter search (string)
# Example query: "covid"
def scrape_search(query):
	scraper = twitter.TwitterSearchScraper(query)
	return scraper

#-- Other scrapers that can be implemented

#Scrapes a single tweet
# Intput: Tweet ID (integer)
# Example tweet_id: 1516359017374887940
def scrape_tweet(tweet_id):
	scraper = twitter.TwitterTweetScraper(tweet_id)
	return scraper

# Input:
# Takes a username string or userid number
# Example: user as UserName: "Proxyway1"
# Example: user as UserID: 1097450610864123904
def scrape_user(user):
	scraper = twitter.TwitterUserScraper(user)
	return scraper

# Input: Twitter hashtag (string) (without '#')
# Example hashtag: "scraping"
def scrape_hashtag(hashtag):
	scraper = twitter.TwitterHashtagScraper(hashtag)
	return scraper

def run_scraper(scraper, output_dir, max_results=100):
	os.makedirs(output_dir, exist_ok=True)
	output_filename = f'./{output_dir}/tweets.txt'
	with open(output_filename, 'w') as f:
		i = 0
		for i, tweet in enumerate(scraper.get_items(), start = 1):

			# download images
			photos_dir = output_dir + "/photos"
			os.makedirs(photos_dir, exist_ok=True)
			image_files = download_photos(tweet, photos_dir)
		
			# Converting the scraped tweet into a json object
			tweet_json = json.loads(tweet.json())
			tweet_json['image_files'] = image_files

			#Printing out the content of a tweet
			print (f"\nScraped tweet: {tweet_json['content']}")
			#Writing to file
			f.write(json.dumps(tweet_json))
			f.write('\n')
			f.flush()
			#Terminate the loop if we reach max_results
			if max_results and i > max_results:
				break