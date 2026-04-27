import qrcode


data = "www.vg.no"
img = qrcode.make(data)
img.save("qr-code.png")
print("Da er den klar!")
