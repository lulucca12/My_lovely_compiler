import re
from itertools import chain #import chain function from itertools module

#an tokens dictionary with all valid tokens

tokens ={
'SUM' : 'SUM','SQUARE':'SQUARE','VALUE':'VALUE','TRUE':'TRUE','FALSE':'FALSE','IF':'IF','INDEXTOKEN':'INDEXTOKEN',
'ELSE':'ELSE','FOR':'FOR','EQUALS':'EQUALS','AND':'AND','OR':'OR','NOT':'NOT','COMPILE':'COMPILE',
'(' : '(', ')' : ')',',':','
}

#prints the prompt and puts the end at the same line
print("My_lovely_Compiler >>>",end='')

#the string input from the prompt
string = input()

#function Tokens that recieves a string and verifies if it is valid
#if so returns it self
#else returns false

def Tokens(strings):
    try:
        for i in tokens:
            for j in strings:
                if(tokens[strings]):
                    return tokens[strings]
    except:
        for i in tokens:
            for j in strings:
                if(re.match(r"\d+", strings)):
                    return strings
                elif(re.match(r"\w+", strings)):
                    return strings
        return False


#parses the string recieved verifiying if it is valid with the token function
#if it is removes all non-token characters(whitespaces,commas,parentesis,etc)
#and returns an arrays with the result
#else it raises an NameError saying that the token was not valid
    
def Parse(strings):
    
    #removes whitespaces and commas
    count = [x.split() for x in strings.split(',')]
    
    #chains the array leaving it in the outside array
    count = [x for x in chain(*count)]
    
    #the final array that will be returned
    final = []

    
    for i in count:
        
        #if the token is valid
        if(Tokens(i) != False):
            
            #append it in the arrray
            final.append(Tokens(i))

        #else raises an error
        else:
            raise NameError('Incorrect Token!')

    #returns the result    
    return final

def Compile(strings,toCompile):
    
    #parses the string and returns the array to compiler
    if(toCompile == True):
        compiler = Parse(strings)
    
    #numbers array, stores all numbers
    num = []

    #if you type SUM evaluates to TRUE
    isSum = False
    
    #if you type SUM evaluates to TRUE
    isValue = False
    
    #if you type SUM evaluates to TRUE
    isIf = False
    
     #if you type SUM evaluates to TRUE
    isElse = False
    
     #if you type SUM evaluates to TRUE
    isFor = False

    #if you type VALUE next to a number saves it here
    var = 0

    #the sum of all numbers in the SUM command
    numSum = 0

    #what will be returned if you type FOR next to 2 numbers
    varFor = ''

    #the array that stores all boolean values
    varBool = []

    #a counter for the number of boolean values
    boolIncrement = 0

    #is True if you typed EQUALS
    isEqual = False

    #is True if you typed SQU and stores in numSquare
    isSquare = False
    numSquare = 1

    #is True if you typed AND
    isAnd = False

    #is True if you typed OR
    isOr = False

    #is True if you typed NOT
    isNot = False

    #is True if you typed COMPILE
    isCompile = False

    #is True if you typed INDEXTOKEN
    isIndex = False
    index = 0
    tokenIndex = 0
    
    #tests for all possibilities just descibed
    for i in compiler:
        if i == 'COMPILE':
            isCompile = True
            with open("compile.txt","r") as file:
                string = file.read()
                break
        if i == 'INDEXTOKEN':
            if tokenIndex != 0:
                tokenIndex = tokenIndex + 1
            isIndex = True
        if i == 'VALUE':
            tokenIndex = tokenIndex + 1
            if boolIncrement == 0:
                isValue = True
        elif i == 'FOR':
            tokenIndex = tokenIndex + 1
            isValue = False
            isFor = True
        elif i == 'IF':
            tokenIndex = tokenIndex + 1
            isValue = False
            isIf = True
        elif i == 'EQUALS':
            tokenIndex = tokenIndex + 1
            isEqual = True
        elif i == 'AND':
            tokenIndex = tokenIndex + 1
            isAnd = True
        elif i == 'OR':
            tokenIndex = tokenIndex + 1
            isOr = True
        elif i == 'NOT':
            tokenIndex = tokenIndex + 1
            isNot = True
        elif i == 'ELSE':
            tokenIndex = tokenIndex + 1
            isValue = False
            isIf = True
            isElse = True
        elif i == 'TRUE':
            tokenIndex = tokenIndex + 1
            if isNot == False:
                boolIncrement = boolIncrement + 1
                isValue = False
                varBool.append(True)
            else:
                boolIncrement = boolIncrement + 1
                isValue = False
                varBool.append(False)
                isNot = False
        elif i == 'FALSE':
            tokenIndex = tokenIndex + 1
            if isNot == False:
                boolIncrement = boolIncrement + 1
                isValue = False
                varBool.append(False)
            else:
                boolIncrement = boolIncrement + 1
                isValue = False
                varBool.append(True)
                isNot = False
        elif i == 'SUM':
            tokenIndex = tokenIndex + 1
            isSum = True
        elif i == 'SQUARE':
            tokenIndex = tokenIndex + 1
            isSquare = True
        elif (re.match(r"\d+", i)):
            tokenIndex = tokenIndex + 1
            num.append(int(i))
            if isIndex == True:
                index = int(i)
                isIndex = False

    if isCompile == False:
        #tests for if you typed SUM, adds all numbers and returns the result
        if isSum == True:
            for element in num:
                if element != var:  
                    numSum = numSum + element + var
                isSum = False
            return numSum
        
        if isIndex == True:
            compiler[tokenIndex] = compiler[index]
            string = compiler
