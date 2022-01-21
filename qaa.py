while True:
    print('##### JOGO DE PERGUNTAS E RESPOSTAS #####')

    pontuacao = 0

    question1 = input('Qual a Linguagem mais usada atualmente? \n'
        '\n'
        '1 - JavaScript \n'
        '2 - Python \n'
        '3 - PHP \n'
        '4 - Java \n'
        '\n'
        'Digite o número da resposta: ')
    
    
    question2 = input('##################### \n''O que é um profissional Front-End? \n'
        '\n'
        '1 - É quem cuida do cafézinho \n'
        '2 - É quem desenvolve a interface \n'
        '3 - Profissional que cuida da nuvem \n'
        '4 - É o profissional que cuida do servidor \n'
        '\n'
        'Digite o número da resposta: ')

    question3 = input('##################### \n''O que é IDE? \n'
        '\n'
        '1 - IDE é uma interface onde são desenvolvidos os códigos \n'
        '2 - É a máquina \n'
        '3 - Indice de Envolvimento \n'
        '4 - Servidor da Nuvem \n'
        '\n'
        'Digite o número da resposta: ')

    print('\n'
    '###### RESULTADO ######'
    '\n') 

    if question1 == '1':
        pontuacao = pontuacao + 1
        print('Questão 1 correta!'
        '\n')
    else:
        print('Questão 1 errada!'
        '\n')

    if question2 == '2':
        pontuacao = pontuacao + 1
        print('Questão 2 correta!'
        '\n')
    else:
        print('Questão 2 errada!'
        '\n')

    if question3 == '1':
        pontuacao = pontuacao + 1
        print('Questão 3 correta!'
        '\n')
    else:
        print('Questão 3 errada!'
        '\n')

    print(f'A sua pontuação foi de {pontuacao}!'
    '\n')
    break