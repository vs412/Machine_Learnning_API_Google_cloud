import io
from google.cloud import vision

vision_client = vision.Client()
file_name = '375px-Guido_van_Rossum_OSCON_2006_cropped.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

labels = image.detect_labels()
for label in labels:
    print(label.description, label.score)
