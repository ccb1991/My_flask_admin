"""
Created by 陈辰柄 
datetime:2019/9/25 22:03
Describe:
"""

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import config
from app.models import User,Post,db

admin = Admin(name='microblog', template_mode='bootstrap3')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    return app