##            string.remove(str(index))
##            num.remove(index)
            return Compile(string, False)
        
        #tests if you typed VALUE and returns the value you typed saving it to a variable
        #if no value provided throws an exception(printing it to the screen)
        elif isValue == True and isIf == False:
            try:
                var = var + num[0]
                isValue = False
                if isSum == False and isSquare == False:
                    return var
            except:
                print('No value provided to the variable ')

        #tests if you typed SQU and returns the square of all elements
        if isSquare == True:
            if isValue == True:
                for element in num:
                    numSquare = numSquare * (var * var)
                return numSquare
            else:
                for element in num:
                    numSquare = numSquare * (element * element)
                return numSquare

        #tests if you typed FOR and not SUM
        #then returns the value you typed how many times you like
        #thows exception for no parameters
        elif isFor == True and isSum == False:
            try:
                for i in range(num[0]):
                    varFor = varFor +' '+ str(num[1])
                return varFor
                    
            except:
                print ('No value provided to the for')
                
        #tests if its not a variable and you typed IF
        #if so return the value based on the parameters(bugy)
        #throws exception for no parameters
        elif isValue == False:
            try:
                if isIf == True: 
                    if boolIncrement > 4:
                        if varBool[1] == True:
                            return varBool[2]
                        elif isElse == True:
                            return varBool[3]
                    else:
                        if isEqual == True:
                            if(num[0] == num[1]):
                                return varBool[0]
                            elif isElse == True:
                                return varBool[1]
                        elif isAnd == False and isOr == False:
                            if varBool[0] == True:
                                return varBool[1]
                            elif isElse == True:
                                return varBool[2]
                        elif isAnd == True:
                            if varBool[0] == True and varBool[1] == True:
                                return varBool[2]
                            elif isElse == True:
                                return varBool[3]
                        elif isOr == True:
                            if varBool[0] == True or varBool[1] == True:
                                return varBool[2]
                            elif isElse == True:
                                return varBool[3]
                                
                    return varBool[0]
                elif boolIncrement >= 1:
                    if varBool[0] == True:
                        return True
                    elif varBool[0] == False:
                        return False
            except:
               print('Provide parameter to the if condition!')
        
        return None
    else:
        print(Compile(string, True))

print(Compile(string, True))
