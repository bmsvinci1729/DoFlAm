
# app.py
from flask import Flask, request, jsonify
import logging
from model import get_prediction
import awsgi

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# @app.route('/', methods = ['GET'])
# def hello():
#     return "Hello World"

@app.route('/', methods=['GET'])
def upload_form():
    return '''
    <html>
        <head>
            <title>Upload an Image</title>
        </head>
        <body>
            <h2>Upload an Image for Classification</h2>
            <form method="POST" action="/predict" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*" required>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    '''


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    try:
        img_bytes = file.read()
        class_id, class_name = get_prediction(img_bytes)
        logger.info(f"Prediction made: {class_id} - {class_name}")
        return jsonify({'class_id': class_id, 'class_name': class_name})
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return jsonify({'error': str(e)}), 500

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

# if __name__ == '__main__':
#     app.run()