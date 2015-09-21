from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

# import the db from main
from app import db, login_manager


# Models goes here....
class _module1(db.Model):
    __tablename__ = '_module1'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_name = db.Column(db.String(20), nullable= False, unique=True, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255))
    admin = db.Column(db.Boolean)
    bio = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_passowrd(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class PasswordReset(db.Model):
    __tablename__ = 'password_reset'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, index=True)
    token = db.Column(db.String(255), nullable=False, index=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)


class Category(db.Model):
    # table name
    __tablename__ = 'categories'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True, index=True)
    description = db.Column(db.String(255), nullable=True)
    parent = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    # timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    product_id = db.relationship('Product', backref='category', lazy='dynamic')


class Brand(db.Model):
    # Table name
    __tablename__ = 'brands'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean)
    # Timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    product_id = db.relationship('Product', backref='brand', lazy='dynamic')


class Product(db.Model):
    # Table name
    __tablename__ = 'products'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(255), nullable=True)
    active = db.Column(db.Boolean)
    # Timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    # backref Relation
    variation_id = db.relationship('Variation', backref='product', lazy='dynamic')
    option_type_id = db.relationship('OptionType', backref='product', lazy='dynamic')


class Variation(db.Model):
    # table name
    __tablename__ = 'variations'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, nullable=True, unique=True)
    sku = db.Column(db.String(255), nullable=False, unique=True, index=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric)
    cost = db.Column(db.Numeric)
    stock_level = db.Column(db.Integer)
    weight = db.Column(db.Numeric)
    height = db.Column(db.Numeric)
    width = db.Column(db.Numeric)
    length = db.Column(db.Numeric)
    master = db.Column(db.Boolean)
    image = db.Column(db.String(255))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    # Timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class OptionType(db.Model):
    # table name
    __tablename__ = 'option_types'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # Timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    # Backref relation
    option_attribute_id = db.relationship('OptionAttribute', backref='type', lazy='dynamic')
    option_id = db.relationship('Option', backref='variation', lazy='dynamic')

class OptionAttribute(db.Model):
    # table name
    __tablename__ = 'option_attributes'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)
    # Timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    option_type_id = db.Column(db.Integer, db.ForeignKey('option_types.id'))
    # backref relation
    option_id = db.relationship('Option', backref='attribute', lazy='dynamic')


class Option(db.Model):
    # table name
    __tablename__ = 'options'
    # Main Fields
    id = db.Column(db.Integer, primary_key=True)
    # Timestamps
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # Relationship
    variation_id = db.Column(db.Integer, db.ForeignKey('variations.id'))
    option_attribute_id = db.Column(db.Integer, db.ForeignKey('option_attributes.id'))
