import pyodbc
from flask import Flask, render_template, request, redirect

# integração com db;
"Driver={SQL Server};"
r"Server=(local)\SQLEXPRESS;"
"Database=DbApp;"
"Trusted_Connection=yes;"

conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Insira os dados no banco de dados
    cursor.execute("INSERT INTO cadastroUsuarios (emailUsuario, senhaUsuario) VALUES (?, ?)", email, senha)
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
