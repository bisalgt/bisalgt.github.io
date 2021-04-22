from flask import Flask, render_template, url_for, request, redirect
import logging
import os

app = Flask(__name__)
app.config['FREEZER_BASE_URL'] = 'http://localhost/build'

logging.basicConfig(filename='flaskr.log', encoding='utf-8', level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def home():
    print(url_for('home'))
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone_number=request.form['phone']
        message=request.form['message']
        msg = f'###{name } -- { message} -- {phone_number} -- {email}###'
        logging.warning(msg)
        return redirect(url_for('home'))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)