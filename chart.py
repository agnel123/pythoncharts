from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
# import urllib3


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

def getExchangeRates():
    rates = []
    # response = urllib3.urlopen('http://api.fixer.io/latest')
    # data = response.read()
    # rdata = json.loads(data, parse_float=float)
    with open('chartdata.json') as json_data:
        rdata = json.load(json_data)
 
    rates.append( rdata['rates'][0]['USD'] )
    rates.append( rdata['rates'][0]['GBP'] )
    rates.append( rdata['rates'][0]['JPY'] )
    rates.append( rdata['rates'][0]['AUD'] )
    return rates
 

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chart")
def index():
    rates = getExchangeRates()
    return render_template('chart.html',**locals())     
    # return "chart!"
 
if __name__ == "__main__":
    app.run()
