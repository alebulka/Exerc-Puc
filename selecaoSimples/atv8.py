nota1 = float(input('Digite as nota 1 do 1º bimestre da disciplina: '))
nota2 = float(input('Digite as nota 2 do 1º bimestre da disciplina: '))
nota3 = float(input('Digite as nota 3 do 1º bimestre da disciplina: '))
nota4 = float(input('Digite as nota 4 do 1º bimestre da disciplina: '))

faltas = int(input('Digite o número de faltas: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('Sua média na disciplina foi', media)

pres = 100 - (faltas * 100) / 40
print('Sua porcentagem de presença é de', pres, '%')

if media >= 7 and pres >= 75:
    print('Você está aprovado na disciplina!')
elif media >= 7 and pres < 75:
    print('Você foi reprovado por faltas!')
elif media <=7 and pres >= 75:
    print('Você foi reprovado por nota!')
else:
    print('Você foi reprovado por nota e por faltas!')