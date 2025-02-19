from . import db

class Member(db.Model):
   __tablename__ = 'Member'
   MID = db.Column(db.Integer, primary_key=True, nullable=False)
   F_name = db.Column(db.String(20), nullable=False)
   L_name = db.Column(db.String(20))
   Password = db.Column(db.String(15), nullable=False)
   Gender = db.Column(db.Enum('Male', 'Female', 'Other'), nullable=False)
   Email = db.Column(db.String(100), unique=True, nullable=False)
   Phone = db.Column(db.String(10), nullable=False)
   Birth = db.Column(db.Date)
   Address = db.Column(db.String(200))
   Reg_date = db.Column(db.Date, nullable=False)
   A_flag = db.Column(db.Boolean, nullable=False)
   S_flag = db.Column(db.Boolean, nullable=False)
   C_flag = db.Column(db.Boolean, nullable=False)
