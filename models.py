from exts import db

class Recommend(db.Model):
    __tablename__ = 'recommend'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class Action(db.Model):
    __tablename__ = 'action'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class Fiction(db.Model):
    __tablename__ = 'fiction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class War(db.Model):
    __tablename__ = 'war'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class Love(db.Model):
    __tablename__ = 'love'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class Funny(db.Model):
    __tablename__ = 'funny'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)