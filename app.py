from flask import Flask, request, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from config import DATABASE_CONFIG
from db import db      

app = Flask(__name__)

db_url = f"{DATABASE_CONFIG['provider']}://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def init_tables():
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)











































# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/flask_test"
                                          #postgresql://postgres:alamakota123@localhost:5432/flask_test
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# ma = Marshmallow(app)


# db.create_all

# @app.route('/', methods=['GET'])
# def get_all():
#     return jsonify({'name': 'alan'})

# #{'msg': 'Hello world'}


# if __name__ == '__main__':
#     app.run(debug=True)
