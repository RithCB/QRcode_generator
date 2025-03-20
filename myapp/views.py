import qrcode
from django.shortcuts import render
import base64
from io import BytesIO

def hello(request):
    qr_base64 = None

    if request.method == "POST":
        website_link = request.POST.get("text_input", "").strip()

        if website_link:  # Generate QR code only if input is provided
            qr = qrcode.QRCode(version=1, box_size=5, border=5)
            qr.add_data(website_link)
            qr.make()
            img = qr.make_image(fill_color="black", back_color="white")
            
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    context = {"qr_base64": qr_base64}
    return render(request, "index.html", context)
