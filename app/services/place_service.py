from app.models.place import Place
from app import db

def create_place(designation, province):
    place = Place(designation=designation, province=province)
    db.session.add(place)
    db.session.commit()
    return place

def get_places():
    return [place.to_dict() for place in Place.query.all()]

def get_place_by_id(place_id):
    return Place.query.get(place_id)

def update_place(place_id, designation, province):
    place = get_place_by_id(place_id)
    place.designation = designation
    place.province = province
    db.session.commit()
    return place

def delete_place(place_id):
    place = get_place_by_id(place_id)
    db.session.delete(place)
    db.session.commit()
    return None