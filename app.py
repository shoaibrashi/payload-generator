from flask import Flask, render_template, request
from modules import xss, sqli, cmdi
from utils.encoders import encode_payload

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    payloads = []
    if request.method == 'POST':
        module = request.form.get('module')
        encoding = request.form.get('encoding')

        if module == 'xss':
            payloads = xss.get_xss_payloads()
        elif module == 'sqli':
            payloads = sqli.get_sqli_payloads()
        elif module == 'cmdi':
            payloads = cmdi.get_cmdi_payloads()

        if encoding:
            payloads = [encode_payload(p, encoding) for p in payloads]

    return render_template('index.html', payloads=payloads)

if __name__ == '__main__':
    app.run(debug=True)
