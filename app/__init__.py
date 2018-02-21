from flask import Flask
from flask_mail import Mail 
app = Flask(__name__)


app.config['SECRET_KEY']= 'cram5'
app.config['MAIL_SERVER']= 'smtp.mailtrap.io' 
app.config['MAIL_PORT']= '2525' 
app.config['MAIL_USERNAME']='081cd2652998d9' 
app.config['MAIL_PASSWORD']='ab232ea8ed7960' 

mail= Mail(app) 
from app import views  

