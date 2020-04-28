# Часть 3

from itertools import groupby
import shutil
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
text_1 = 'detective_for_kidds.txt' # Текст который разбираем на слова
chastoti = 'itog.txt' # Файл отсортированный по частоте 
desyatki = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

f = open(chastoti, 'rb')
U = len(f.readlines())
f.close()

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
        print (n)
        for i in range (n):
            p = morph.parse(stroka_slov[i])
            #print(p,'\n')
            raund = []
            p_tag_nf = []
            for i in range (len(p)):
                #print(p[i],'\n')
                if p[i].tag.POS != None:
                    p_tag_nf = []
                    p_tag_nf.append(p[i].normal_form)
                    p_tag_nf.append(p[i].tag.POS)
                raund.append(p_tag_nf)
            #print('\n+++++\n',p_tag_nf)
            print('\n=====\n',raund)

            # ВОТ ТУТ ИЗБАВЛЯЕМСЯ ОТ ПОВТОРОВ В raund

            # А вот тут начинаем делить
            if len(raund[0]) > 0:
                if len(raund) == 1:
                    cha = open(chastoti)
                    for i in range (U):
                        s_2 = cha.readline()
                        t1_2 = s_2.split()
                        #print(s_2)             ---- ОДНОЗНАЧНЫЕ ----
                        #print(t1_2)
                        #print('si_2[1] -- ',s1_2[1],'raund[0][0] -- ',raund[0][0],'s1_2[2] -- ',s1_2[2],'raund[0][1] -- ',raund[0][1])
                        if t1_2[1] == raund[0][0] and t1_2[2] == raund[0][1]:
                            if int(t1_2[0]) <= 100:
                                desyatki[0][0] += 1
                            if int(t1_2[0]) > 100 and int(t1_2[0]) <= 200:
                                desyatki[1][0] += 1
                            if int(t1_2[0]) > 200 and int(t1_2[0]) <= 300:
                                desyatki[2][0] += 1
                            if int(t1_2[0]) > 300 and int(t1_2[0]) <= 400:
                                desyatki[3][0] += 1
                            if int(t1_2[0]) > 400 and int(t1_2[0]) <= 500:
                                desyatki[4][0] += 1
                            if int(t1_2[0]) > 500 and int(t1_2[0]) <= 600:
                                desyatki[5][0] += 1
                            if int(t1_2[0]) > 600 and int(t1_2[0]) <= 700:
                                desyatki[6][0] += 1
                            if int(t1_2[0]) > 700 and int(t1_2[0]) <= 800:
                                desyatki[7][0] += 1
                            if int(t1_2[0]) > 800 and int(t1_2[0]) <= 900:
                                desyatki[8][0] += 1
                            if int(t1_2[0]) > 900 and int(t1_2[0]) <= 1000:
                                desyatki[9][0] += 1
                            if int(t1_2[0]) > 1000 and int(t1_2[0]) <= 1100:
                                desyatki[10][0] += 1

                            if int(t1_2[0]) > 1100 and int(t1_2[0]) <= 1200:
                                desyatki[11][0] += 1
                            if int(t1_2[0]) > 1200 and int(t1_2[0]) <= 1300:
                                desyatki[12][0] += 1
                            if int(t1_2[0]) > 1300 and int(t1_2[0]) <= 1400:
                                desyatki[13][0] += 1
                            if int(t1_2[0]) > 1400 and int(t1_2[0]) <= 1500:
                                desyatki[14][0] += 1
                            if int(t1_2[0]) > 1500 and int(t1_2[0]) <= 1600:
                                desyatki[15][0] += 1
                            if int(t1_2[0]) > 1600 and int(t1_2[0]) <= 1700:
                                desyatki[16][0] += 1
                            if int(t1_2[0]) > 1700 and int(t1_2[0]) <= 1800:
                                desyatki[17][0] += 1
                            if int(t1_2[0]) > 1800 and int(t1_2[0]) <= 1900:
                                desyatki[18][0] += 1
                            if int(t1_2[0]) > 1900 and int(t1_2[0]) <= 2000:
                                desyatki[19][0] += 1
                            if int(t1_2[0]) > 2000 and int(t1_2[0]) <= 2100:
                                desyatki[20][0] += 1
                                
                            if int(t1_2[0]) > 3100 and int(t1_2[0]) <= 3200:
                                desyatki[21][0] += 1
                            if int(t1_2[0]) > 3200 and int(t1_2[0]) <= 3300:
                                desyatki[22][0] += 1
                            if int(t1_2[0]) > 3300 and int(t1_2[0]) <= 3400:
                                desyatki[23][0] += 1
                            if int(t1_2[0]) > 3400 and int(t1_2[0]) <= 3500:
                                desyatki[24][0] += 1
                            if int(t1_2[0]) > 3500 and int(t1_2[0]) <= 3600:
                                desyatki[25][0] += 1
                            if int(t1_2[0]) > 3600 and int(t1_2[0]) <= 3700:
                                desyatki[26][0] += 1
                            if int(t1_2[0]) > 3700 and int(t1_2[0]) <= 3800:
                                desyatki[27][0] += 1
                            if int(t1_2[0]) > 3800 and int(t1_2[0]) <= 3900:
                                desyatki[28][0] += 1
                            if int(t1_2[0]) > 3900 and int(t1_2[0]) <= 3000:
                                desyatki[29][0] += 1
                            if int(t1_2[0]) > 4000 and int(t1_2[0]) <= 4100:
                                desyatki[30][0] += 1
                    cha.close()
                if len(raund) > 1:
                    n_f = 0
                    ch_r = 0
                    kill = 0
                    nf1_nf, cr1_nf, nf2_nf, cr2_nf = '', '', '', ''
                    nf1_c, cr1_c, nf2_c, cr2_c = '', '', '', ''
                    nf1_2, cr1_2, nf2_2, cr2_2 = '', '', '', ''
                    for i in range (len(raund)-2):
                        if raund[i][0] != raund[i+1][0] and raund[i][1] != raund[i+1][1]:
                            print('нф и чр')
                            kill = 1
                            nf1_2, nf2_2 = raund[i][0], raund[i+1][0]
                            cr1_2, cr2_2 = raund[i][1], raund[i+1][1]
                        elif raund[i][0] == raund[i+1][0] and raund[i][1] != raund[i+1][1]:
                            print('чр')
                            ch_r = 1
                            nf1_c, nf2_c = raund[i][0], raund[i+1][0]
                            cr1_c, cr2_c = raund[i][1], raund[i+1][1]
                        elif raund[i][0] != raund[i+1][0] and raund[i][1] == raund[i+1][1]:
                            print('нф')
                            n_f = 1
                            nf1_nf, nf2_nf = raund[i][0], raund[i+1][0]
                            cr1_nf, cr2_nf = raund[i][1], raund[i+1][1]
                    if kill == 1:
                        print('Однозначный даблкилл')
                        cha = open(chastoti)
                        for i in range (U):
                            s_2 = cha.readline() #              ---- ПО ЧАСТИ РЕЧИ И ПО ЛЕММЕ ----
                            t1_2 = s_2.split()
                            if (t1_2[1] == nf1_2 and t1_2[2] == cr1_2) or (t1_2[1] == nf2_2 and t1_2[2] == cr2_2):
                                if int(t1_2[0]) <= 100:
                                    desyatki[0][3] += 1
                                if int(t1_2[0]) > 100 and int(t1_2[0]) <= 200:
                                    desyatki[1][3] += 1
                                if int(t1_2[0]) > 200 and int(t1_2[0]) <= 300:
                                    desyatki[2][3] += 1
                                if int(t1_2[0]) > 300 and int(t1_2[0]) <= 400:
                                    desyatki[3][3] += 1
                                if int(t1_2[0]) > 400 and int(t1_2[0]) <= 500:
                                    desyatki[4][3] += 1
                                if int(t1_2[0]) > 500 and int(t1_2[0]) <= 600:
                                    desyatki[5][3] += 1
                                if int(t1_2[0]) > 600 and int(t1_2[0]) <= 700:
                                    desyatki[6][3] += 1
                                if int(t1_2[0]) > 700 and int(t1_2[0]) <= 800:
                                    desyatki[7][3] += 1
                                if int(t1_2[0]) > 800 and int(t1_2[0]) <= 900:
                                    desyatki[8][3] += 1
                                if int(t1_2[0]) > 900 and int(t1_2[0]) <= 1000:
                                    desyatki[9][3] += 1
                                if int(t1_2[0]) > 1000 and int(t1_2[0]) <= 1100:
                                    desyatki[10][3] += 1

                                if int(t1_2[0]) > 1100 and int(t1_2[0]) <= 1200:
                                    desyatki[11][3] += 1
                                if int(t1_2[0]) > 1200 and int(t1_2[0]) <= 1300:
                                    desyatki[12][3] += 1
                                if int(t1_2[0]) > 1300 and int(t1_2[0]) <= 1400:
                                    desyatki[13][3] += 1
                                if int(t1_2[0]) > 1400 and int(t1_2[0]) <= 1500:
                                    desyatki[14][3] += 1
                                if int(t1_2[0]) > 1500 and int(t1_2[0]) <= 1600:
                                    desyatki[15][3] += 1
                                if int(t1_2[0]) > 1600 and int(t1_2[0]) <= 1700:
                                    desyatki[16][3] += 1
                                if int(t1_2[0]) > 1700 and int(t1_2[0]) <= 1800:
                                    desyatki[17][3] += 1
                                if int(t1_2[0]) > 1800 and int(t1_2[0]) <= 1900:
                                    desyatki[18][3] += 1
                                if int(t1_2[0]) > 1900 and int(t1_2[0]) <= 2000:
                                    desyatki[19][3] += 1
                                if int(t1_2[0]) > 2000 and int(t1_2[0]) <= 2100:
                                    desyatki[20][3] += 1
                                
                                if int(t1_2[0]) > 3100 and int(t1_2[0]) <= 3200:
                                    desyatki[21][3] += 1
                                if int(t1_2[0]) > 3200 and int(t1_2[0]) <= 3300:
                                    desyatki[22][3] += 1
                                if int(t1_2[0]) > 3300 and int(t1_2[0]) <= 3400:
                                    desyatki[23][3] += 1
                                if int(t1_2[0]) > 3400 and int(t1_2[0]) <= 3500:
                                    desyatki[24][3] += 1
                                if int(t1_2[0]) > 3500 and int(t1_2[0]) <= 3600:
                                    desyatki[25][3] += 1
                                if int(t1_2[0]) > 3600 and int(t1_2[0]) <= 3700:
                                    desyatki[26][3] += 1
                                if int(t1_2[0]) > 3700 and int(t1_2[0]) <= 3800:
                                    desyatki[27][3] += 1
                                if int(t1_2[0]) > 3800 and int(t1_2[0]) <= 3900:
                                    desyatki[28][3] += 1
                                if int(t1_2[0]) > 3900 and int(t1_2[0]) <= 3000:
                                    desyatki[29][3] += 1
                                if int(t1_2[0]) > 4000 and int(t1_2[0]) <= 4100:
                                    desyatki[30][3] += 1
                        cha.close()
                    elif n_f == 1 and kill == 0:
                        print('Начальная форма и только')
                        cha = open(chastoti)
                        for i in range (U):
                            s_2 = cha.readline() #           ---- ПО НАЧАЛЬНОЙ ФОРМЕ ----
                            t1_2 = s_2.split()
                            if (t1_2[1] == nf1_nf and t1_2[2] == cr1_nf) or (t1_2[1] == nf2_nf and t1_2[2] == cr2_nf):
                                if int(t1_2[0]) <= 100:
                                    desyatki[0][2] += 1
                                if int(t1_2[0]) > 100 and int(t1_2[0]) <= 200:
                                    desyatki[1][2] += 1
                                if int(t1_2[0]) > 200 and int(t1_2[0]) <= 300:
                                    desyatki[2][2] += 1
                                if int(t1_2[0]) > 300 and int(t1_2[0]) <= 400:
                                    desyatki[3][2] += 1
                                if int(t1_2[0]) > 400 and int(t1_2[0]) <= 500:
                                    desyatki[4][2] += 1
                                if int(t1_2[0]) > 500 and int(t1_2[0]) <= 600:
                                    desyatki[5][2] += 1
                                if int(t1_2[0]) > 600 and int(t1_2[0]) <= 700:
                                    desyatki[6][2] += 1
                                if int(t1_2[0]) > 700 and int(t1_2[0]) <= 800:
                                    desyatki[7][2] += 1
                                if int(t1_2[0]) > 800 and int(t1_2[0]) <= 900:
                                    desyatki[8][2] += 1
                                if int(t1_2[0]) > 900 and int(t1_2[0]) <= 1000:
                                    desyatki[9][2] += 1
                                if int(t1_2[0]) > 1000 and int(t1_2[0]) <= 1100:
                                    desyatki[10][2] += 1

                                if int(t1_2[0]) > 1100 and int(t1_2[0]) <= 1200:
                                    desyatki[11][2] += 1
                                if int(t1_2[0]) > 1200 and int(t1_2[0]) <= 1300:
                                    desyatki[12][2] += 1
                                if int(t1_2[0]) > 1300 and int(t1_2[0]) <= 1400:
                                    desyatki[13][2] += 1
                                if int(t1_2[0]) > 1400 and int(t1_2[0]) <= 1500:
                                    desyatki[14][2] += 1
                                if int(t1_2[0]) > 1500 and int(t1_2[0]) <= 1600:
                                    desyatki[15][2] += 1
                                if int(t1_2[0]) > 1600 and int(t1_2[0]) <= 1700:
                                    desyatki[16][2] += 1
                                if int(t1_2[0]) > 1700 and int(t1_2[0]) <= 1800:
                                    desyatki[17][2] += 1
                                if int(t1_2[0]) > 1800 and int(t1_2[0]) <= 1900:
                                    desyatki[18][2] += 1
                                if int(t1_2[0]) > 1900 and int(t1_2[0]) <= 2000:
                                    desyatki[19][2] += 1
                                if int(t1_2[0]) > 2000 and int(t1_2[0]) <= 2100:
                                    desyatki[20][2] += 1
                                
                                if int(t1_2[0]) > 3100 and int(t1_2[0]) <= 3200:
                                    desyatki[21][2] += 1
                                if int(t1_2[0]) > 3200 and int(t1_2[0]) <= 3300:
                                    desyatki[22][2] += 1
                                if int(t1_2[0]) > 3300 and int(t1_2[0]) <= 3400:
                                    desyatki[23][2] += 1
                                if int(t1_2[0]) > 3400 and int(t1_2[0]) <= 3500:
                                    desyatki[24][2] += 1
                                if int(t1_2[0]) > 3500 and int(t1_2[0]) <= 3600:
                                    desyatki[25][2] += 1
                                if int(t1_2[0]) > 3600 and int(t1_2[0]) <= 3700:
                                    desyatki[26][2] += 1
                                if int(t1_2[0]) > 3700 and int(t1_2[0]) <= 3800:
                                    desyatki[27][2] += 1
                                if int(t1_2[0]) > 3800 and int(t1_2[0]) <= 3900:
                                    desyatki[28][2] += 1
                                if int(t1_2[0]) > 3900 and int(t1_2[0]) <= 3000:
                                    desyatki[29][2] += 1
                                if int(t1_2[0]) > 4000 and int(t1_2[0]) <= 4100:
                                    desyatki[30][2] += 1
                        cha.close()
                    elif ch_r == 1 and kill == 0:
                        print('часть речи и ни слова больше')
                        print('Однозначный даблкилл')
                        cha = open(chastoti)
                        for i in range (U):
                            s_2 = cha.readline() #         ---- ПО ЧАСТИ РЕЧИ ----
                            t1_2 = s_2.split()
                            if (t1_2[1] == nf1_c and t1_2[2] == cr1_c) or (t1_2[1] == nf2_c and t1_2[2] == cr2_c):
                                if int(t1_2[0]) <= 100:
                                    desyatki[0][1] += 1
                                if int(t1_2[0]) > 100 and int(t1_2[0]) <= 200:
                                    desyatki[1][1] += 1
                                if int(t1_2[0]) > 200 and int(t1_2[0]) <= 300:
                                    desyatki[2][1] += 1
                                if int(t1_2[0]) > 300 and int(t1_2[0]) <= 400:
                                    desyatki[3][1] += 1
                                if int(t1_2[0]) > 400 and int(t1_2[0]) <= 500:
                                    desyatki[4][1] += 1
                                if int(t1_2[0]) > 500 and int(t1_2[0]) <= 600:
                                    desyatki[5][1] += 1
                                if int(t1_2[0]) > 600 and int(t1_2[0]) <= 700:
                                    desyatki[6][1] += 1
                                if int(t1_2[0]) > 700 and int(t1_2[0]) <= 800:
                                    desyatki[7][1] += 1
                                if int(t1_2[0]) > 800 and int(t1_2[0]) <= 900:
                                    desyatki[8][1] += 1
                                if int(t1_2[0]) > 900 and int(t1_2[0]) <= 1000:
                                    desyatki[9][1] += 1
                                if int(t1_2[0]) > 1000 and int(t1_2[0]) <= 1100:
                                    desyatki[10][1] += 1

                                if int(t1_2[0]) > 1100 and int(t1_2[0]) <= 1200:
                                    desyatki[11][1] += 1
                                if int(t1_2[0]) > 1200 and int(t1_2[0]) <= 1300:
                                    desyatki[12][1] += 1
                                if int(t1_2[0]) > 1300 and int(t1_2[0]) <= 1400:
                                    desyatki[13][1] += 1
                                if int(t1_2[0]) > 1400 and int(t1_2[0]) <= 1500:
                                    desyatki[14][1] += 1
                                if int(t1_2[0]) > 1500 and int(t1_2[0]) <= 1600:
                                    desyatki[15][1] += 1
                                if int(t1_2[0]) > 1600 and int(t1_2[0]) <= 1700:
                                    desyatki[16][1] += 1
                                if int(t1_2[0]) > 1700 and int(t1_2[0]) <= 1800:
                                    desyatki[17][1] += 1
                                if int(t1_2[0]) > 1800 and int(t1_2[0]) <= 1900:
                                    desyatki[18][1] += 1
                                if int(t1_2[0]) > 1900 and int(t1_2[0]) <= 2000:
                                    desyatki[19][1] += 1
                                if int(t1_2[0]) > 2000 and int(t1_2[0]) <= 2100:
                                    desyatki[20][1] += 1
                                
                                if int(t1_2[0]) > 3100 and int(t1_2[0]) <= 3200:
                                    desyatki[21][1] += 1
                                if int(t1_2[0]) > 3200 and int(t1_2[0]) <= 3300:
                                    desyatki[22][1] += 1
                                if int(t1_2[0]) > 3300 and int(t1_2[0]) <= 3400:
                                    desyatki[23][1] += 1
                                if int(t1_2[0]) > 3400 and int(t1_2[0]) <= 3500:
                                    desyatki[24][1] += 1
                                if int(t1_2[0]) > 3500 and int(t1_2[0]) <= 3600:
                                    desyatki[25][1] += 1
                                if int(t1_2[0]) > 3600 and int(t1_2[0]) <= 3700:
                                    desyatki[26][1] += 1
                                if int(t1_2[0]) > 3700 and int(t1_2[0]) <= 3800:
                                    desyatki[27][1] += 1
                                if int(t1_2[0]) > 3800 and int(t1_2[0]) <= 3900:
                                    desyatki[28][1] += 1
                                if int(t1_2[0]) > 3900 and int(t1_2[0]) <= 3000:
                                    desyatki[29][1] += 1
                                if int(t1_2[0]) > 4000 and int(t1_2[0]) <= 4100:
                                    desyatki[30][1] += 1
                        cha.close()
                    else:
                        cha = open(chastoti)
                        for i in range (U):
                            s_2 = cha.readline() #       ---- ПО ПАРАМЕТРАМ ----
                            t1_2 = s_2.split()
                            if t1_2[1] == raund[0][0] and t1_2[2] == raund[0][1]:
                                if int(t1_2[0]) <= 100:
                                    desyatki[0][4] += 1
                                if int(t1_2[0]) > 100 and int(t1_2[0]) <= 200:
                                    desyatki[1][4] += 1
                                if int(t1_2[0]) > 200 and int(t1_2[0]) <= 300:
                                    desyatki[2][4] += 1
                                if int(t1_2[0]) > 300 and int(t1_2[0]) <= 400:
                                    desyatki[3][4] += 1
                                if int(t1_2[0]) > 400 and int(t1_2[0]) <= 500:
                                    desyatki[4][4] += 1
                                if int(t1_2[0]) > 500 and int(t1_2[0]) <= 600:
                                    desyatki[5][4] += 1
                                if int(t1_2[0]) > 600 and int(t1_2[0]) <= 700:
                                    desyatki[6][4] += 1
                                if int(t1_2[0]) > 700 and int(t1_2[0]) <= 800:
                                    desyatki[7][4] += 1
                                if int(t1_2[0]) > 800 and int(t1_2[0]) <= 900:
                                    desyatki[8][4] += 1
                                if int(t1_2[0]) > 900 and int(t1_2[0]) <= 1000:
                                    desyatki[9][4] += 1
                                if int(t1_2[0]) > 1000 and int(t1_2[0]) <= 1100:
                                    desyatki[10][4] += 1

                                if int(t1_2[0]) > 1100 and int(t1_2[0]) <= 1200:
                                    desyatki[11][4] += 1
                                if int(t1_2[0]) > 1200 and int(t1_2[0]) <= 1300:
                                    desyatki[12][4] += 1
                                if int(t1_2[0]) > 1300 and int(t1_2[0]) <= 1400:
                                    desyatki[13][4] += 1
                                if int(t1_2[0]) > 1400 and int(t1_2[0]) <= 1500:
                                    desyatki[14][4] += 1
                                if int(t1_2[0]) > 1500 and int(t1_2[0]) <= 1600:
                                    desyatki[15][4] += 1
                                if int(t1_2[0]) > 1600 and int(t1_2[0]) <= 1700:
                                    desyatki[16][4] += 1
                                if int(t1_2[0]) > 1700 and int(t1_2[0]) <= 1800:
                                    desyatki[17][4] += 1
                                if int(t1_2[0]) > 1800 and int(t1_2[0]) <= 1900:
                                    desyatki[18][4] += 1
                                if int(t1_2[0]) > 1900 and int(t1_2[0]) <= 2000:
                                    desyatki[19][4] += 1
                                if int(t1_2[0]) > 2000 and int(t1_2[0]) <= 2100:
                                    desyatki[20][4] += 1
                                
                                if int(t1_2[0]) > 3100 and int(t1_2[0]) <= 3200:
                                    desyatki[21][4] += 1
                                if int(t1_2[0]) > 3200 and int(t1_2[0]) <= 3300:
                                    desyatki[22][4] += 1
                                if int(t1_2[0]) > 3300 and int(t1_2[0]) <= 3400:
                                    desyatki[23][4] += 1
                                if int(t1_2[0]) > 3400 and int(t1_2[0]) <= 3500:
                                    desyatki[24][4] += 1
                                if int(t1_2[0]) > 3500 and int(t1_2[0]) <= 3600:
                                    desyatki[25][4] += 1
                                if int(t1_2[0]) > 3600 and int(t1_2[0]) <= 3700:
                                    desyatki[26][4] += 1
                                if int(t1_2[0]) > 3700 and int(t1_2[0]) <= 3800:
                                    desyatki[27][4] += 1
                                if int(t1_2[0]) > 3800 and int(t1_2[0]) <= 3900:
                                    desyatki[28][4] += 1
                                if int(t1_2[0]) > 3900 and int(t1_2[0]) <= 3000:
                                    desyatki[29][4] += 1
                                if int(t1_2[0]) > 4000 and int(t1_2[0]) <= 4100:
                                    desyatki[30][4] += 1
            print('\n___________________________________________________________\n',desyatki)

            
        print('\n')
    else:
        break
x -=1
fail.close()

print('\n___________________________________________________________\n',desyatki)

g1, g2, g3, g4, g5 = [], [], [], [], []
for i in range (len(desyatki)):
    g1.append(desyatki[i][0])
    g2.append(desyatki[i][1])
    g3.append(desyatki[i][2])
    g4.append(desyatki[i][3])
    g5.append(desyatki[i][4])


print('\n',g1,'\n',g2,'\n',g3,'\n',g4,'\n',g5,'\n') # Вес параметров по сотням

aaa = int(input())
print(aaa)
