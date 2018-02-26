from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Required

class RegForm(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Email()])
    representative = StringField('Edustava taho/joukkue', validators=[DataRequired()])
    greeting = BooleanField('Haluatko tuoda tervehdyksen?')
    food = StringField('Erityisruokavalio')
    alcohol = RadioField('Holiton / Holillinen', choices=(['Holillinen', 'Holillinen (20e)'],['Holiton', 'Holiton (20e)']), validators=[Required()])
    gambina = BooleanField('Iso G (+9,83 € hintaan)')
    avec = StringField('Avec / Pöytätoive (avec ilmoittautuu erikseen)')
    free = TextAreaField('Vapaa sana')
    submit = SubmitField('Ilmoittaudu')

class HumuForm(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Email()])
    food = StringField('Erityisruokavalio, (esimerkiksi "kasvis" tai "ei herneitä")')
    alcohol = RadioField('Holiton / Holillinen', choices=(['Holillinen', 'Holillinen (20e)'],['Holiton', 'Holiton (18e)']), validators=[Required()])
    drink = RadioField('Mieto juoma', 
                                    choices=(['Kalja', 'Kalja'],
                                             ['Siideri', 'Siideri']))
    wine = RadioField('Viini',
                                    choices=(['Valkoviini', 'Valkoviini'],
                                             ['Punaviini', 'Punaviini']))
    representative = SelectField('Kilta', 
                                    choices=[('OTiT', 'OTiT'), 
                                             ('YMP', 'YMP'), 
                                             ('Communica', 'Comunica')])
    free = TextAreaField('Vapaa sana')
    submit = SubmitField('Ilmoittaudu')

class KMPForm(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Email()])
    representative = SelectField('Kilta', 
                                choices=[('OTiT', 'OTiT'), 
                                ('SIK', 'SIK'), 
                                ('Tärkeä_henkilö', 'kulttuuriministeri/excursiomestari/tai muu etuoikeutettu')])
    place = SelectField('Mistä nouset kyytiin?', 
                        choices=[('Linnanmaa','Linnanmaa'), 
                                ('Tuira','Tuira'),
                                ('Keskusta','Linja-autoasema')])
    submit = SubmitField('Ilmoittaudu')