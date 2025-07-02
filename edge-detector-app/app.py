from flask import Flask, render_template, request, send_file
import cv2
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output_generated = False
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = 'static/input.jpg'
            file.save(filepath)

            # Process image
            img = cv2.imread(filepath)
            edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
            cv2.imwrite('static/edgedetected.png', edges)
            output_generated = True

    return render_template('index.html', output=output_generated)

@app.route('/download')
def download():
    return send_file('static/edgedetected.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
