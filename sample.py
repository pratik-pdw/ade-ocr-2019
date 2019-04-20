import os
import cv2
import io
import numpy as np
import json
from bson import json_util
from werkzeug import secure_filename
from flask import Flask, jsonify, request, flash, redirect
from flask_cors import CORS
from google.cloud import vision
from google.cloud.vision import types
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"

mydb = myclient["mydatabase"]
mycol = mydb["coordinates"]
saveCol = mydb["finalData"]

UPLOAD_FOLDER = "E:\\ade-ocr-2019\\flask-api\\uploads" 
#Set this to your preferred directory
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       some_json = request.get_json() #get the data
       print(type(some_json[0]))
       res = []
       for i in range(len(some_json)):
           temp = json.dumps(some_json[i])
           loaded_temp = json.loads(temp)
           res.append(loaded_temp)
       print(res)
       add_coordinates(res)
       return jsonify(some_json)
    else:
       docs_list  = list(mycol.find())
       img = cv2.imread("./uploads/Form.jpg")

       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       kernel = np.ones((1, 10), np.uint8)
       morphed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
       imgwtl = cv2.add(gray, (255-morphed))

       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       kernel = np.ones((40, 1), np.uint8)
       morphed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
       imgwt2 = cv2.add(gray, (255-morphed))

       result = cv2.add(imgwtl, imgwt2)


       kernel = np.ones((1, 1), np.uint8)
       img_erosion = cv2.erode(result, kernel, iterations=1) 
       img_dilation = cv2.dilate(result, kernel, iterations=1) 
       th = cv2.adaptiveThreshold(img_erosion, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) 
       client = vision.ImageAnnotatorClient()
       res = {}
       for i in docs_list:
            cropped_image = th[i['dimensions']['y']: i['dimensions']['y'] + i['dimensions']['height'], i['dimensions']['x']: i['dimensions']['x'] + i['dimensions']['width']]
            scale_percent = 220 # percent of original size
            width = int(cropped_image.shape[1] * scale_percent / 100)
            height = int(cropped_image.shape[0] * scale_percent / 100)
            dim = (width, height) 
            resized = cv2.resize(cropped_image, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(f'{i["fieldName"]}.jpg', resized)

            file_name = f'{i["fieldName"]}.jpg'
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = vision.types.Image(content=content)

            response = client.text_detection(image=image)
            texts = response.text_annotations
            res[i["fieldName"]] = texts[0].description
            # res[f'fieldName{i}'] = i["fieldName"] 
            # res[f'value{i}'] = texts[0].description

       #print(res)
       return json.dumps(res, default=json_util.default)  


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        filename = 'Form.jpg'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Saved to file"
       
@app.route('/save', methods=['POST'])
def save():
    some_json = request.get_json() #get the data
    print(type(some_json[0]))
    res = []
    for i in range(len(some_json)):
        temp = json.dumps(some_json[i])
        loaded_temp = json.loads(temp)
        res.append(loaded_temp)
    print(res)
    saveCol.insert_many(res)
    return jsonify(some_json)


def add_coordinates(data):
    mycol.insert_many(data)
