from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional,Email

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired()])
    mail = StringField('Sähköpostiosoite*', validators=[DataRequired(), Email(message="Sähköposti ei ole oikeaa muotoa")])
    wine = RadioField('Ruokajuomatoive', choices=(['viini', 'Viini'], ['holiton', 'Alkoholiton']), validators=[Optional()], default="viini")
    specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    place_wish = StringField('Plaseeraustoive')
    cocktail_who = StringField('Edustava taho (jos osallistut cocktail-tilaisuuteen)')
    show_name = BooleanField('Nimeni saa näyttää ilmoittautuneiden listassa')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn <a target = "_blank" href = "https://www.otit.fi/~jsloth/temp/tietosuojaseloste.pdf" > tietosuojaselosteen </a> mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.',
        validators=[InputRequired()])

    avec = BooleanField('Avec')
    avec_name = StringField('Avecin nimi*')
    avec_wine = RadioField('Ruokajuomatoive', choices=(['viini', 'Viini'], ['holiton', 'Alkoholiton']), validators=[Optional()])
    avec_specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    avec_show_name = BooleanField('Aveccini nimen saa näyttää ilmoittautuneiden listassa')
    avec_consent = BooleanField(
        'Avecini hyväksyy hänen henkilötietojensa käsittelyn <a target = "_blank" href = "https://www.otit.fi/~jsloth/temp/tietosuojaseloste.pdf" > tietosuojaselosteen </a> mukaisesti.', default="checked", validators=[InputRequired()])

    submit = SubmitField('Lähetä')
