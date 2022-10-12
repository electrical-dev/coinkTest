import email
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/userRecord.db'
db =SQLAlchemy(app)

class registrarUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    ciudad = db.Column(db.String(100))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crear_usuario', methods=['POST'])
def create():
    register = registrarUsuario(name = request.form ['name'], email = request.form ['email'], ciudad = request.form ['ciudad'])
    #db.session.add()

if __name__ == '__main__':
    app.run(port=3000, debug=True)