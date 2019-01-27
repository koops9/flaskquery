from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2018, 1, 19, 12, 00, 00)
    endtime = datetime(3018, 2, 2, 23, 59, 00)
    nowtime = datetime.now()

    otitlimit = 36
    communicalimit = 36

    entrys = Model.query.all()
    count = Model.query.count()


    otits = []
    communicas = []
    otitcount = 0
    communicacount = 0

    maxlimit = 500

    entries = len(entrys)
    for entry in entrys:
        if entry["guild"] == "otit":
            otits.append(entry)
            otitcount += 1
            if entry["avec"]:
                otitcount += 1
        elif entry["guild"] == "communica":
            communicas.append(entry)
            communicacount += 1
            if entry["avec"]:
                communicacount += 1


    if form.validate_on_submit() and count <= maxlimit:
        flash('Thank you for participating')
        sub = Model(
            name=form.string.data,
            mail = form.string.data,
            guild = form.string.data,
            alcohol = form.string.data,
            wine = form.string.data,
            beer = form.string.data,
            specialneeds = form.text.data,
            avec = form.boolean.data,
            avec_name = form.string.data,
            avec_alcohol = form.string.data,
            avec_wine = form.string.data,
            avec_beer = form.string.data,
            avec_specialneeds = form.text.data,
            datetime = nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('index'))

    elif form.is_submitted() and count > maxlimit:
        flash('Query is already full')

    return render_template('index.html',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           otitlimit=otitlimit,
                           otits=otits,
                           otitcount=otitcount,
                           communicalimit=communicalimit,
                           communicas=communicas,
                           communicacount=communicacount,
                           form=form,
                           entries=entries)
