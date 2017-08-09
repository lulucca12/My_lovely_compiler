import re
from itertools import chain #import chain function from itertools module

#an tokens dictionary with all valid tokens

tokens ={
'SUM' : 'SUM','SQUARE':'SQUARE','VALUE':'VALUE','TRUE':'TRUE','FALSE':'FALSE',
'IF':'IF','INDEXTOKEN':'INDEXTOKEN','ELSE':'ELSE','FOR':'FOR','EQUALS':'EQUALS',
'AND':'AND','OR':'OR','NOT':'NOT','IMPORT':'IMPORT','REMOVEINDEX':'REMOVEINDEX',
'FUNCTION':'FUNCTION','START':'START','END':'END','PRINT':'PRINT','PARAMETER':'PARAMETER',
'PRODUCT':'PRODUCT',
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
                if(re.match(r"^-*[0-9,\.]+$", strings)):
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

    #if you typed FUCNTION evaluates to TRUE
    isFunction = False
    compileFunction = Parse(strings)
    #compileReference = []
    removeCompiler = False
    isEnd = False
    excecutionNameFunction = ""
    typedStart = False
    typedEnd = False
    defineNameFunction = ""
    indexStart = 0
    ReturnFunction = ""
    parameterName = ""
    parameterValue = ""
    parameterString = ""
    isParameter = False
    
    #if you type SUM evaluates to TRUE
    isSum = False
    
    #if you typed PRODUCT evaluates to TRUE
    isProduct = False
    varProduct = 1
    
    #if you type VALUE evaluates to TRUE
    isValue = False
    
    #if you type IF evaluates to TRUE
    isIf = False
    
     #if you type ELSE evaluates to TRUE
    isElse = False
    
    #if you type FOR evaluates to TRUE
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

    #is True if you typed IMPORT
    isImport = False
    importValue = ""
    importString = ""
    importStringTester = True

    #is True if you typed INDEXTOKEN
    isIndex = False
    index = 0
    tokenIndex = 0

    #is True if you typed REMOVEINDEX
    isRemove = False

    #is True if you typed PRINT
    isPrint = False

    #strings array
    names = []
    
    #tests for all possibilities just descibed
    for i in compiler:
        if i == 'IMPORT':
            isImport = True
        elif i == 'FUNCTION':
            tokenIndex = tokenIndex + 1
            isFunction = True
        elif i == 'PARAMETER':
            isParameter = True
        elif i == 'START':
            typedStart = True
        elif i == 'END':
            typedEnd = True
        elif i == 'REMOVETOKEN':
            tokenIndex = tokenIndex + 1
            isRemove = True
        elif i == 'INDEXTOKEN':
            if tokenIndex != 0:
                tokenIndex = tokenIndex + 1
            isIndex = True
        elif i == 'VALUE':
            tokenIndex = tokenIndex + 1
            if boolIncrement == 0:
                isValue = True
        elif i == 'FOR':
            tokenIndex = tokenIndex + 1
            isValue = False
            isFor = True
        elif i == 'PRINT':
            isPrint = True
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
        elif i == 'PRODUCT':
            tokenIndex = tokenIndex + 1
            isProduct = True
        elif i == 'SQUARE':
            tokenIndex = tokenIndex + 1
            isSquare = True
        elif (re.match(r"^-*[0-9,\.]+$", i)):
            tokenIndex = tokenIndex + 1
            num.append(float(i))
            if isIndex == True:
                index = float(i)
                isIndex = False
            elif isRemove == True:
                index = float(i)
                isRemove = False    
        elif(re.match(r"\w+", i)):
            names.append(str(i))
            if isFunction == True:
                if typedStart == True and typedEnd == True:
                    excecutionNameFunction = str(i)
                #print(i);
                elif typedStart == False and typedEnd == False:
                    #print(i)
                    defineNameFunction = str(i)
            if isImport == True and importStringTester == True:
                importValue = str(i)
                importStringTester = False
                
    if isImport == False:
        '''
The function works by separating whats in the block of code(START, END) and whats not(else) and compiling whats inside and
replacing its value with the calling of the function 

        '''
        if isFunction == True:
            isFunction = False

            compiler = Parse(strings)
            del compiler[compiler.index('FUNCTION'):compiler.index('END')+1]

            indexStart = compileFunction.index('START')
            del compileFunction[0:compileFunction.index('FUNCTION') + 2]
            compileFunction.pop(indexStart - 2)
            if compileFunction[-1] != 'END':
                del compileFunction[compileFunction.index('END') : compileFunction.index(compileFunction[-1]) + 1]
            else:
                compileFunction.remove('END')

            if isParameter == True:
                isParameter = False
                try:
                    parameterName = compileFunction[compileFunction.index('PARAMETER') + 1]
                    if excecutionNameFunction != '':
                        parameterValue = compiler[compiler.index(excecutionNameFunction) + 1]
                        del compiler[compiler.index(excecutionNameFunction) + 1]
                        compileFunction.pop(compileFunction.index('PARAMETER') + 1)
                        compileFunction.pop(compileFunction.index('PARAMETER'))
                        for i in compileFunction:
                            if i == parameterName:
                                parameterString = ' '.join(compileFunction)
                                parameterString = parameterString.replace(parameterName, parameterValue)
                                compileFunction = parameterString.split()
                    else:
                        compileFunction.pop(compileFunction.index('PARAMETER') + 1)
                        compileFunction.pop(compileFunction.index('PARAMETER'))
            
                except:
                    print('provide parameter value')
     
            ReturnFunction = str(Compile(' '.join(compileFunction), True))
        
            for i in compiler:
                if i == excecutionNameFunction:
                    compiler[compiler.index(i)] = ReturnFunction.upper()

            if(int(' '.join(compiler)) is not None):
                
                return int(' '.join(compiler))
            
            else:
                
                return Compile(' '.join(compiler) , True)

        #tests for if you typed SUM, adds all numbers and returns the result
            #return
        if isSum == True:
            for element in num:
                if element != var:  
                    numSum = numSum + element + var
                isSum = False
            return numSum

        elif isProduct == True:
            for i in range(int(compiler[compiler.index('PRODUCT') + 2]) + 1):
                if i >= int(compiler[compiler.index('PRODUCT') + 1]):
                    varProduct = varProduct * i
            return varProduct
            
        elif isRemove == True:
            compiler.pop(index)
            string = compiler
            return Compile(string,False)
        
        elif isIndex == True:
            compiler[tokenIndex] = compiler[index]
            string = compiler
##            string.remove(str(index))
##            num.remove(index)
            index = 0
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


        elif isPrint == True:
            print(compiler[compiler.index('PRINT') + 1])
            
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
        try:
            isImport = False
            with open(importValue+".txt","r") as file:
                    importString = file.read()

            compiler[compiler.index('IMPORT') + 1] = ' '
            compiler[compiler.index('IMPORT')] = ' ' + importString
            #print(compiler)
            return Compile(' '.join(compiler), True)
        except:
            print("No file found, be sure that it is on the same directory as the compiler and that it has the same name")
print(Compile(string, True))
