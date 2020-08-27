from application import db

class ToldFortunes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeframe = db.Column(db.String(100), nullable=False)
    fortune = db.Column(db.String(100), nullable=False)
    percentage = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join([
            'FortuneID: ', str(self.id), '\r\n',
            'Fortune: ', str(self.fortune), '\r\n'
        ])