import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageFilter
import requests
from io import BytesIO
import pytesseract as pt
import numpy as np
pt.pytesseract.tesseract_cmd = r'C:\Users\ilya_\AppData\Local\tesseract.exe'

url = [
    "https://github.com/TiffanyICIS/TextInPhotoAutocorrector/blob/b9b552fa9191f51ed6d36af6c18609c973ebca6f/Photos/1.jpg?raw=true",
    "https://github.com/TiffanyICIS/TextInPhotoAutocorrector/blob/9c21e8ec91cd0cc8d7c465da044819239347b3da/Photos/2_1.jpg?raw=true",
    "https://github.com/TiffanyICIS/TextInPhotoAutocorrector/blob/a0f0c133c26e6b61a2fc950e37d6aac9980e65fa/Photos/3_3.jpg?raw=true",
    "https://github.com/TiffanyICIS/TextInPhotoAutocorrector/blob/9d3f88a8f1e4068165b35be9874795c7489015e0/Photos/3_1.jpg?raw=true"
]

images = []
for path in url:
    response = requests.get(path)
    Img = Image.open(BytesIO(response.content))
    images.append(Img)

fig = plt.figure(figsize=(16,10))
rows = 2
columns = 2


fig.add_subplot(rows, columns, 1)
plt.imshow(images[0])
plt.axis('off')
plt.title("First Image")

fig.add_subplot(rows, columns, 2)
plt.imshow(images[1])
plt.axis('off')
plt.title("Second Image")

fig.add_subplot(rows, columns, 3)
plt.imshow(images[2])
plt.axis('off')
plt.title("Third Image")

fig.add_subplot(rows, columns, 4)
plt.imshow(images[3])
plt.axis('off')
plt.title("4th Image")

plt.show()

enh_images = []

for img in images:
    a = np.asarray(img)
    x = Image.fromarray(a)
    x = x.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(x)
    x = enhancer.enhance(2)
    #x = x.convert('1')
    enh_images.append(x)

fig = plt.figure(figsize=(16,10))
rows = 2
columns = 2

fig.add_subplot(rows, columns, 1)
plt.imshow(enh_images[0])
plt.axis('off')
plt.title("First Image")

fig.add_subplot(rows, columns, 2)
plt.imshow(enh_images[1])
plt.axis('off')
plt.title("Second Image")

fig.add_subplot(rows, columns, 3)
plt.imshow(enh_images[2])
plt.axis('off')
plt.title("Third Image")

fig.add_subplot(rows, columns, 4)
plt.imshow(enh_images[3])
plt.axis('off')
plt.title("4th Image")


plt.show()

tesseract_preds = []
for img in enh_images:
    tesseract_preds.append(pt.image_to_string(img, lang="rus"))


print(tesseract_preds[0])
plt.imshow(enh_images[0])
plt.title("First Image")

print(tesseract_preds[1])
plt.imshow(enh_images[1])
plt.title("Second Image")

print(tesseract_preds[2])
plt.imshow(enh_images[2])
plt.title("Third Image")

print(tesseract_preds[3])
plt.imshow(enh_images[3])
plt.title("4th Image")
