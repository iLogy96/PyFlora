import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
import os


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(40), nullable = False, unique=True)
    password = db.Column(db.String(40), nullable = False)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40))

class Plant(Base):
    __tablename__ = "plants"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40))
    about = db.Column(db.String())
    photo = db.Column(db.String(40))
    hydration = db.Column(db.String(40))
    light = db.Column(db.String(10))
    warmth = db.Column(db.String(40))
    pH = db.Column(db.String(10))
    substrate = db.Column(db.String(200))  

class Pot(Base):
    __tablename__ = "pots"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40))
    location = db.Column(db.String(40))
    plant_id = db.Column(db.Integer(), db.ForeignKey("plants.id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))

class Data(Base):
    __tablename__ = "data"
    id = db.Column(db.Integer(), primary_key=True)
    api_temp = db.Column(db.String())
    sen_light = db.Column(db.String(10))
    sen_temp = db.Column(db.Float())
    sen_hydration = db.Column(db.Float())
    sen_pH = db.Column(db.Float())
    sen_date = db.Column(db.DateTime(), default= datetime.datetime.today)
    pot_id = db.Column(db.Integer(), db.ForeignKey("pots.id"))
    plant_id = db.Column(db.Integer(), db.ForeignKey("plants.id"))
    

def create_and_connect():
    """
    Main module function

    Connects to the database and check if it exists, otherwise creates it

    Makes a session so we can use it in an app
    """
    BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database")

    conn = "sqlite:///" + os.path.join(BASE_DIR, 'database.sqlite')
    db_engine = db.create_engine(conn)
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()
    return session

class Database_repo:
    def __init__(self, session):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_username(self, username):
        try:
            return self.session.query(User).filter(User.username==username).first()
        except Exception as e:
            print(f"User {username} not found: {e}")
            return None
        
    def get_user_by_userid(self, user_id):
        return self.session.query(User).filter(User.id==user_id).first()

    def update_user(self, user):
        self.session.add(user)
        self.session.commit()
    
    def get_all_plants(self):
        return self.session.query(Plant).all()
    
    def create_plant(self, plant: Plant):
        self.session.add(plant)
        self.session.commit()

    def update_plant(self, plant:Plant):
        self.session.add(plant)
        self.session.commit()

    def delete_plant(self, plant:Plant):
        self.session.delete(plant)
        self.session.commit()
        
    def get_plant_by_id(self, plant_id):
        return self.session.query(Plant).filter(Plant.id == plant_id).first()
    
    def get_plant_by_name(self, plant_name):
        return self.session.query(Plant).filter(Plant.name == plant_name).first()

    def get_all_pots(self, user_id):
        return self.session.query(Pot).filter(Pot.user_id== user_id).all()
    
    def get_a_pot(self, user_id):
        return self.session.query(Pot).filter(Pot.user_id== user_id).first()
    
    def get_all_pots_plant(self, user_id, plant_id):
        return self.session.query(Pot).filter(Pot.user_id== user_id).filter(Pot.plant_id == plant_id).all()
    
    def get_all_data(self, pot, plant):
        data = self.session.query(Data).filter(Data.pot_id== pot.id).filter(Data.plant_id== plant.id).all()
        return data
    
    def create_pot(self, pot: Pot, user_id):
        pot.user_id = user_id
        self.session.add(pot)
        self.session.commit()

    def create_data(self, data: Data):
        self.session.add(data)
        self.session.commit()

    def delete_pot(self, pot: Pot):
        self.session.delete(pot)
        self.session.commit()

    def update_pot(self, pot: Pot):
        self.session.add(pot)
        self.session.commit()

def connect_repo_to_db():
    try:
        session = create_and_connect()
        repo = Database_repo(session)
        return repo
    except Exception as e:
        print(e)
        return None
    

