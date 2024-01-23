from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(u'Coffee Rating',
                                choices=[('☕', '☕'),
                                         ('☕☕', '☕☕'),
                                         ('☕☕☕', '☕☕☕'),
                                         ('☕☕☕☕', '☕☕☕☕'),
                                         ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_rating = SelectField(u'Wifi Strength Rating',
                              choices=[('❌', '❌'),
                                       ('💪💪', '💪💪'),
                                       ('💪💪💪', '💪💪💪'),
                                       ('💪💪💪💪', '💪💪💪💪'),
                                       ('💪💪💪💪💪', '💪💪💪💪💪')])

    power_availability = SelectField(u'Power Socket Availability',
                                     choices=[('🔌', '🔌'),
                                              ('🔌🔌', '🔌🔌'),
                                              ('🔌🔌🔌', '🔌🔌🔌'),
                                              ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                              ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')
