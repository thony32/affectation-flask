from app import db
from app.models.employee import Employee


def create_employee(username, first_name, last_name, job, password):
    new_employee = Employee(
        username=username, first_name=first_name, last_name=last_name, job=job
    )
    new_employee.set_password(password)
    db.session.add(new_employee)
    db.session.commit()
    return new_employee


def authenticate_employee(username, password):
    employee = Employee.query.filter_by(username=username).first()
    if employee and employee.check_password(password):
        return employee
    return None


def get_employee_by_id(employee_id):
    return Employee.query.get(employee_id)


def update_employee(employee_id, **kwargs):
    employee = get_employee_by_id(employee_id)
    if employee:
        for key, value in kwargs.items():
            setattr(employee, key, value)
        db.session.commit()
    return employee


def delete_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return employee
