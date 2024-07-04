from questionario import db


class Telefone(db.Model):

    __tablename__ = 'telefone'

    id = db.Column(db.Integer, primary_key=True)
    tel = db.Column(db.String(4), nullable=True)

class Respostas(db.Model):

    __tablename__ = 'respostas'

    id = db.Column(db.Integer, primary_key=True)
    tel = db.Column(db.String(4), db.ForeignKey('telefone.tel'), nullable=True)
    comodo = db.Column(db.String(50), nullable=True)
    temperatura = db.Column(db.String(50), nullable=True)
    preferencia = db.Column(db.String(50), nullable=True)
    consideracao = db.Column(db.String(50), nullable=True)
    vestimenta = db.Column(db.String(50), nullable=True)
    atividade = db.Column(db.String(100), nullable=True)
    situacao = db.Column(db.String(200), nullable=True)
    atividade_outro = db.Column(db.String(100), nullable=True)
    situacao_outro = db.Column(db.String(100), nullable=True)
