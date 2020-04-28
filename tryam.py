# часть 1
from itertools import groupby
import shutil
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
text_1 = 'detective_for_kidds.txt' # Текст который разбираем на слова
chast_rechi = 'cha.txt' # локольный вспомогательный файл
chastota = 'chacha.txt' # Файл промежуточных результатов - используется в следующей части кода


fail = open(text_1)
x = 0
y = 0
stroka_dlya_zapisi = ['','']
while 1 == 1:
    s = fail.readline()
    stroka_slov = s.split()
    x +=1
    if stroka_slov:
        tryam=0
        #print (stroka_slov) #- Творить магию со словами в каждой строчке ТУТ!!!!
        n = len(stroka_slov)
        print (n, 'строка -- ', x)
        for i in range (n):
            p = morph.parse(stroka_slov[i])[0]
            #print(p)
            if p.tag.POS != None:
                stroka_dlya_zapisi[0], stroka_dlya_zapisi[1] = p.normal_form, p.tag.POS
                #print('\n     ', stroka_dlya_zapisi)
                fail2 = open(chast_rechi, "a+")
                #print(stroka_dlya_zapisi[0])
                fail2.write(stroka_dlya_zapisi[0])
                fail2.write('   ')
                fail2.write(stroka_dlya_zapisi[1])
                #fail2.write('   ')
                #fail2.write('1') #- Для числа частоты
                fail2.write('\n')
                fail2.close()
        print('\n')
    else:
        break
x -=1
fail.close()

#fail2 = open(chast_rechi)
#strf = fail2.read()
#print(strf)
#fail2.close()
content = []
fail3 = open(chast_rechi, "r")
#list_schet = ['{} {} {}'.format(s.split('   ')[0], s.split('    ')[1], s.split('    ')[2]) for s in fail2.read().split('\n')]
while 1 == 1:
    s = fail3.readline()
    stroka_pro_slovo = s.split()
    '''
    for i in content:
        print(stroka_pro_slovo)
        print(i)
        if stroka_pro_slovo[0] == i[0]:
            i[2] += 1
        else:
    '''
    content.append(stroka_pro_slovo)
    if stroka_pro_slovo:
        tryam = 0
    else:
        break

fail3.close()
print(content)

print('\n\n\n\n\n')

print(content[2])
sss = content[2]

print(content.count(sss))
content2=[]

from collections import Counter

data = map(tuple, content)
counter = Counter(data)

print(data, '\n')
print(counter)
ccc = list(counter.items())
ccc.pop()
print('\n\n', ccc[0][0][0], ccc[0][0][1], ccc[0][1])
fail4 = open(chastota, "w")
trxt = ''
for i in ccc:
    #print('\n\n', i[0][0], i[0][1], i[1])
    text = '\n{}    {}    {}'.format(i[0][0], i[0][1], i[1])
    '''
    fail4.write(i[0][0])
    fail4.write(i[0][1])
    fail4.write(i[1])
    '''
    fail4.write(text)

fail4.close()
    


'''
content2.append(content[0])
content2[0].append(content.count(content[0]))

content2.append(content[1])
content2[1].append(content.count(content[1]))
content2.append(content[2])
content2[2].append(content.count(content[2]))

print(content2)

for i in range (len(content)-1):
    for j in range (len(content2)-1):
        #print(content2[j][0],' == ', content[i][0],' and ',content2[j][1],' == ',content[i][1])
        if content2[j][0] == content[i][0] and content2[j][1] == content[i][1]:
            #content.pop(i)
            o =1
        else:
            content2.append(content[i])
            content2[i].append(content.count(content[i]))
print(content2)
print(content)
'''
