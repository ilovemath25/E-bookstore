from . import db

class Product(db.Model):
    __tablename__ = 'Product'
    PID = db.Column(db.Integer, primary_key=True, nullable=False)
    SMID = db.Column(db.Integer, db.ForeignKey('Member.MID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    SpEvent_ID = db.Column(db.Integer, db.ForeignKey('Special_event.DID', onupdate="CASCADE", ondelete="SET NULL"))
    Name = db.Column(db.String(100), nullable=False)
    Desc = db.Column(db.String(1000))
    Author = db.Column(db.String(50))
    Price = db.Column(db.Integer, nullable=False)
    Stock_quantity = db.Column(db.Integer, nullable=False)
    Category = db.Column(db.String(20))
    Product_pict = db.Column(db.String(100))
    Sale_count = db.Column(db.Integer, nullable=False)