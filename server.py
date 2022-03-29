# from flask import Flask,render_template
from lib2to3.pgen2.token import NEWLINE
from pickle import TRUE
from flask import Flask,render_template,request
import csv

app = Flask(__name__)
# print(__name__)

@app.route('/')
def my_index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_index2(page_name):
    return render_template(page_name)

def wrtie_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def wrtie_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route('/submit_forms',methods=["POST","GET"])
def submit_form():
    strs= (request.form)
    wrtie_to_csv(strs.to_dict()) 
    if strs == "POST":
        wrtie_to_file(strs) 
        # return strs
    else:
        return "like"
    
    # if request.method == "POST":
        # data = request.form
        # data = data.to_dict()
        # print('data')
    # else:
        # return'sdsds'

