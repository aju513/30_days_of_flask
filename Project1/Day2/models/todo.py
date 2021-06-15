from models import db

class Todo(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    content=db.Column(db.String(),nullable=False)  

