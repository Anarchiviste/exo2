from flask import Flask
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from .config import Config

app = Flask(
	__name__,
	template_folder='templates',
    static_folder='static',
)

app.config.from_object(Config)

db = SQLAlchemy(app)

from .route import generale