from itertools import chain

tokens ={
'SUM' : 'SUM','VALUE':'VALUE','TRUE':'TRUE','FALSE':'FALSE', '(' : '(', ')' : ')',',':',', '0' : '0', '1' : '1', '2' : '2',
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
    var = 0
    numSum = 0
    varBool = False
    for i in compiler:
        if i == 'VALUE':
            isValue = True
        elif i == 'TRUE':
            isValue = False
            varBool = True
        elif i == 'FALSE':
            isValue = False
            varBool = False
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
        var = var + num[0]
        isValue = False
        if isSum == False:
            return var
    
    elif isValue == False:
        return varBool
    
    
    return False

print(Compile(string))
