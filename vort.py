# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:48:49 2019

@author: razakamanana
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:36:33 2019

@author: razakamanana
"""

from flask import Flask, render_template
from flask_wtf import Form
from wtforms import DateField
from datetime import date, datetime
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'SHH!'

class DateForm(Form):
    dt = DateField(id="datetimepicker", default= datetime.utcnow)
    
def nr_get_value(input):
    soup = BeautifulSoup(input, 'html.parser')
    return soup.find(id="datetimepicker")['value']

@app.route('/', methods=['post','get'])
def home():
    form = DateForm()
    if form.validate_on_submit():
        datetime = nr_get_value(str(form.dt))
        return form.dt.data
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)