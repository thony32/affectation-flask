from datetime import datetime
from app import db 

class Affect(db.Model):
    __tablename__ = 'affects'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
    date = db.Column(db.DateTime, default=datetime.now)
    
    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "place_id": self.place_id,
            "date": self.date
        }
    
    def __repr__(self):
        return f"<Affect {self.id}>"