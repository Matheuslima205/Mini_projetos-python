nome = input("Digite um nome: ")
cont = 0
cont_dois = 0


for letra in nome.lower():
    cont_dois += 1
    if (letra == 'a'):
        cont += 1
    elif (letra == 'e'):
        cont += 1
    elif (letra == 'i'):
        cont += 1
    elif (letra == 'o'):
        cont += 1
    elif (letra == 'u'):
        cont += 1


porcentagem = (cont*100)/cont_dois

print ("A) O nome ", nome, "tem", cont, "letras vogais")
print ("B) O nome ", nome, "tem", cont_dois, "caracteres")
print ("C) O nome", nome, "tem", cont, "letras vogais, que correspondem a", 
       porcentagem, "%", " do nome")