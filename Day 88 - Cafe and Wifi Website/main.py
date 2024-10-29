from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, and_
from wx.lib.agw.hypertreelist import method

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///cafes.db'
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



app.run(debug=True)