from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DiceFrame(db.Model):
    __tablename__ = 'dice_frames'
    id = db.Column(db.Integer, primary_key=True)
    dice_number = db.Column(db.Integer, nullable=False)
    dice_value = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
