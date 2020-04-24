from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():

    form = Form()

    starttime = datetime(2020, 1, 27, 12, 00, 00)
    endtime = datetime(2020, 6, 1, 23, 59, 00)
    nowtime = datetime.now()

    snapsilimit = 100

    entrys = Model.query.all()
    count = Model.query.count()
    myentrys = []
    maxlimit = 200

    for entry in entrys:
        if entry.avec:
            count = count + 1
            if entry.show_name:
                myentrys.append({"name": entry.name, "avec": True})
            else:
                myentrys.append({"name": "Ano nyymi", "avec": True})
            if entry.avec_name:
                myentrys.append({"name": entry.avec_name, "avec": False})
            else:
                myentrys.append({"name": "Ano nyymi", "avec": False})

        else:
            if entry.show_name:
                myentrys.append({"name": entry.name, "avec": False})
            else:
                myentrys.append({"name": "Ano nyymi", "avec": False})

    if form.validate_on_submit() and count <= (snapsilimit - 1):
        flash('Kiitos ilmoittautumisesta! Lähetit tiedot:')
        msg = ["Nimi:  ", form.name.data,
               "Sähköposti:  ",  form.mail.data,
               "Ruokajuoma:  ", form.wine.data,
               "Eritysruokavalio:  ", form.specialneeds.data,
               "Edustava taho:  ", form.cocktail_who.data,
               "Plaseeraustoive:  ", form.place_wish.data,
               "Näytä nimi:  ", form.show_name.data]

        i = 0
        max = len(msg)
        for i in range(0, len(msg), 2):
            printtext = msg[i] + str(msg[i + 1])
            flash(printtext)

        i = 0
        if (form.avec.data == True):
            flash("Avecin tiedot:")
            avecmsg = ["Avecin nimi: ", form.avec_name.data,
                       "Ruokajuoma: ", form.avec_wine.data,
                       "Eritysruokavalio: ", form.avec_specialneeds.data,
                       "Näytä avecin nimi: ", form.avec_show_name.data]
            for i in range(0, len(avecmsg), 2):
                printavec = avecmsg[i] + str(avecmsg[i + 1])
                flash(printavec)

        sub = Model(
            name=form.name.data,
            mail = form.mail.data,
            wine = form.wine.data,
            specialneeds = form.specialneeds.data,
            place_wish = form.place_wish.data,
            cocktail_who = form.cocktail_who.data,
            show_name = form.show_name.data,
            avec = form.avec.data,
            avec_name = form.avec_name.data,
            avec_wine = form.avec_wine.data,
            avec_specialneeds = form.avec_specialneeds.data,
            avec_show_name = form.avec_show_name.data,
            datetime = nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect("https://www.otit.fi/snapsi16v/")

    elif form.is_submitted() and count > snapsilimit:
        flash('Ilmoittautuminen täynnä!')

    return render_template('index.html',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           entries = myentrys,
                           snapsilimit=snapsilimit,
                           counter=count,
                           form=form
                           )
