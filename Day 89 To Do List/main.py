from flask import Flask, render_template, request
from werkzeug.utils import redirect

tasks_todo = []

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        tasks_todo.append(request.form.get('input'))
        print(tasks_todo)
    return render_template('index.html', tasks=tasks_todo)

@app.route('/delete/<int:index>')
def delete(index):
    del tasks_todo[index-1]
    return redirect('/')

app.run(debug=True, port=5001)