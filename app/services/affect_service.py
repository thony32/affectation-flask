from app.models.affect import Affect
from app import db

def create_affect(employee_id, place_id):
    affect = Affect(employee_id=employee_id, place_id=place_id)
    db.session.add(affect)
    db.session.commit()
    return affect

def get_affects():
    return [affect.to_dict() for affect in Affect.query.all()]

def get_affect_by_id(affect_id):
    return Affect.query.get(affect_id)

def update_affect(affect_id, employee_id, place_id):
    affect = get_affect_by_id(affect_id)
    affect.employee_id = employee_id
    affect.place_id = place_id
    db.session.commit()
    return affect

def delete_affect(affect_id):
    affect = get_affect_by_id(affect_id)
    db.session.delete(affect)
    db.session.commit()
    return None