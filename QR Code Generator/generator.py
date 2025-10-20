from flask import Flask, render_template
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    user_name = "Alice"
    return render_template('index.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True)



website_link = str(input("Enter a website link: ")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = '{fill_color}', back_color = '{back_color}')
img.save('f{name}' + '.png')

