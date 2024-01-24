import pyodbc
from flask import Flask, render_template, request
from models import RequestType, request_types

app = Flask(__name__)

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class UserDatabase:
    def __init__(self):
        self.conn = pyodbc.connect(
            "Driver={SQL Server};"
            r"Server=(local)\SQLEXPRESS;"
            "Database=DbApp;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    def add_user(self, user):
        # Check if the email already exists
        self.cursor.execute("SELECT * FROM Users WHERE Email = ?", user.email)
        if self.cursor.fetchone():
            return "Email já cadastrado."

        # Insert new user
        self.cursor.execute(
            "INSERT INTO Users (Username, Email, Password) VALUES (?, ?, ?)",
            user.username, user.email, user.password
        )
        self.conn.commit()
        return "Usuário cadastrado com sucesso!"

db = UserDatabase()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        new_user = User(username, email, password)
        result = db.add_user(new_user)
        return result
    return render_template("index_with_db.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html", request_types=request_types)

@app.route("/submit_request", methods=["POST"])
def submit_request():
    request_type_id = int(request.form["request_type"])
    request_text = request.form["request_text"]

    selected_request_type = next(rt for rt in request_types if rt.id == request_type_id)

    # Aqui você pode adicionar lógica para armazenar a solicitação no banco de dados ou realizar outras ações necessárias

    return f"Solicitação do tipo '{selected_request_type.name}' enviada com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
