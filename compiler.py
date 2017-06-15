from itertools import chain

tokens ={
'SUM' : 'SUM','VALUE':'VALUE','TRUE':'TRUE','FALSE':'FALSE','IF':'IF', '(' : '(', ')' : ')',',':',', '0' : '0', '1' : '1', '2' : '2',
'3' : '3', '4' : '4',  '5' : '5', '6' : '6',
'7' : '7', '8' : '8', '9' : '9'
}

print("My_lovely_Compiler >>>",end='')
string = input()

def Tokens(str):
    try:
        for i in tokens:
            for j in str:
                if(tokens[str] == str):
                    return tokens[str]
    except:
        return False


def Parse(str):
    count = [x.split() for x in str.split(',')]
    count = [x for x in chain(*count)]
    final = []
    
    for i in count:
        if(Tokens(i) != False):
            final.append(Tokens(i))
        else:
            raise NameError('Incorrect Token!')
        
    return final

def Compile(str):
    compiler = Parse(string)
    num = []
    isSum = False
    isValue = False
    isIf = False
    var = 0
    numSum = 0
    varBool = []
    boolIncrement = 0
    for i in compiler:
        if i == 'VALUE':
            if boolIncrement == 0:
                isValue = True
        elif i == 'IF':
            isValue = False
            isIf = True
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
        elif (i == '0' or i == '1'or i == '2'or i == '3'or i == '4'or i == '5'or i == '6'or i == '7'or i == '8'or i == '9'):
            num.append(int(i))


    if isSum == True:
        for element in num:
            if element != var:  
                numSum = numSum + element + var
            isSum = False
        return numSum

    elif isValue == True:
        try:
            var = var + num[0]
            isValue = False
            if isSum == False:
                return var
        except:
            print('No value provided to the variable ')
        
            
    
    elif isValue == False:
        try:
            if isIf == True:
                if boolIncrement > 4:
                    if varBool[1] == True:
                        return varBool[2]
                    else:
                        return varBool[3]
                else:
                    if varBool[0] == True:
                        return varBool[1]
                    else:
                        return varBool[2]
            return varBool[0]
        except:
           print('Provide parameter to the if condition!')
    
    return False

print(Compile(string))
