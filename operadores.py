idade = int (input('digite a sua idade em anos '))

if (idade<=3):
    print('sua idade de',idade,' anos é de um bebe')
elif (idade>=4 and idade<=11):
    print('sua idade de',idade,' anos é de uma criança')
elif (idade>=12 and idade<=17):
    print('sua idade de',idade,' anos é de um adolescente')
elif (idade>=18 and idade<60):
    print('sua idade de',idade,' anos é de um adulto')
else:
    print('sua idade de',idade,' anos é de um idoso')       

