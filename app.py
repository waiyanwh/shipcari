from flask import Flask
from flask import render_template
from flask import request
from tempfile import mkstemp
from flask import send_file
import logging
import requests
from pdf_crop.pdf_to_jpg import convert_to_jpg, crop_image


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/crop_pdf', methods=['POST'])
def handle():
    url = request.form['url']
    assert "mercariapp" in url
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    r = requests.get(url, headers=headers, allow_redirects=True)

    if r.status_code != 200:
        logging.fatal(msg=r.json()['message'])

    # Create temporary file
    handle, filepath = mkstemp(prefix="temp")

    # Write PDF file to temp file
    open(f"{handle}.pdf", "wb").write(r.content)
    convert_to_jpg(handle)
    crop_image(handle)


    return send_file(f"{handle}.jpg", mimetype='image/jpeg', as_attachment=True, attachment_filename=f"{handle}.jpg")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)
