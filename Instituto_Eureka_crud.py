from Instituto_Eureka_database import conectar

def criar_aluno(nome, idade, data_matricula):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Alunos ( nome, idade, data_matricula) VALUES ( ?, ?, ?)", 
                   ( nome, idade, data_matricula))
    conn.commit()
    conn.close()

def ler_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def atualizar_aluno(matricula, nome, idade, data_matricula):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Alunos SET nome = ?, idade = ?, data_matricula = ? WHERE matricula = ?", 
                   (nome, idade, data_matricula, matricula))
    conn.commit()
    conn.close()

def deletar_aluno(matricula):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Alunos WHERE matricula = ?", (matricula,))
    conn.commit()
    conn.close()

def criar_nota(matricula_aluno, disciplina, nota, data_avaliacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Notas (matricula_aluno, disciplina, nota, data_avaliacao) VALUES (?, ?, ?, ?)", 
                   (matricula_aluno, disciplina, nota, data_avaliacao))
    conn.commit()
    conn.close()

def ler_notas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notas")
    notas = cursor.fetchall()
    conn.close()
    return notas

def atualizar_nota(id_materia, matricula_aluno, disciplina, nota, data_avaliacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Notas SET matricula_aluno = ?, disciplina = ?, nota = ?, data_avaliacao = ? WHERE id_materia = ?", 
                   (matricula_aluno, disciplina, nota, data_avaliacao, id_materia))
    conn.commit()
    conn.close()

def deletar_nota(id_materia):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notas WHERE id_materia = ?", (id_materia,))
    conn.commit()
    conn.close()
