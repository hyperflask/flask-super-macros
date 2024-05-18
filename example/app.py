from flask import Flask, render_template, request
from flask_super_macros import SuperMacros
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    done: bool

TASKS = [Task(1, "task 1", True), Task(2, "task 2", False)]

app = Flask(__name__)
SuperMacros(app)

# define macros as functions
@app.macro
def SubmitBtn(**kwargs):
    """<{button type="submit" **kwargs}>{{ inner }}</{}>"""

@app.route("/")
def index():
    return render_template("index.html", tasks=TASKS)

@app.route("/btn")
def btn():
    return SubmitBtn(style="color: red")("hello") # call a macro defined as a function

@app.post("/toggle/<int:task_id>")
def toggle(task_id):
    task = [t for t in TASKS if t.id == task_id][0]
    task.done = not task.done
    return app.macros.Task(task=task)

@app.post('/create')
def create():
    task = Task(len(TASKS) + 1, request.form['title'], False)
    TASKS.append(task)
    return app.macros.Task(task=task)

@app.post("/delete/<int:task_id>")
def delete(task_id):
    TASKS.remove([t for t in TASKS if t.id == task_id][0])
    return ""


if __name__ == "__main__":
    app.run(debug=True)