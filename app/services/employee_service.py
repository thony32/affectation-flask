from app import db
from app.models.employee import Employee

# NOTE: Sign up
def create_employee(username, first_name, last_name, job, password):
    new_employee = Employee(
        username=username, first_name=first_name, last_name=last_name, job=job
    )
    new_employee.set_password(password)
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

# NOTE: Authentication
def authenticate_employee(username, password):
    employee = Employee.query.filter_by(username=username).first()
    if employee and employee.check_password(password):
        return employee
    return None

# NOTE: get by id
def get_employee_by_id(employee_id):
    return Employee.query.get(employee_id)

# REFACTOR: update
def update_employee(employee_id, **kwargs):
    employee = get_employee_by_id(employee_id)
    if employee:
        for key, value in kwargs.items():
            setattr(employee, key, value)
        db.session.commit()
    return employee

# NOTE: Delete
def delete_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return employee
