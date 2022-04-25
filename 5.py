# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
primeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))

media = round((primeira_nota + segunda_nota) / 2, 2)

if media == 10:
    print("Aprovado com Distinção - média:", media)
elif media >= 7 and media < 10:
    print("Aprovado - média:", media)
else:
    print("Reprovado - média:", media)