from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired()])
    mail = StringField('Sähköpostiosoite*', validators=[DataRequired()])
    wine = RadioField('Ruokajuomatoive', choices=(['viini', 'Viini'], ['holiton', 'Alkoholiton']), validators=[Optional()])
    specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    place_wish = StringField('Edustava taho')
    cocktail_who = StringField('Edustava taho')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn <a target = "_blank" href = "https://www.otit.fi/~jsloth/temp/tietosuojaseloste.pdf" > tietosuojaselosteen </a> mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.',
        validators=[InputRequired()])

    avec = BooleanField('Avec')
    avec_name = StringField('Avecin nimi*')
    avec_wine = RadioField('Ruokajuomatoive', choices=(['viini', 'Viini'], ['holiton', 'Alkoholiton']), validators=[Optional()])
    avec_specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    avec_consent = BooleanField(
        'Avecini hyväksyy hänen henkilötietojensa käsittelyn <a target = "_blank" href = "https://www.otit.fi/~jsloth/temp/tietosuojaseloste.pdf" > tietosuojaselosteen </a> mukaisesti.', default="checked", validators=[InputRequired()])

    submit = SubmitField('Submit')
