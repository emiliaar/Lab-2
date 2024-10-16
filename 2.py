from xml.dom.minidom import parse
dom1 = parse('currency.xml')
file = dom1.toprettyxml()

char_code = ''
nominal = ''
text = ''
flag1 = 0
flag2 = 0
ans=[]

for symb in file:
    text += symb
    if flag1 == 1 and symb =='<':
        flag1 = 0
        char_code = text[:-1]
        text = ''
    if '<CharCode>' in text:
        text = ''
        flag1 = 1

    if flag2 == 1 and symb =='<':
        flag2 = 0
        nominal = text[:-1]
        text = ''
    if '<Nominal>' in text:
        text = ''
        flag2 = 1
    
    if nominal == '10' or nominal == '100':
        ans += [char_code]
    if nominal != '':
        char_code = ''
        nominal = ''
print(ans)