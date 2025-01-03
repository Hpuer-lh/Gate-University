from flask import Flask, render_template, request, redirect, url_for, flash, session
import random
from models import db, User, Student
from config import Config
from route.student import student_bp
from route.dormitory import dormitory_bp
from route.academic import academic_bp
from route.financial import financial_bp
from route.admin import admin_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(student_bp)
app.register_blueprint(dormitory_bp)
app.register_blueprint(academic_bp)
app.register_blueprint(financial_bp)
app.register_blueprint(admin_bp)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        captcha = request.form['captcha']
        if int(captcha) != session.get('captcha_answer'):
            flash('验证码错误', 'danger')
            generate_captcha()
        else:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                flash('登录成功！', 'success')
                return redirect(url_for('index'))
            else:
                flash('用户名或密码错误', 'danger')
                generate_captcha()
    else:
        generate_captcha()
    return render_template('login.html')

def generate_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    session['captcha_question'] = f"{num1} + {num2} = ?"
    session['captcha_answer'] = num1 + num2

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        student_id = request.form.get('student_id')

        # 检查 students 表是否为空
        students_empty = Student.query.count() == 0

        if students_empty and username == 'root':
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            # 插入管理员信息
            admin_student = Student(student_id='32767', name='root', age=20, major='管理员', user_id=new_user.id)
            db.session.add(admin_student)
            db.session.commit()

            flash('注册成功，请登录', 'success')
            return redirect(url_for('login'))

        student = Student.query.filter_by(student_id=student_id).first()
        if not student:
            flash('学生ID不存在', 'danger')
        elif User.query.filter_by(username=username).first():
            flash('用户名已存在', 'danger')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            new_user.student = student
            db.session.add(new_user)
            db.session.commit()
            flash('注册成功，请登录', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('您已成功退出登录', 'success')
    return redirect(url_for('login'))

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        student = user.student
        backgrounds = ['1.jpg', '2.jpg', '3.jpg']
        random_bg = random.choice(backgrounds)
        return render_template('index.html', random_bg=random_bg, student=student)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)