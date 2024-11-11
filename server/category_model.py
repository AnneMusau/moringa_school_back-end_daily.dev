from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from subscription_model import Subscription

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    subscribed_at = db.Column(db.DateTime, default = db.func.now())

    # Relationship mapping category to posts
    posts = db.relationship('Content', back_populates='category')

    # Relationship mapping category to subscription
    subscriptions = db.relationship('Subscription', back_populates='category')

    # Association proxy
    subscribers = association_proxy('subscriptions', 'user', creator = lambda user_obj: Subscription(user = user_obj, subscribed_at = db.func.now()))

    # Serialization rules
    serialize_rules = ('-posts.category', '-subscriptions.category')

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

    