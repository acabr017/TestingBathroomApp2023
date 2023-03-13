import requests
from PIL import Image
from io import BytesIO

url = "http://10.0.0.97:8080"

response = requests.get(url)

image_data = BytesIO(response.content)

image = Image.open(image_data)

image.show()