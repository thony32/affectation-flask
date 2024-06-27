from app import db

class Place(db.Model):
    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    designation = db.Column(db.String(80), unique=True, nullable=False)
    province = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "designation": self.designation,
            "province": self.province
        }

    def __repr__(self):
        return f"<Place {self.name}>"