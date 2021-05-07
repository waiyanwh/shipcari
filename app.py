from flask import Flask
from flask import render_template
from flask import request
from flask import Response
from flask import send_file
from shipping_label import crop_pdf
import tempfile

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crop_pdf', methods=['POST'])
def handle():
    pdf_file = crop_pdf(request.form['url'])
    resp = Response(pdf_file)
    resp.headers['Content-Type'] = 'application/pdf'
    return resp

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
