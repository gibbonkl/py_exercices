'''
Função que recebe um array (de tamanho entre 1 e 100000) de inteiros (entre -1 milhão e +1 milhão) e retorna o menor positivo, maior que zero, não contido no array.
int_list = [2, 4, 6, 1, 2] saída 3
int_list = [0, 1, 2, 3] saída 4
int_list = [−2, −4] saída 1
'''
def solution(int_list):
    testList = list(range(100000))
    for i in range(1, len(testList)):
        if(testList[i] not in int_list): 
            return(i)
    return 0

'''
Função calculadora string: Sempre usa o conceito de pilha, primeiro a entrar é o último a sair, recebe como parâmetro uma string com números e operações separados por espaço e retorna um número com o resultado ou um erro -1
DUP duplica o último número
POP remove o último número
- subtrai os dois números anteriores e os substitui pelo resultado
+ soma os dois números anteriores e os substitui pelo resultado
'''
def solution(str_in):
    operations = list(str_in.split(" "))
    intStack = []

    for i in range(len(operations)):
        if ((len(intStack)<1 and (operations[i] == "DUP" or operations[i] == "POP")) or (len(intStack)<2 and (operations[i] == "-" or operations[i] == "+"))):
            return -1
        elif (operations[i] == "DUP"): intStack.append(intStack[-1])
        elif (operations[i] == "POP"): intStack.pop()
        elif (operations[i] == "-"): intStack.append(intStack.pop()-intStack.pop())
        elif (operations[i] == "+"): intStack.append(intStack.pop()+intStack.pop())
        else: intStack.append(int(operations[i]))
                  
    if (intStack[-1]):
        return intStack[-1]
    else: 
        return -1  