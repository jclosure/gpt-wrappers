import os
from utils import Utils
import tricks
import twit_scraper as ts
from PIL import Image

# setup openapi key
Utils.load_key()

out_dir = "./tmp"

tweet_count = 10
variation_count = 2

def search_twitter(queries, n=tweet_count):
    results = {}
    for query in queries:
        query_name = query.replace(" ", "_")
        output_dir = f'{out_dir}/{query_name}'
        scraper = ts.scrape_search(query)
        results[query_name] = ts.run_scraper(scraper, output_dir, n)
    return results

# demo fn
def run(queries, n=tweet_count):
    tweets = execute_queries(queries, n=n)
    for tweet in tweets:
        image_files = tweet['image_files']
        for path in image_files:
            seed, images = variations(path, tweet['name'], n=1)
            for img in [seed] + images:
                img.show()
    return tweets

def execute_queries(queries, n=tweet_count):
    buckets = search_twitter(queries, n=n)
    new_tweets = []
    for name, bucket in buckets.items():
        for tweet in bucket:
            content = tweet['renderedContent']
            flipped = tricks.opposite(content)
            summarized = tricks.summarize(flipped)
            # analogy = tricks.analogy(summarized)

            tweet['botContent'] = summarized
            tweet['name'] = name
            new_tweets.append(tweet)
    return new_tweets


def variations(url, file_id, n=variation_count):
    """Example:
    url = "https://s3.amazonaws.com/CFSV2/obituaries/photos/9995/995933/5fc571372bb52.JPG"
    file_id = "milo"
    seed, images = variations(url, file_id, n=5)
    """
    file_dir = f"{out_dir}/{file_id}"
    os.makedirs(file_dir, exist_ok=True)

    images = []
    if url.startswith('http'):
        seed = Utils.download_image(url)
    else:
        # assume it's a local file for now
        seed = Image.open(url)

    seed = Utils.crop_image(seed)
    seed.save(f"{file_dir}/orig.png")

    res = Utils.create_variation(seed, n=n)
    for i, d in enumerate(res.data):
        img = Utils.download_image(d.url)
        img.save(f"{file_dir}/{i}.png")
        images.append(img)

    return seed, images
    