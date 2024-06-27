from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
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

# NOTE: Sign up
@employee_api.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    # Map JSON keys to function parameters
    try:
        new_employee = create_employee(
            username=data["username"],
            first_name=data.get(
                "first_name", ""
            ),  # Default to an empty string if not provided
            last_name=data.get("last_name", ""),
            job=data.get("job", ""),
            password=data["password"],
        )
        return jsonify({"message": "Employee added", "id": new_employee.id}), 201
    except KeyError as e:
        # Handle missing data cases
        return jsonify({"error": f"Missing data for required field: {str(e)}"}), 400
    except Exception as e:
        # Generic error handling
        return jsonify({"error": str(e)}), 500


@employee_api.route("/employees/<int:id>", methods=["GET", "PUT", "DELETE"])
@jwt_required()
def handle_employee(id):
    if request.method == "GET":
        # FIXME: get by id
        employee = get_employee_by_id(id)
        return jsonify(employee), 200
    elif request.method == "PUT":
        # REFACTOR: update
        data = request.get_json()
        employee = update_employee(id, **data)
        return jsonify(employee), 200
    elif request.method == "DELETE":
        # NOTE: delete
        employee = delete_employee(id)
        return "", 204
