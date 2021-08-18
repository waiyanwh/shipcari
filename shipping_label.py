import urllib
import tempfile
from pdf2image import convert_from_bytes
from PIL import ImageOps
import requests


def crop_pdf(url):
    # req = urllib.request
    # response = urllib.request.urlopen(url, headers=head)
    
    payload={}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cookie': '_mwus=eyJhY2Nlc3NUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUppSWpvaVpURm1NMkk1WmpVNU56VmlOak01T0RRMU0yTTFZekE1WldFd09XRXpNaklpTENKa1lYUmhJanA3SW5WMWFXUWlPaUpuYURwM09qUmlORGhrT0RCakxUbG1NRGN0TkRjeVlpMDVOell5TFdVNE9UTTNZV1ZqWm1ZeFlTSXNJbUZqWTJWemMxUnZhMlZ1SWpvaVdscElXV2RHWjBSUmFtcEFNM0EwVEZkb1FGRldUV0V5WmlGWk9FMDJVRmc0TGxwcWFuWlFVR00zYlV4cVVFNUdURjlYUzNOb0luMHNJbVY0Y0NJNk1UWXlPVGcyTURBNE9Dd2lhV0YwSWpveE5qSTVNalUxTWpnNGZRLnV3VTNLLUJMc3hCS1V1WnhzU284Rml4cnN1UHV5Z0N3S3h5eEZYWVVidU0iLCJyZWZyZXNoVG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaUlqb2laVEZtTTJJNVpqVTVOelZpTmpNNU9EUTFNMk0xWXpBNVpXRXdPV0V6TWpJaUxDSmtZWFJoSWpwN0luVjFhV1FpT2lKbmFEcDNPalJpTkRoa09EQmpMVGxtTURjdE5EY3lZaTA1TnpZeUxXVTRPVE0zWVdWalptWXhZU0o5TENKcFlYUWlPakUyTWpreU5UVXlPRGg5LkNYei1mRDZJRXVlSlR3ZXY2TnNCMWVTbE1zbVNzYXRoWHdFWHlVLUk2Q0kiLCJvcHRpbWl6ZUV4cGVyaW1lbnRzIjpbeyJ2YXJpYW50IjoxLCJleHBlcmltZW50IjoiUUZzcWZxTVJULVNvN2pDYXhYd2tFZyIsIm5hbWUiOiJnZXRfdGhlX2FwcF9hZ2FpbnN0X3NlbGxfbm93IiwiZXhwaXJlZERhdGUiOjE2MzcwMzEyODh9LHsidmFyaWFudCI6MCwiZXhwZXJpbWVudCI6IkFxNWhDSlVHU2tLdDNId2JuYlpQRFEiLCJuYW1lIjoiZnJlZV9zaGlwcGluZ190aHVtYiIsImV4cGlyZWREYXRlIjoxNjM3MDMxMjg4fSx7InZhcmlhbnQiOjAsImV4cGVyaW1lbnQiOiJyRHdNRV9fZVEwLWp5SjA3cUJaVkV3IiwibmFtZSI6InBheXBhbF9jcmVkaXQiLCJleHBpcmVkRGF0ZSI6MTYzNzAzMTI4OH0seyJ2YXJpYW50IjozLCJleHBlcmltZW50IjoidXBrMG1DVkJRek92MWlyTEdBSnNtQSIsIm5hbWUiOiJ3ZWItdG8tYXBwLTIwMjEiLCJleHBpcmVkRGF0ZSI6MTYzNzAzMTI4OH0seyJ2YXJpYW50IjoxLCJleHBlcmltZW50IjoiMHdvcWpLaU1RQTY2ZFU5dzNIVlhLUSIsIm5hbWUiOiJyZWZlcnJhbC1jdGEtdGVzdCIsImV4cGlyZWREYXRlIjoxNjM3MDMxMjg4fSx7InZhcmlhbnQiOjIsImV4cGVyaW1lbnQiOiIzcTdjcGtCRVQ3YUZmX2cweE45S2p3IiwibmFtZSI6Imluc2lnaHQtYmFzZWQtcG9wdWxhci1zZWFyY2giLCJleHBpcmVkRGF0ZSI6MTYzNzAzMTI4OH0seyJ2YXJpYW50IjoxLCJleHBlcmltZW50IjoiajN1ZmZydTBUbC1icGVaZU5vTDl1QSIsIm5hbWUiOiJ3ZWItbmV3LXB1YmxpYy1wYWdlIiwiZXhwaXJlZERhdGUiOjE2MzcwMzEyODh9XSwiY3NyZlNlY3JldCI6Ijh4UmZraDZ5b1Z4dnppSmVxT0Eza0JNcyJ9; _mwus.sig=pSCETjjXShs6wk0ueB8a5h6GAOE; merCtx=2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    original_pdf = response.text
    border = (170,120,170,1215)
    temp = tempfile.TemporaryFile()
    temp.write(bytes(original_pdf,'utf8'))
    temp.seek(0)
    images = convert_from_bytes(bytes(original_pdf,'utf8'))
    cropped_img = ImageOps.crop(images[0], border).rotate(270, expand=True)
    return cropped_img