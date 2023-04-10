from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

# Add any form classes for Flask-WTF here

class MovieForm(FlaskForm):
    title=StringField('Movie Title',validators=[InputRequired()])
    description=TextAreaField('Movie Description',validators=[InputRequired()])
    poster=FileField('Upload Poster',validators=[FileRequired, FileAllowed(['jpg', 'png'], 'Images only!')])