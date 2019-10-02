from flask import Flask, jsonify, abort, make_response, request, url_for


app = Flask(__name__)

#Create two in-memory objects of type tasks
tasks = [
    {
        'id':1,
        'title':u'Buy groceries',
        'description':u'Milk, Cheese, Pizza',
        'done':False
    },
    {
        'id':2,
        'title':u'Go to gym',
        'description':u'Cardio, Triceps, Biceps',
        'done':False
    },
]

#Define a helper to return URI for a given resource
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_tasks',id=task['id'], _external=True)
        else:
            new_task[field]=task[field]
    return new_task


# Get all resources
@app.route("/todo/api/v1.0/tasks",methods=['GET'])
def get_tasks():
    return jsonify({'tasks':[make_public_task(task) for task in tasks]})

#Get a specific resource by id and parameter will be passed on to the service
@app.route("/todo/api/v1.0/tasks/<int:id>",methods=['GET'])
def get_task(id):
    t=[task for task in tasks if task['id']==id]
    if len(t)==0:
        abort(404)
    return jsonify({'task':[make_public_task(t[0])]})

#Define error handler to send Json error message rather than http message
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

#Post method to create new object in collection
@app.route("/todo/api/v1.0/tasks",methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }

    tasks.append(task)
    return jsonify({'task':[make_public_task(task) for task in tasks]}), 201

#Update task by id
@app.route('/todo/api/v1.0/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    t=[task for task in tasks if task['id']==id]
    
    if len(t) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' not in request.json:
        abort(400)
    if 'description' not in request.json:
        abort(400)
    if 'done' not in request.json or type(request.json['done']) is not bool:
        abort(400)
    t[0]['title'] = request.json.get('title',t[0]['title'])
    t[0]['description'] = request.json.get('description',t[0]['description'])
    t[0]['done'] = request.json.get('done',t[0]['done'])
    return jsonify({'task':[make_public_task(t[0])]})

#Delete task by id
@app.route('/todo/api/v1.0/tasks/<int:id>',methods=['DELETE'])
def delete_task(id):

    if len(tasks) == 0:
         abort(404)

    t=[task for task in tasks if task['id']==id]

    if len(t[0]) == 0:
        abort(404)

    tasks.remove(t[0])
    return jsonify({'result':True})

if __name__ == "__main__":
    app.run(debug=True)