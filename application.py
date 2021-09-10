from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'karasumorih93094hjjbdihr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///upfk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Alat(db.Model):
    nomor = db.Column(db.Integer, primary_key=True)
    nama_alat = db.Column(db.String(50), nullable=False)
    merk = db.Column(db.String(50), nullable=False)
    peminjam = db.relationship('Peminjaman', backref='alat', lazy=True)

    def __repr__(self):
        return f"alat: {self.nama_alat}"

class Peminjaman(db.Model):
    nomor = db.Column(db.Integer, primary_key=True)
    nama_peminjam = db.Column(db.String(50), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.now())
    id_alat = db.Column(db.Integer, db.ForeignKey(Alat.nomor), nullable=False)

    def __repr__(self):
        return f"peminjam: {self.nama_peminjam}"

@app.route('/')
def index():
    return render_template('beranda.html')

@app.route('/input')
def input():
    return render_template('input_alat.html')


if __name__=="__main__":
    app.run(debug=True)