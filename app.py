from flask import Flask, render_template, request, redirect
from main import add_student, view_students, update_student, delete_student

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    students = view_students()
    selected_student = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add":
            uni_no = request.form.get("uni_no")
            name = request.form.get("name")
            course = request.form.get("course")
            phone_number = request.form.get("phone_number")
            if uni_no and name and course and phone_number:
                add_student(uni_no, name, course, phone_number)
                return redirect("/")

        elif action == "update":
            uni_no = request.form.get("uni_no")
            name = request.form.get("name")
            course = request.form.get("course")
            phone_number = request.form.get("phone_number")
            if uni_no and name and course and phone_number:
                update_student(uni_no, name, course, phone_number)
                return redirect("/")

        elif action == "delete":
            uni_no = request.form.get("uni_no")
            if uni_no:
                delete_student(uni_no)
                return redirect("/")

    elif request.method == "GET":
        uni_no = request.args.get("edit")
        if uni_no:
            for student in students:
                if str(student["uni_no"]) == str(uni_no):
                    selected_student = student
                    break

    return render_template("index.html", students=students, selected_student=selected_student)

if __name__ == "__main__":
    app.run(debug=True)
