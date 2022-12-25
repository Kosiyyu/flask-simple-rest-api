from flask_migrate import Migrate
from db import db
from app import app

migrate = Migrate(app, db)