# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/')
def timeline():
    return render_template('layout.html')

@app.route('/sessions')
def sessions():
    """calculator"""
    global a
    global b
    global c
    global cal

    if a is not None and b is not None:
        if cal=='+':
            c = str(float(a) + float(b))
        elif cal == '-':
            c = str(float(a) - float(b))
        else:
            cal = None
    return render_template('sessions.html', num=a ,num2=b, num3=c, cal=cal)

@app.route('/calculate2',methods=['POST'])
def calculate2():
    global a
    global b
    global cal

    if 'plus' in request.form:
        cal = '+'
    elif 'minus' in request.form:
        cal = '-'
    else:
        cal = None

    if request.method == 'POST':
        if request.form['num']!='' and request.form['num2']!='':
            a = request.form['num']
            b = request.form['num2']
            return redirect(url_for('sessions'))
        else:
            a = request.form['num']
            b = request.form['num2']
            if a =='':
                if b =='':
                    a = None
                    b = None
                else:
                    a = None
            else:
                b = None
            return redirect(url_for('sessions'))

@app.route('/<name>/memos')
def memos(name):
    if '이동' in request.form:
        return render_template('memo.html', name=name)
    elif 'calcul' in request.form:
        return redirect(url_for('sessions'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
