from flask import Flask, render_template, request

tasks_todo = []

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        tasks_todo.append(request.form.get('input'))
        print(tasks_todo)
        print(request.form.get('hello'))
    return render_template('index.html', tasks=tasks_todo)

app.run(debug=True)