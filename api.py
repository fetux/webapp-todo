from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fwqqvxftanafet:d3f7124ad7379c86ec15685c7b5f2fdf3a5097e29f897ef170b0ff951ebb7004@ec2-54-235-193-0.compute-1.amazonaws.com:5432/dgk6fl10nffv4'
db = SQLAlchemy(app)
api = Api(app)

##################################
# TASK MODEL
##################################


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'task': self.task
        }

    def __repr__(self):
        return '<Task %r>' % self.task


db.create_all()


##################################
# WEB CONTROLLER
##################################


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task = Task(task=request.form['task'])
        db.session.add(task)
        db.session.commit()

    return render_template('index.html', tasks=Task.query.all())

##################################
# API INTERFACE
##################################


parser = reqparse.RequestParser()
parser.add_argument('task')


class TaskList(Resource):
    def get(self):
        return [task.serialize() for task in Task.query.all()]

    def post(self):
        args = parser.parse_args()
        task = Task(task=args['task'])
        db.session.add(task)
        db.session.commit()
        return task.serialize(), 201


# API Routes
api.add_resource(TaskList, '/api/tasks')


if __name__ == '__main__':
    app.run(debug=True)