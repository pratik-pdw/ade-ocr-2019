import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\USER\\Downloads\\gcloudstuff\\apikey.json"

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# The name of the image file to annotat
# e
file_name = "FirstName.jpg"

# # Instantiates a client
# client = vision.ImageAnnotatorClient()


# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()

# image = types.Image(content=content)

# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations
# print('Labels:')
# for label in labels:
#     print(label.description)

client = vision.ImageAnnotatorClient()

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
# print(texts)
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))
