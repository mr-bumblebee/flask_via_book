from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship("User", backref='role')

    def __repr__(self):
        return f'<Role( id: {self.id}, name: {self.name})>'

    def __str__(self):
        return f'name: {self.name}'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'<User( id: {self.id}, name: {self.name})>'

    def __str__(self):
        return f'name: {self.name}'
