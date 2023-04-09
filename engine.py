import os
from utils import Utils
import tricks
import twit_scraper as ts

# setup openapi key
Utils.load_key()

out_dir = "./tmp"
queries = ['monkey', 'chicken']
tweet_count = 10
variation_count = 1

def get_tweet_buckets(n=10):
    results = {}
    for query in queries:
        query_name = query.replace(" ", "_")
        output_dir = f'{out_dir}/{query_name}'
        scraper = ts.scrape_search(query)
        results[query_name] = ts.run_scraper(scraper, output_dir, n)
    return results

def run():
    buckets = get_tweet_buckets(n=tweet_count)
    new_contents = []
    for name, bucket in buckets.items():
        for tweet in bucket:
            content = tweet['renderedContent']
            flipped = tricks.opposite(content)
            summarized = tricks.summarize(flipped)
            analogy = tricks.analogy(summarized)
            new_contents.append(analogy)
    return new_contents


def variations(url, file_id, n=variation_count):
    """Example:
    url = "https://s3.amazonaws.com/CFSV2/obituaries/photos/9995/995933/5fc571372bb52.JPG"
    file_id = "milo"
    seed, images = variations(url, file_id, n=5)
    """
    file_dir = f"{out_dir}/{file_id}"
    os.makedirs(file_dir, exist_ok=True)

    images = []
    seed = Utils.download_image(url)
    seed = Utils.crop_image(seed)
    seed.save(f"{file_dir}/orig.png")

    res = Utils.create_variation(seed, n=n)
    for i, d in enumerate(res.data):
        img = Utils.download_image(d.url)
        img.save(f"{file_dir}/{i}.png")
        images.append(img)

    return seed, images
    