# gpt-wrappers 

## Instructions

1. create an api key from: https://platform.openai.com/account/api-keys
2. save the api key in a file call key.txt
3. open tester.ipynb and try it out



**Plan 1**:
```plantuml
!include docs/plan1.puml
```

## Quickstart
#### Engine Example:

```python
# see impl for how to
import engine
tweets = engine.run()
```

### Twitter Examples
Anonymously scrape twitter with critera and storing all the text and images

#### Scrape with queries
```python
import twit_scraper as ts

queries = ['edgelord', 'overwatch', 'toxic gamers']
for query in queries:
    output_dir = f'./tmp/{query.replace(" ", "_")}'
    scraper = ts.scrape_search(query)
    ts.run_scraper(scraper, output_dir)
```


#### Scrape a user's tweets
```python
import twit_scraper as ts

user = "ChomskyDotInfo"
output_dir = f'./tmp/{user}'
scraper = ts.scrape_user(user)
ts.run_scraper(scraper, output_dir)
```

### GPT Examples

#### Quickstart GPT Tricks

```python
import tricks

content = """
Buzz Aldrin left a pen on the moon after the first visit. 
Eugene Cernan, the last moon walker, found it. It still worked.
"""

# chaining opposite+summarized+analogy
flipped = tricks.opposite(content)
summarized = tricks.summarize(flipped)
analogy = tricks.analogy(summarized)
```

#### Generate variation images from an image online
```python
import engine
url = "https://s3.amazonaws.com/CFSV2/obituaries/photos/9995/995933/5fc571372bb52.JPG"
file_id = "milo"
seed, images = engine.variations(url, file_id)
```