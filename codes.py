'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):
    # write your code in Python 3.6
    testList = list(range(100000))
    for i in range(1, len(testList)):
        if(testList[i] not in A): 
            return(i)
    return 0
'''

'''
SELECT participation.name
FROM participation
    JOIN 
    (SELECT name, year
    FROM participation
    ) AS tmp1 
    ON participation.name = tmp1.name AND participation.year+1= tmp1.year
    JOIN 
    (SELECT name, year
    FROM participation
    ) AS tmp2 
    ON participation.name = tmp2.name AND participation.year+2= tmp2.year
GROUP BY participation.name
ORDER BY participation.name ASC


'''

'''

def solution(S):
    # write your code in Python 3.6
    operations = list(S.split(" "))
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