import os

class Aluno:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def status(self):
        if self.media >= 7:
            self.status = "Aprovado"
        else:
            self.status = "Reprovado"

    def mostra_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        print(f'Média: {self.media}')
        print(f'Status: {self.status}')

os.system("cls")
a1 = Aluno('Marcos', 7.0, 8.0)
a2 = Aluno('João', 8.0, 9.5)
a3 = Aluno('Vinicius', 2.8, 6.5)
a4 = Aluno('Vasconcellos', 7.0, 8.0)
a5 = Aluno('Jota Cê', 8.0, 9.5)
a6 = Aluno('Cecília', 9.8, 6.5)

alu = int(input("Deseja verificar qual aluno? "))

if alu == 1:
    a1.calcular_media()
    a1.status()
    a1.mostra_dados()

elif alu == 2:
    a2.calcular_media()
    a2.status()
    a2.mostra_dados()

elif alu == 3:
    a3.calcular_media()
    a3.status()
    a3.mostra_dados()

elif alu == 4:
    a4.calcular_media()
    a4.status()
    a4.mostra_dados()

elif alu == 5:
    a5.calcular_media()
    a5.status()
    a5.mostra_dados()

elif alu == 6:
    a6.calcular_media()
    a6.status()
    a6.mostra_dados()
    
else:
    print("Aluno não encontrado.")
