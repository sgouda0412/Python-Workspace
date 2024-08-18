import pyqrcode
import png
from pyqrcode import QRCode

QRcreate = "https://www.instagram.com/__beginnerscode__/"

url = pyqrcode.create(QRcreate)
url.png('Desktop/qr.png', scale=8)
