from app import app
from flask import request
from temp import calc
import numpy as np
import cv2


@app.route("/area", methods=["POST"])
def area():
    file = request.files["image"].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    return calc(img)
