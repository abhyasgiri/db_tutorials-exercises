from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.89.117.45/flask_db' # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    orders = db.relationship('Orders', backref='customer')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Orders', backref ='product')

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers_id'), nullable=False)
    product_d = db.Column(db.Integer, db.ForeignKey('prodcuts_id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')

