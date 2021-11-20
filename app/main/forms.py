from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Quiz or Answer', validators=[DataRequired()])
    owners = TextAreaField('Owners/Members', validators=[DataRequired()])
    technologies = TextAreaField('Technologies used', validators=[DataRequired()])
    language = SelectField('Select language', choices=[('html', 'HTML'),('css', 'CSS'),('bootstrap', 'BOOTSTRAP'),('javascript', 'JAVASCRIPT'),('jquery', 'JQUERY'),('angular', 'ANGULAR'),('python-flask', 'PYTHON-FLASK'),('python-django', 'PYTHON-DJANGO'),('java-spark', 'JAVA-SPARK'),('android', 'ANDROID'),('c', 'C'),('c++', 'C++'),('others', 'OTHERS')])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')