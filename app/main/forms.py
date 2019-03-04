from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required, Email, Length

class BlogForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    text = TextAreaField('Blog',validators = [Required()])
    category = SelectField('Category', choices = [('general', 'General'),('happiness','Happiness'), ('motivation','Motivation'),('success','Success')], validators = [Required()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you', validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField('Add your name', validators = [Required()])
    text = TextAreaField('Leave a Comment',validators = [Required()])
    submit = SubmitField('Add Comment')

class SubscriberForm(FlaskForm):
    name  = StringField('Your name', validators = [Required()])
    email = StringField('Your email address', validators = [Required(), Email()])
    submit = SubmitField('Subscribe')

