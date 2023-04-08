import tricks
import twit_scraper as ts

queries = ['monkey', 'chicken']

def get_tweet_buckets():
    results = {}
    for query in queries:
        query_name = query.replace(" ", "_")
        output_dir = f'./tmp/{query_name}'
        scraper = ts.scrape_search(query)
        results[query_name] = ts.run_scraper(scraper, output_dir, 10)
    return results

def run():
    buckets = get_tweet_buckets()
    new_contents = []
    for name, bucket in buckets.items():
        for tweet in bucket:
            content = tweet['renderedContent']
            flipped = tricks.opposite(content)
            summarized = tricks.summarize(flipped)
            analogy = tricks.analogy(summarized)
            new_contents.append(analogy)
    return new_contents