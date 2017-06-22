from itertools import chain #import chain function from itertools module

#an tokens dictionary with all valid tokens

tokens ={
'SUM' : 'SUM','SQU':'SQU','VALUE':'VALUE','TRUE':'TRUE','FALSE':'FALSE','IF':'IF','ELSE':'ELSE','FOR':'FOR','EQUALS':'EQUALS', '(' : '(', ')' : ')',',':',', '0' : '0', '1' : '1', '2' : '2',
'3' : '3', '4' : '4',  '5' : '5', '6' : '6',
'7' : '7', '8' : '8', '9' : '9'
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
                if(tokens[strings] == strings):
                    return tokens[strings]
    except:
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

def Compile(strings):
    
    #parses the string and returns the array to compiler
    compiler = Parse(string)
    
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

    #tests for all possibilities just descibed
    for i in compiler:
        if i == 'VALUE':
            if boolIncrement == 0:
                isValue = True
        elif i == 'FOR':
            isValue = False
            isFor = True
        elif i == 'IF':
            isValue = False
            isIf = True
        elif i == 'EQUALS':
            isEqual = True
        elif i == 'ELSE':
            isValue = False
            isIf = True
            isElse = True
        elif i == 'TRUE':
            boolIncrement = boolIncrement + 1
            isValue = False
            varBool.append(True)
        elif i == 'FALSE':
            boolIncrement = boolIncrement + 1
            isValue = False
            varBool.append(False)
        elif i == 'SUM':
            isSum = True
        elif i == 'SQU':
            isSquare = True
        elif (i == '0' or i == '1'or i == '2'or i == '3'or i == '4'or i == '5'or i == '6'or i == '7'or i == '8'or i == '9'):
            num.append(int(i))

    #tests for if you typed SUM, adds all numbers and returns the result
    if isSum == True:
        for element in num:
            if element != var:  
                numSum = numSum + element + var
            isSum = False
        return numSum
    
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
                    elif varBool[0] == True:
                        return varBool[1]
                    elif isElse == True:
                        return varBool[2]
                return varBool[0]
            elif varBool[0] == True:
                return True
            elif varBool[0] == False:
                return False
        except:
           print('Provide parameter to the if condition!')
    
    return False

print(Compile(string))
