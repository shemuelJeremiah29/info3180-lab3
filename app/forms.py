from flask_wtf import FlaskForm 
from wtforms import StringField , validators, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm): 
    name = StringField('name', validators =[validators.Length(min=8, max=25),DataRequired()]) 
    email = StringField ('email', validators=[validators.Length(min=8, max=35), DataRequired()]) 
    address=StringField('address', validators=[validators.Length(min=12, max=255),DataRequired()]) 
    subject=StringField('subject', validators=[validators.Length(min=12, max=80),DataRequired()]) 
    textarea=StringField('textarea', validators=[validators.Length(min=1, max=5000), DataRequired()]) 
    submit = SubmitField('Send') 
    