from flask import Flask , render_template , request
import qrcode
from io import BytesIO
from base64 import b64encode

app= Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def QR_generator():
    data= request.form.get("link")
    img= qrcode.make(data)

    memory= BytesIO()
    img.save(memory)
    memory.seek(0)

    base64_image= "data:image/png;base64," + b64encode(memory.getvalue()).decode("ascii")
    return render_template('index.html', data= base64_image)
if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000, debug= True)