
from flask import Blueprint, jsonify, request
from app.services.affect_service import create_affect, delete_affect, get_affect_by_id, get_affects, update_affect

affect_api = Blueprint("affect_api", __name__)

# NOTE: Create an affect
@affect_api.route("/affects", methods=["POST"])
def add_affect():
    data = request.get_json()
    try: 
        new_affect = create_affect(
            employee_id=data["employee_id"], place_id=data["place_id"]
        )
        return jsonify({"message": "Affect added", "id": new_affect.id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing data for required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
     
# NOTE: Get all affects
@affect_api.route("/affects", methods=["GET"])
def get_all_affects():
    affects = get_affects()
    return jsonify(affects), 200

# NOTE: Get an affect by id
@affect_api.route("/affects/<int:affect_id>", methods=["GET"])
def get_an_affect(affect_id):
    affect = get_affect_by_id(affect_id)
    return jsonify(affect.to_dict())

# NOTE: Update an affect
@affect_api.route("/affects/<int:affect_id>", methods=["PUT"])
def update_an_affect(affect_id):
    data = request.get_json()
    try:
        updated_affect = update_affect(
            affect_id=affect_id,
            employee_id=data["employee_id"],
            place_id=data["place_id"]
        )
        return jsonify({"message": "Affect updated", "id": updated_affect.id}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing data for required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# NOTE: Delete an affect
@affect_api.route("/affects/<int:affect_id>", methods=["DELETE"])   
def delete_an_affect(affect_id):
    delete_affect(affect_id)
    return jsonify({"message": "Place deleted"}), 200