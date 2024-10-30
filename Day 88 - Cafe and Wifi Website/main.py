from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, and_

from flask_bootstrap import Bootstrap5, Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import SubmitField, StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, URL

SECRET_KEY = 'xdd'

class AddCafe(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe Location of Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Cafe img (URL)', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Number of seats', validators=[DataRequired()])
    coffee_price = StringField('Caffe price', validators=[DataRequired()])
    has_toilet = BooleanField('Has toilets?', default=False, false_values=('False', 'false', ''))
    has_wifi = BooleanField('Has wifi?', default=False, false_values=('False', 'false', ''))
    has_sockets = BooleanField('Has sockets?', default=False, false_values=('False', 'false', ''))
    can_take_calls = BooleanField('Can take calls?', default=False, false_values=('False', 'false', ''))
    submit = SubmitField('Submit')
app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

with app.app_context():
    db.create_all()


with app.app_context():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    print(result[0].name)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        with app.app_context():
            database = db.session.execute(db.select(Cafe)).scalars().all()
    if request.method == 'POST':
        try:
            sockets = bool(int(request.form["has_socket"]))
        except:
            sockets = 0

        try:
            wifi = bool(int(request.form["has_wifi"]))
        except:
            wifi = 0

        try:
            toilet = bool(int(request.form["has_toilet"]))
        except:
            toilet = 0

        with app.app_context():
            database = db.session.execute(db.select(Cafe).filter(
                and_(
                    Cafe.has_sockets == sockets),
                    Cafe.has_wifi == wifi,
                    Cafe.has_toilet == toilet)).scalars().all()
    return render_template('index.html', database=database)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddCafe()
    if request.method == 'POST':
        new_cafe = Cafe(name=request.form.get('name'),
                        map_url=request.form.get('map_url'),
                        img_url=request.form.get('img_url'),
                        location=request.form.get('location'),
                        seats=request.form.get('seats'),
                        has_toilet=bool(request.form.get('has_toilet')),
                        has_wifi=bool(request.form.get('has_wifi')),
                        has_sockets=bool(request.form.get('has_sockets')),
                        can_take_calls=bool(request.form.get('can_take_calls')),
                        coffee_price=request.form.get('coffee_price'))
        db.session.add(new_cafe)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=form)

@app.route('/delete/<int:id>') #methods=['DELETE'] doesnt work...?
def delete(id):
    coffee_to_delete = db.get_or_404(Cafe, id)
    if coffee_to_delete:
        db.session.delete(coffee_to_delete)
        db.session.commit()
    return redirect('/')
app.run(debug=True)