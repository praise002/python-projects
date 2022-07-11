import pyqrcode

data = input("Enter the text or link to generate QR code: ")
qr = pyqrcode.create(data)   #create QR code
#to see the qr code we have to export it into a file
qr.svg('qr_code.svg', scale=9)   #using filename & scale