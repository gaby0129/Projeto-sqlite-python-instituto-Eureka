import sqlite3

def conectar():
    return sqlite3.connect('Instituto_Eureka.db')

def criar_tabelas():
    banco = conectar()
    cursor = banco.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
        matricula INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        data_matricula TEXT NOT NULL        

    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Notas (
        id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        matricula_aluno INTEGER NOT NULL,
        disciplina TEXT NOT NULL,
        nota REAL NOT NULL,
        data_avaliacao TEXT NOT NULL,
        FOREIGN KEY (matricula_aluno) REFERENCES Alunos(matricula)
    )
    ''')
    banco.commit()
    banco.close()