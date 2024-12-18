from flask import Flask, render_template, redirect, request
import stripe
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, UserMixin, LoginManager, login_required, logout_user, current_user

# api from stripe page
stripe.api_key = 'stripe key'
YOUR_DOMAIN = 'http://localhost:4242'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_hehe'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(UserMixin, db.Model):
    id: Mapped[id] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))

with app.app_context():
    db.create_all()

# LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()

# creating a product with stripe
pr_1 = stripe.Product.create(name="t-shirt")
pr_1_id = stripe.Price.create(
    product=pr_1,
    unit_amount=2000,
    currency="usd"
)

pr_2 = stripe.Product.create(name="lalala")
pr_2_id = stripe.Price.create(
    product=pr_2,
    unit_amount=1000,
    currency='usd'
)

pr_3 = stripe.Product.create(name="backpack")
pr_3_id = stripe.Price.create(
    product=pr_3,
    unit_amount=1000,
    currency='usd'
)
items_id = [pr_1_id, pr_2_id, pr_3_id]
shopping_cart = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            ok = check_password_hash(pwhash=user.password, password=password)
            if ok:
                login_user(user)
                return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    if current_user:
        print(current_user.name)
    logout_user()
    return redirect('/')

@app.route('/secret')
@login_required
def secret():
    return render_template('success.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        secure_password = generate_password_hash(password=request.form['password'], method='pbkdf2:sha256', salt_length=8)
        new_user = User(name=request.form['name'],
                        email=request.form['email'],
                        password=secure_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/add/<int:id>', methods=["POST"])
def add(id):
    shopping_cart.append(items_id[id])
    return redirect('/')

@app.route('/delete')
def delete():
    global shopping_cart
    shopping_cart = []
    return redirect('/')

@app.route('/create-checkout-session', methods=['POST', 'GET'])
def create_checkout_session():
    if len(shopping_cart) > 0:

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[{'price': id, 'quantity': shopping_cart.count(id)} for id in items_id if id in shopping_cart
                    # {
                    #     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    #     'price': items_id[1],
                    #     'quantity': 1,
                    # },
                    # { 'price': items_id[2], 'quantity': 1},
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)
    else:
        return redirect('/')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True, port=4242)
