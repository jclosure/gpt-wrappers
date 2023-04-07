# gpt-wrappers 

## Instructions

1. create an api key from: https://platform.openai.com/account/api-keys
2. save the api key in a file call key.txt
3. open tester.ipynb and try it out
   
Example:
```python
from utils import Utils

Utils.load_key()

url = "https://s3.amazonaws.com/CFSV2/obituaries/photos/9995/995933/5fc571372bb52.JPG"
img = Utils.download_image(url)
img = Utils.crop_image(img)
res = Utils.create_variation(img)

url = res.data[0].url
img2 = Utils.download_image(url)
img2.show()
```
