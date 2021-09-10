from flask import Flask, json, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Buku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    penulis = db.Column(db.String(100), nullable = False)
    penerbit = db.Column(db.String(100), nullable = False)
    tahun = db.Column(db.String(4), nullable=False)
    penjualan =db.relationship('Penjualan', backref='buku', lazy=True)

    def __init__(self, judul, penulis,penerbit,tahun):
        __tablename__ = "buku"
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun = tahun

    def __repr__(self):
        return f"Judul buku : {self.judul}"

class Penjualan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jumlah = db.Column(db.Integer)
    hari = db.Column(db.String(20))
    buku_id = db.Column(db.Integer, db.ForeignKey(Buku.id), nullable=False)

    def __repr__(self):
        return f"id penjualan : {self.id}"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ajaxlivesearch', methods=["POST", "GET"])
def ajaxlivesearch():
    if request.method == "POST":
        search_word = request.form['hasil']
        print(search_word)

        if search_word == '':
            buku = Buku.query.filter().all()
        else:
            cari = "%{}%".format(search_word)
            buku = Buku.query.filter(Buku.judul.like(cari))
        
    return jsonify({'htmlresponse': render_template('response.html', buku=buku)})


if __name__=="__main__":
    app.run(debug=True)