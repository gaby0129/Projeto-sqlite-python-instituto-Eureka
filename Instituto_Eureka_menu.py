import os
import Instituto_Eureka_crud


def exibir_menu():
    print("------------------------------")
    print("|      Instituto Eureka      |")
    print("------------------------------\n")
    print("alunos----------------------\n")
    print("  1. Criar aluno")
    print("  2. Ler alunos")
    print("  3. Atualizar aluno")
    print("  4. Deletar aluno")
    print("")
    print("matérias--------------------\n")
    print("  5. Criar nota")
    print("  6. Ler notas")
    print("  7. Atualizar nota")
    print("  8. Deletar nota")
    print("\n------------------------------")
    print("  9. Sair")
    print("------------------------------\n")
def listar_alunos():
    alunos = Instituto_Eureka_crud.ler_alunos()
    print("\nLista de Alunos:\n")
    for aluno in alunos:
        print(f"Matrícula: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Idade: {aluno[2]}")
        print(f"Data de Matrícula: {aluno[3]}\n")

def listar_notas():
    notas = Instituto_Eureka_crud.ler_notas()
    print("\nLista de Notas:\n")
    for nota in notas:
        print(f"ID da Matéria: {nota[0]}")
        print(f"Matrícula do Aluno: {nota[1]}")
        print(f"Disciplina: {nota[2]}")
        print(f"Nota: {nota[3]}")
        print(f"Data de Avaliação: {nota[4]}\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            listar_alunos()
            print("\nVocê escolheu: Criar aluno\n")
            nome = input("\nNome: ")
            idade = int(input("\nIdade: "))
            data_matricula = input("\nData de matrícula (DD-MM-AAAA): ")
            Instituto_Eureka_crud.criar_aluno(nome, idade, data_matricula)
            limpar_tela()
        elif escolha == '2':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Ler alunos\n")
            listar_alunos()

        elif escolha == '3':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Atualizar aluno\n")
            listar_alunos()
            matricula = int(input("\nMatrícula do aluno a ser atualizado: "))
            nome = input("\nNovo nome: ")
            idade = int(input("\nNova idade: "))
            data_matricula = input("\nNova data de matrícula (DD-MM-AAAA): ")
            Instituto_Eureka_crud.atualizar_aluno(matricula, nome, idade, data_matricula)
            limpar_tela()
        
        elif escolha == '4':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Deletar aluno\n")
            listar_alunos()
            matricula = int(input("Matrícula do aluno a ser deletado: "))
            Instituto_Eureka_crud.deletar_aluno(matricula)
            limpar_tela()




        elif escolha == '5':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Criar nota\n")
            listar_alunos()
            materias = ["Inteligência Artificial", "Robótica", "Artes Digitais", "Arquitetura Sustentável", "Game Design"]
            print("------------------------------")
            matricula_aluno = int(input("\nMatrícula do aluno: "))
            print("\n------------------------------")
            limpar_tela()
            print("\nDisciplinas disponíveis:\n")
            for i, materia in enumerate(materias):
                print(f"{i + 1}. {materia}")
            disciplina = materias[int(input("\nEscolha a disciplina: ")) - 1]
            nota = float(input("\nNota: "))
            data_avaliacao = input("\nData de avaliação (DD-MM-AAAA: ")
            Instituto_Eureka_crud.criar_nota(matricula_aluno, disciplina, nota, data_avaliacao)
            limpar_tela()

        
        elif escolha == '6':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Ler notas\n")
            listar_notas()
        
        elif escolha == '7':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Atualizar nota\n")
            listar_notas()
            id_materia = int(input("\nID da nota a ser atualizada: "))
            matricula_aluno = int(input("\nNova matrícula do aluno: "))
            materias = ["Inteligência Artificial", "Robótica", "Artes Digitais", "Arquitetura Sustentável", "Game Design"]
            print("\nDisciplinas disponíveis:")
            for i, materia in enumerate(materias):
                print(f"{i + 1}. {materia}")
            disciplina = materias[int(input("\nEscolha a nova disciplina: ")) - 1]
            nota = float(input("\nNova nota: "))
            data_avaliacao = input("\nNova data de avaliação (DD-MM-AAAA): ")
            Instituto_Eureka_crud.atualizar_nota(id_materia, matricula_aluno, disciplina, nota, data_avaliacao)
            limpar_tela()

        elif escolha == '8':
            limpar_tela()
            print("------------------------------")
            print("|      Instituto Eureka      |")
            print("------------------------------")
            print("\nVocê escolheu: Deletar nota\n")
            listar_notas()
            id_materia = int(input("\nID da materia a ser deletada: "))
            Instituto_Eureka_crud.deletar_nota(id_materia)
            limpar_tela()
        
        elif escolha == '9':
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
