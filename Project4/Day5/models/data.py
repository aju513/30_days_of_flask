from models import db
 
class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(20),nullable=False,unique=True)
	password=db.Column(db.String(20),nullable=False)
	username=db.Column(db.String(20),nullable=False,unique=True)
	def __repr__(self):
        	return f"User('{self.username}', '{self.email}' )"
	 
