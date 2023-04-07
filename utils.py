import openai
from io import BytesIO
from PIL import Image
from PIL import Image
import requests
import io

# defaults
key_file = 'key.txt'


class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def load_key(key_file=key_file):
        with open(key_file, 'r') as f:
            key = f.read()
            openai.api_key = key

    @staticmethod
    def crop_image(image):
        w, h = image.size
        d = h if h < w else w
        width, height = d, d
        image = image.resize((width, height))
        return image
    
    @staticmethod
    def download_image(url):
        res = requests.get(url, stream = True)
        if res.status_code == 200:
            img = Image.open(io.BytesIO(res.content))
            return img
        else:
            print('Image Couldn\'t be retrieved')


    @staticmethod
    def create_variation(image):
        byte_stream = io.BytesIO()
        image.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()
        response = openai.Image.create_variation(
            image=byte_array,
            n=1,
            size="1024x1024"
        )
        return response