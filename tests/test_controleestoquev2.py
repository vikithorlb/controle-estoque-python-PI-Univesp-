import unittest
from seu_projeto.app import app, db, Item

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app = app.test_client()
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_adicionar_item(self):
        response = self.app.post('/add', data={'codigo': 123, 'nome': 'Produto Teste', 'quantidade': 50})
        self.assertEqual(response.status_code, 302)
        item = Item.query.filter_by(codigo=123).first()
        self.assertIsNotNone(item)

if __name__ == '__main__':
    unittest.main()
