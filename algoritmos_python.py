#aqui estou implementando um código e respondendo as questões 1, 2 e 3 de Linguagem de Programação Python e
# 1 e 2 de Algoritmos

array1 = []
i = 0

#utilizando um while pra receber, nesse caso, 5 números do usuário
while i < 5:

  #Python 2. exceções
  #espera uma exceção, no caso, inserção de um não número
  try:

    #compondo o array e atualizando o contador
    array1.append(int(input('Digite os números do array'.format(i))))
    i += 1
  
  #caso a exceção(inserir algo != de um número), solicita ao usuário que insira corretamente 
  except: 
     print('Digite NÚMEROS')
    
comprimento = i 

#Algoritmos 1. implementando bubblesort e 
# Algoritmos 2. descrevendo sua eficiencia, algoritmo que ordena e imprime o maior elemento
def ordenador(array, comprimento):
    n = comprimento
    for j in range(n-1):

      #se colocar até n andaria até o último indice
      #-1 vai até o penúlitmo que faz a última comparação realmente necessária
      # trazendo a eficiência de não fazer passagens desnecessárias

      for i in range(n-1):
        #ver se será > para ser movido e comparado com o próximo número
        if array[i] > array[i+1]: #ver se será > para ser movido e comparado com o próximo número

            #no python da pra fazer sem a necessidade de uma variável "auxiliar" para armazenar os valores
            #realizando nas posições de elementos nas posição i e i+1
            array[i], array[i+1] = array[i+1], array[i]

            #com apenas 2 for ordenando o vetor inteiro, sem variáveis desnecessárias

    print("O maior número é",array[-1])
    return array

#instanciando para testar!
teste_ordenador = ordenador(array1, comprimento)
print(teste_ordenador)

#Python 1.calculo da média da lista não ordenada
# utilizando a função do python para somar os valores do vetor e dividindo pela quantidade de itens
print(sum(array1)/comprimento)

#Python 3.contador de palavras
stringteste = "Abobora Batata Cenoura Doce Esquilo"
#já que vai contar as palavras por um espaço, começar com a primeira já considerada
contou = 1 
for i in range(len(stringteste)):
    #onde houver um espaço conta-se +1 palavra
    if stringteste[i] == " ":
        contou += 1
print("Há ",contou," palavras.")

#python já tinha uma função para isso kkkkk
quantas = len(stringteste.split())
print("Há " + str(quantas) + " palavras.")