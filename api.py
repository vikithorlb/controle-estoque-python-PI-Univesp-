from flask import Blueprint, request, jsonify
from . import db, Item

api_bp = Blueprint('api', __name__)

@api_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    output = []
    for item in items:
        item_data = {
            'id': item.id,
            'codigo': item.codigo,
            'nome': item.nome,
            'quantidade': item.quantidade
        }
        output.append(item_data)
    return jsonify({'items': output})

@api_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    item_data = {
        'id': item.id,
        'codigo': item.codigo,
        'nome': item.nome,
        'quantidade': item.quantidade
    }
    return jsonify(item_data)

@api_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(codigo=data['codigo'], nome=data['nome'], quantidade=data['quantidade'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item criado com sucesso!'})

@api_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    item.codigo = data['codigo']
    item.nome = data['nome']
    item.quantidade = data['quantidade']
    db.session.commit()
    return jsonify({'message': 'Item atualizado com sucesso!'})

@api_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item excluído com sucesso!'})

