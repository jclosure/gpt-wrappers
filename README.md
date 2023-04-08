# gpt-wrappers 

## Instructions

1. create an api key from: https://platform.openai.com/account/api-keys
2. save the api key in a file call key.txt
3. open tester.ipynb and try it out
   
### Generate variation images of any image online
```python
import os
from utils import Utils

Utils.load_key()

url = "https://s3.amazonaws.com/CFSV2/obituaries/photos/9995/995933/5fc571372bb52.JPG"
file_id = "milo"
file_dir = f"./tmp/{file_id}"
os.makedirs(file_dir, exist_ok=True)

img = Utils.download_image(url)
img = Utils.crop_image(img)
img.save(f"{file_dir}/0.png")

for i in range(1, 10):
    res = Utils.create_variation(img)
    url = res.data[0].url
    img2 = Utils.download_image(url)
    img2.save(f"{file_dir}/{i}.png")
    img2.show()
```

## Content

### Twitter

#### Scrape a twitter search and storing all the text and images
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

output_dir = f'./tmp/{query.replace(" ", "_")}'
scraper = ts.scrape_user("mtgreenee")
ts.run_scraper(scraper, output_dir)
```