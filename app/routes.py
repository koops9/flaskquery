from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import HumuForm, KMPForm, OKSForm
from .models import Humu, KMP, OKS
from datetime import datetime

@app.route('/KMP', methods=['GET', 'POST'])
def kmpilmo():
    form = KMPForm()

    starttime = datetime(2018, 2, 23, 12, 00, 00)
    endtime = datetime(2018, 3, 7, 12, 00, 00)
    nowtime = datetime.now()

    limit = 45
    maxlimit = 200

    partisipants = KMP.query.all()
    count =KMP.query.count()
    otit = KMP.query.filter_by(representative='OTiT').all()
    sik = KMP.query.filter_by(representative='SIK').all()
    
    guilds = [
        {'name': 'OTiT',
         'quota': 22,
         'submissions': otit},
        {'name': 'SIK',
         'quota': 23,
         'submissions': sik},
    ]
    
    

    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoittautumisestasi')
        sub = KMP(
            name=form.name.data,
            email=form.email.data,
            representative=form.representative.data,
            place=form.place.data
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('kmpilmo')) #this is the fucktion name
    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen on täynnä')
    return render_template('KMP.html', 
                        title='KMP 2018 ilmoittautuminen',
                        partisipants=partisipants, 
                        count=count, 
                        starttime=starttime, 
                        endtime=endtime, 
                        nowtime=nowtime, 
                        limit=limit,
                        guilds=guilds,
                        otit=otit,
                        sik=sik,
                        form=form)

@app.route('/humusitsit', methods=['GET', 'POST'])
def humusitsit():
    form = HumuForm()

    starttime = datetime(2018, 1, 19, 12, 00, 00)
    endtime = datetime(2018, 3, 17, 23, 59, 00)
    nowtime = datetime.now()

    limit = 99
    maxlimit = 200

    partisipants = Humu.query.all()
    count = Humu.query.count()

    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoitautumisestasi')
        sub = Humu(
            name=form.name.data,
            email=form.email.data,
            representative=form.representative.data,
            food=form.food.data,
            alcohol=form.alcohol.data,
            drink=form.drink.data,
            wine=form.wine.data
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('/humusitsit'))
    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen on täynnä')
    return render_template('ilmo.html', title='Humanöörisitsit 2018 ilmoittautuminen', partisipants=partisipants, count=count, starttime=starttime, endtime=endtime, nowtime=nowtime, limit=limit, form=form)

    
@app.route('/oks-ilmo', methods=['GET', 'POST'])
def oksilmo():
    form = OKSForm()

    starttime = datetime(2018, 1, 19, 12, 00, 00)
    endtime = datetime(2018, 3, 15, 23, 59, 00)
    nowtime = datetime.now()

    limit = 80
    maxlimit = 200

    partisipants = OKS.query.all()
    count = OKS.query.count()
    otit = OKS.query.filter_by(representative='OTiT').all()
    sik = OKS.query.filter_by(representative='SIK').all()
    blanko = OKS.query.filter_by(representative='Blanko').all()
    hnk = OKS.query.filter_by(representative='Henkilökunta').all()

    guilds = [
        {'name': 'OTiT',
         'quota': 20,
         'submissions': otit},
        {'name': 'SIK',
         'quota': 20,
         'submissions': sik},
        {'name': 'Blanko',
         'quota': 20,
         'submissions': blanko},
        {'name': 'Henkilökunta',
         'quota': 20,
         'submissions': hnk}]
    
    
    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoittautumisestasi')
        sub = OKS(
            name=form.name.data,
            email=form.email.data,
            representative=form.representative.data,
            table=form.table.data,
            discussion = form.discussion.data,
            food=form.food.data,
            alcohol=form.alcohol.data,
            drink=form.drink.data,
            wine=form.wine.data
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('oksilmo'))
    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen on täynnä')
    return render_template('oks-ilmo.html', 
                            title='Opetuksenkehittämisseminaari 2018 ilmoittautuminen', 
                            partisipants=partisipants, 
                            count=count, 
                            starttime=starttime, 
                            endtime=endtime, 
                            nowtime=nowtime, 
                            limit=limit,
                            otit=otit,
                            sik=sik,
                            blanko=blanko,
                            hnk=hnk,
                            guilds=guilds,
                            form=form)
