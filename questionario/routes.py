from flask import render_template, request, session, redirect
from questionario.models import Respostas, Telefone
from questionario import db
import sqlite3

def register_routes(app, db):

    @app.route("/", methods=["GET", "POST"])
    @app.route("/home", methods=["GET", "POST"])
    def home():

        if request.method == 'POST':
            tel = request.form.get('tel')
            telefone = Telefone(tel=tel)
            db.session.add(telefone)
            db.session.commit()

            session['tel'] = tel

            return redirect('/questionario')
        
        return render_template('main.html')

    @app.route("/questionario", methods=["GET", "POST"])
    def questionario():

        tel = session.get("tel")

        if request.method == 'POST':
            comodo = request.form.get('comodo')
            temperatura = request.form.get('temp')
            preferencia = request.form.get('pref')
            consideracao = request.form.get('considera')
            vestimenta = request.form.get('vestimenta')
            atividade = request.form.get('atividade')
            situacao = request.form.getlist('situacao')
            situacao_str = ', '.join(situacao)
            atividade_outro = request.form.get('outro_1_texto') if atividade == 'outro_1' else None
            situacao_outro = request.form.get('outro_2') if request.form.get('situacao') == 'Outra situação' else None
            respostas = Respostas(tel=tel, comodo=comodo, temperatura=temperatura, preferencia=preferencia, consideracao=consideracao, vestimenta=vestimenta, atividade=atividade, situacao=situacao_str, atividade_outro=atividade_outro, situacao_outro=situacao_outro)
            db.session.add(respostas)

            id_do_registro = respostas.id

            for valor in situacao:
                db.session.query(Respostas).filter_by(id=id_do_registro).update({'situacao': valor})

            db.session.commit()

            return redirect("/logout")
        
        return render_template("questionario.html")


    @app.route("/logout", methods=["GET", "POST"])
    def logout():

        if request.method == 'POST':
            session.pop('tel', None)
            return redirect('/popup')

        return render_template("logout.html")


    @app.route("/popup", methods=["GET"])
    def popup():

        return render_template("popup.html")
