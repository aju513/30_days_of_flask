from models import app,db
from models.todo import Todo
from flask import render_template,redirect,request
 


@app.route('/',methods=['POST','GET'])
def home():
    tasks_1=Todo.query.all()

    if request.method=='POST':
        content_found=request.form['todolist']
        new_content=Todo(content=content_found)
        try:
            db.session.add(new_content)
            db.session.commit()
            tasks=Todo.query.all()
            return render_template('homepage.html',tasks=tasks)
           
        except:
            return 'there was an error'
        
        
    else:
        return render_template('homepage.html',tasks=tasks_1)

@app.route('/delete/<int:id>',methods=['POST','GET'])
def delete(id):
    delete_content=Todo.query.get(id)
    try:
        db.session.delete(delete_content)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error'

@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    task=Todo.query.get_or_404(id)
    if request.method=='POST':
        task.content=request.form['updatedata']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an error'

    return render_template('update.html',task=task)

