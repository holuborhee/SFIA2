from application import db
from application.models import ToldFortunes

db.drop_all()
db.create_all()