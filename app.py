from flask import Flask
from flask import render_template
from flask import request
from tempfile import NamedTemporaryFile
from flask import send_file
from shipping_label import crop_pdf
from io import BytesIO
import uuid

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crop_pdf', methods=['POST'])
def handle():
    image = crop_pdf(request.form['url'])
    temp = BytesIO()
    image.save(temp, format="JPEG")
    temp.seek(0)
    return send_file(temp, mimetype='image/jpeg', as_attachment=True, attachment_filename=f"{uuid.uuid4().hex[:8]}.jpg")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
