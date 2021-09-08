#Incrição time de futebol:
altura = float(input("Qual é sua altura?"))
peso = float(input("Qual é seu peso?"))
idade = float(input("Qual sua idade?"))
imc = peso / (altura * altura)
print( "Seu IMC é {}".format(imc))

if (imc > 24.9):
    print("Normalize sua forma fisíca e depois volte a se inscrever.")
elif (imc < 24.9):
    semana = int(input("Quantas vezes você treina por semana?"))
    minutos =int(input("Aproximadamente quantos minutos por sessão de treino?"))
    treino = semana * minutos
    print("Seu tempo de treino na semana é de {}, minutos".format(treino))

if(treino < 300):
    print("Muito obrigado, agredecemos sua participação.")
else:
    print("Parabéns, você passou em todos os nossos testes, agora você fará um teste pessoal em nossa sede, favor comparecer ao endereço: Rua dos Atletas, 43, Bairro do Futebol. Nos vemos lá!")