from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', back_populates='student')

class DormitoryAssignment(db.Model):
    __tablename__ = 'dormitory_assignments'
    assignment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    dormitory_id = db.Column(db.Integer, nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    student = db.relationship('Student', backref=db.backref('dormitory_assignments', lazy=True))

class AccessRecord(db.Model):
    __tablename__ = 'access_records'
    record_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    access_time = db.Column(db.DateTime, nullable=False)
    access_type = db.Column(db.Enum('in', 'out'), nullable=False)
    student = db.relationship('Student', backref=db.backref('access_records', lazy=True))

class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)

class CourseSelection(db.Model):
    __tablename__ = 'course_selections'
    selection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('course_selections', lazy=True))
    course = db.relationship('Course', backref=db.backref('course_selections', lazy=True))

class PracticalExperiment(db.Model):
    __tablename__ = 'practical_experiments'
    experiment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    experiment_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    course = db.relationship('Course', backref=db.backref('practical_experiments', lazy=True))

class FinancialRecord(db.Model):
    __tablename__ = 'financial_records'
    record_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('paid', 'unpaid'), nullable=False)
    student = db.relationship('Student', backref=db.backref('financial_records', lazy=True))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    student = db.relationship('Student', back_populates='user', uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
