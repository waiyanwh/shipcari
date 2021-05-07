import requests
import re
import tempfile

url = "https://www.mercari.com/shipping/label/?id=108099172&token=1a62c62a74abc11448f791f09acf17e454a10201&sc=1302"

def crop_pdf(url):
    payload={}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    original_pdf = response.text
    new_pdf = re.sub("/Rotate 0","/Rotate 90", original_pdf)
    new_pdf = new_pdf.replace("/Contents 8 0 R /MediaBox [ 0 0 595.2756 790.8661 ] /Parent 7 0 R /Resources <<", "/Contents 8 0 R /MediaBox [ 60 435 535 750.8661 ] /Parent 7 0 R /Resources <<")

    return new_pdf