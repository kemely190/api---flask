from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configurar banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',  
    'database': 'aula'  
}

# Rota: cadastrar o aluno
@app.route('/aula', methods=['POST'])
def cadastrar_aluno():
    data = request.get_json()
    nome = data['nome']
    email = data['email']
    matricula = data['matricula']
    senha = data['senha']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO aluno (matricula, nome, email, senha) VALUES (%s, %s, %s, %s)",
                   (matricula, nome, email, senha))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'Resultado': 'Aluno cadastrado com sucesso!'})

# Rota: listar os alunos no navegador
@app.route('/aulas', methods=['GET'])
def listar_alunos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aluno")
    aulas = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(aulas)

if __name__ == '__main__':
    app.run(debug=True)