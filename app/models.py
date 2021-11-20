from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from . import db,login_manager
from datetime import datetime
from hashlib import md5


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    language = db.Column(db.String)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    stars = db.relationship('Star', backref='post', lazy='dynamic')
    posted_p = db.Column(db.DateTime,default=datetime.utcnow)
    user_p = db.Column(db.Integer,db.ForeignKey("users.id"),  nullable=False)
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        posts = Post.query.order_by(post_id=id).desc().all()
        return posts
    
    def __repr__(self):
        return f"Post {self.title}','{self.posted_p}')"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted_c = db.Column(db.DateTime,default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    user_c = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post):
        comments = Comment.query.filter_by(postit = post).all()
        return comments

    @classmethod
    def delete_comment(cls,id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments
    def __repr__(self):
        return f'Comment{self.comment}'


class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    user_post = db.relationship('Post', backref='user', lazy='dynamic')
    user_comment = db.relationship('Comment', backref='user', lazy='dynamic')
    stars = db.relationship('Star', backref='user', lazy='dynamic')


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Star(db.Model):
    __tablename__ = 'stars'

    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer, default=1)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_stars(self):
        db.session.add(self)
        db.session.commit()

    def add_stars(cls, id):
        star_post = Star(post_id=id)
        star_post.save_stars()

    @classmethod
    def get_stars(cls, id):
        star = Star.query.filter_by(post_id=id).all()
        return star

    @classmethod
    def get_all_stars(cls, post_id):
        stars = Star.query.order_by('id').all()
        return stars

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'
