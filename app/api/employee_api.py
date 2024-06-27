from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    # jwt_required,
)
from app.services.employee_service import (
    create_employee,
    get_employee_by_id,
    update_employee,
    delete_employee,
    authenticate_employee,
)

employee_api = Blueprint("employee_api", __name__)


# NOTE: Authentication
@employee_api.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    employee = authenticate_employee(username, password)
    if employee:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


# NOTE: Register (create employee)
@employee_api.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    try:
        new_employee = create_employee(
            username=data["username"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            job=data.get("job", ""),
            password=data["password"],
        )
        return jsonify({"message": "Employee added", "id": new_employee.id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing data for required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# NOTE: Get an employee by id
@employee_api.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    try:
        employee = get_employee_by_id(id)
        if employee:
            return jsonify(employee.to_dict()), 200
        else:
            return jsonify({"error": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# NOTE: Update an employee by id
@employee_api.route("/employees/<int:id>", methods=["PUT"])
def update_employee_by_id(id):
    data = request.get_json()
    try:
        employee = update_employee(id, **data)
        if employee:
            return jsonify(employee.to_dict()), 200
        else:
            return jsonify({"error": "Unable to update employee"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# NOTE: Delete an employee by id    
@employee_api.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee_by_id(id):
    try:
        success = delete_employee(id)
        if success:
            return jsonify({"message": "Employee deleted"}), 200
        else:
            return jsonify({"error": "Failed to delete employee"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500