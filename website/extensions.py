from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()




# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created!')