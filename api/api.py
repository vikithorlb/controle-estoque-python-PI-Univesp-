from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return items_schema.jsonify(items)

@app.route('/api/items/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    return item_schema.jsonify(item)

@app.route('/api/items', methods=['POST'])
def add_item():
    codigo = request.json['codigo']
    nome = request.json['nome']
    quantidade = request.json['quantidade']
    new_item = Item(codigo=codigo, nome=nome, quantidade=quantidade)
    db.session.add(new_item)
    db.session.commit()
    return item_schema.jsonify(new_item)

@app.route('/api/items/<id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)
    codigo = request.json['codigo']
    nome = request.json['nome']
    quantidade = request.json['quantidade']
    item.codigo = codigo
    item.nome = nome
    item.quantidade = quantidade
    db.session.commit()
    return item_schema.jsonify(item)

@app.route('/api/items/<id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return item_schema.jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
