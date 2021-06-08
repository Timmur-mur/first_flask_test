from app import db
from transcript import Transcript


class Eat(db.Model):
    __tablename__ = 'Eat'
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(100), unique = True)#переписать слаг в транслитерацию и через дефис
    tipe = db.Column(db.String(20), nullable = False)
    namefoto = db.Column(db.String(60), unique = True, nullable = False)
    name = db.Column(db.String(60), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    body = db.Column(db.String)
    basket_id = db.Column(db.Integer, db.ForeignKey('Basket.id'))
    

    def __init__(self, *args, **kwargs):
        super(Eat, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        s = Transcript(self.name)
        self.slug = s.tran_word()

    def __repr__(self):
        return 'Name eat: {}, Price {}'.format(self.name, self.price)

roles_users = db.Table('role_user',
    db.Column("user_id", db.Integer(), db.ForeignKey('User.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('Role.id')))

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True )
    phone = db.Column(db.String(100))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    hesh = db.Column(db.String(512))
    code = db.Column(db.Integer)
    
    role = db.relationship('Role', secondary = roles_users, backref = db.backref('users', lazy = 'dynamic'))

    basket = db.relationship('Basket', uselist = False, backref = 'user')
    

    def __repr__(self):
        return 'name: {}, email: {}'.format(self.name, self.email)

class Role(db.Model):
    __tablename__ = 'Role'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(100), unique = True)

class Basket(db.Model):
    __tablename__ = 'Basket'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    items_order = db.relationship('Eat', lazy = 'select')

class Orders(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.PickleType)
    items_order = db.Column(db.PickleType)
    status = db.Column(db.Boolean)




class News_page(db.Model):
    __tablename__ = 'News_page'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String)

