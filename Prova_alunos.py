
iniciar = 1
alunos=0
notas=[0]
novas_notas =0
gabarito=["A","A","A","A","A","A","A","A","A","A"]

questoes_numeros = [1,2,3,4,5,6,7,8,9,10]

prova=[["1+1=\na)\nb)\nc)\nd)","1+2=\na)\nb)\nc)\nd)","1+3=\na)\nb)\nc)\nd)","1+4=\na)\nb)\nc)\nd)",
        "1+5=\na)\nb)\nc)\nd)","1+6=\na)\nb)\nc)\nd)","1+7=\na)\nb)\nc)\nd)",
        "1+8=\na)\nb)\nc)\nd)","1+9=\na)\nb)\nc)\nd)","1+10=\na)\nb)\nc)\nd)"]]
       
respostas = [[0,0,0,0,0,0,0,0,0,0,0]]

nova_prova=["1+1=\na)\nb)\nc)\nd)","1+2=\na)\nb)\nc)\nd)","1+3=\na)\nb)\nc)\nd)","1+4=\na)\nb)\nc)\nd)",
        "1+5=\na)\nb)\nc)\nd)","1+6=\na)\nb)\nc)\nd)","1+7=\na)\nb)\nc)\nd)",
        "1+8=\na)\nb)\nc)\nd)","1+9=\na)\nb)\nc)\nd)","1+10=\na)\nb)\nc)\nd)"]
       
novas_respostas = [0,0,0,0,0,0,0,0,0,0,0]
            
iniciar = int(input("Deseja iniciar a prova\n1-Sim\n2-Não\n=>"))

    #RECEBE NOME DO ALUNO
while iniciar == 1:
        
    if iniciar == 1:
            nome_aluno=input("Nome do Aluno:\n=> ")
            respostas [alunos][0]=nome_aluno
            print(" ")


        #RECEBE AS RESPOSTAS
        
    for c in range (0,10):
        print("Aluno: {}".format(respostas[alunos][0]) )
        print(" ")
        print("QUESTÃO - {}\n"
        "{}\n".format(questoes_numeros[c],prova[alunos][c]))
        print('')
        resposta=input("Resposta\n=> ")
        respostas [alunos][c+1] = resposta.upper()

        #COMPARA AS RESPOSTAS COM O GABARITO
    for c in range(10):
        if respostas [alunos][c+1] == gabarito[c]:
            notas[alunos] =  notas[alunos] + 1


    reiniciar = int(input("OUTRO ALUNO DESEJA USAR O SISTEMA\n1-SIM\n2-NÃO\n=> "))
    if reiniciar == 1:
            
        alunos = alunos + 1
        respostas.append(novas_respostas)
        prova.append(nova_prova)
        notas.append(novas_notas) 
        iniciar = 1
    else:
        iniciar = 0
else:
        
   print(respostas,notas,alunos)



#quantidade_alunos=len(alunos)
#for l in range