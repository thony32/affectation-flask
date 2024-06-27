from flask import Blueprint, jsonify, request
from app.services.place_service import create_place, delete_place, get_place_by_id, get_places, update_place

place_api = Blueprint("place_api", __name__)


# NOTE: create place
@place_api.route("/places", methods=["POST"])
def add_place():
    data = request.get_json()
    # Map JSON keys to function parameters
    try:
        new_place = create_place(
            designation=data["designation"], province=data["province"]
        )
        return jsonify({"message": "Place added", "id": new_place.id}), 201
    except KeyError as e:
        # Handle missing data cases
        return jsonify({"error": f"Missing data for required field: {str(e)}"}), 400
    except Exception as e:
        # Generic error handling
        return jsonify({"error": str(e)}), 500


# NOTE: get all places
@place_api.route("/places", methods=["GET"])
def get_all_places():
    places = get_places()
    return jsonify(places), 200


# NOTE: get by id
@place_api.route("/places/<int:id>", methods=["GET"])
def get_place(id):
    place = get_place_by_id(id)
    if place:
        return jsonify(place.to_dict()), 200
    else:
        return jsonify({"error": "Place not found"}), 404


# NOTE: update place
@place_api.route("/places/<int:id>", methods=["PUT"])
def update_a_place(id):
    data = request.get_json()
    try:
        updated_place = update_place(
            place_id=id,
            designation=data["designation"],
            province=data["province"],
        )
        return jsonify({"message": "Place updated", "id": updated_place.id}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing data for required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# NOTE: delete place
@place_api.route("/places/<int:id>", methods=["DELETE"])
def delete_place_by_id(id):
    delete_place(id)
    return jsonify({"message": "Place deleted"}), 200
