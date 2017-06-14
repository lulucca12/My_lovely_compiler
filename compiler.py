from itertools import chain

tokens ={
'SUM' : 'SUM', '(' : '(', ')' : ')',',':',', '0' : '0', '1' : '1', '2' : '2',
'3' : '3', '4' : '4',  '5' : '5', '6' : '6',
'7' : '7', '8' : '8', '9' : '9'
}
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
    numSum = 0
    for i in compiler:
        if i == 'SUM':
            isSum = True
        elif (i == '0' or i == '1'or i == '2'or i == '3'or i == '4'or i == '5'or i == '6'or i == '7'or i == '8'or i == '9'):
            num.append(int(i))
            
    if isSum == True:
        for element in num:
            numSum = numSum + element
            isSum = False
        return numSum
    
    
    return False

print(Compile(string))
