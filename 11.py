# Часть 4

# Приводим распределение по сотням к процентам


dec=[[5217, 1423, 814, 741, 476, 371, 318, 332, 260, 179, 212, 210, 148, 150, 160, 163, 122, 108, 105, 103, 128, 50, 46, 46, 53, 52,  61, 59, 61, 53],
     [2024,  618, 111,  40,  16,  14,  14,   6,   5,  17,   1,   4,   1,   8,   3,   7,   2,   4,   2,   2,   3,  3,  9,  1,  1,  1, 125,  0,  0,  1],
     [ 264,   98,  11,  35,  41,  15,  54,  43,  10,   8,  73,  13,   3,   0,   8,   9,   0,   2,  10,   2,   1,  2, 12,  1,  2,  1,   2,  2,  2,  1],
     [2915,  458,  59,  25,  69,  27, 521,  38,  23,  26,   5,   9,  13,  20,  15,  21,   8,  11,  32,   6,   2,  4,  7,  4,  2,  3,   1,  2,  5,  6],
     [3666, 1168, 807, 423, 392, 324, 283, 198, 206, 224, 165, 174, 137, 123, 129, 120, 109,  76,  75,  86,  66, 40, 45, 47, 38, 43,  35, 37, 32, 43]]
sum_dec = [0]*30
for i in range (5):
    sum_dec[0] += dec[i][0]
    sum_dec[1] += dec[i][1]
    sum_dec[2] += dec[i][2]
    sum_dec[3] += dec[i][3]
    sum_dec[4] += dec[i][4]
    sum_dec[5] += dec[i][5]
    sum_dec[6] += dec[i][6]
    sum_dec[7] += dec[i][7]
    sum_dec[8] += dec[i][8]
    sum_dec[9] += dec[i][9]
    sum_dec[10] += dec[i][10]
    sum_dec[11] += dec[i][11]
    sum_dec[12] += dec[i][12]
    sum_dec[13] += dec[i][13]
    sum_dec[14] += dec[i][14]
    sum_dec[15] += dec[i][15]
    sum_dec[16] += dec[i][16]
    sum_dec[17] += dec[i][17]
    sum_dec[18] += dec[i][18]
    sum_dec[19] += dec[i][19]
    sum_dec[20] += dec[i][20]
    sum_dec[21] += dec[i][21]
    sum_dec[22] += dec[i][22]
    sum_dec[23] += dec[i][23]
    sum_dec[24] += dec[i][24]
    sum_dec[25] += dec[i][25]
    sum_dec[26] += dec[i][26]
    sum_dec[27] += dec[i][27]
    sum_dec[28] += dec[i][28]
    sum_dec[29] += dec[i][29]
proc = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
for i in range (5):
    proc[i][0] = (dec[i][0]*100)/sum_dec[0]
    proc[i][1] = (dec[i][1]*100)/sum_dec[1]
    proc[i][2] = (dec[i][2]*100)/sum_dec[2]
    proc[i][3] = (dec[i][3]*100)/sum_dec[3]
    proc[i][4] = (dec[i][4]*100)/sum_dec[4]
    proc[i][5] = (dec[i][5]*100)/sum_dec[5]
    proc[i][6] = (dec[i][6]*100)/sum_dec[6]
    proc[i][7] = (dec[i][7]*100)/sum_dec[7]
    proc[i][8] = (dec[i][8]*100)/sum_dec[8]
    proc[i][9] = (dec[i][9]*100)/sum_dec[9]
    proc[i][10] = (dec[i][10]*100)/sum_dec[10]
    proc[i][11] = (dec[i][11]*100)/sum_dec[11]
    proc[i][12] = (dec[i][12]*100)/sum_dec[12]
    proc[i][13] = (dec[i][13]*100)/sum_dec[13]
    proc[i][14] = (dec[i][14]*100)/sum_dec[14]
    proc[i][15] = (dec[i][15]*100)/sum_dec[15]
    proc[i][16] = (dec[i][16]*100)/sum_dec[16]
    proc[i][17] = (dec[i][17]*100)/sum_dec[17]
    proc[i][18] = (dec[i][18]*100)/sum_dec[18]
    proc[i][19] = (dec[i][19]*100)/sum_dec[19]
    proc[i][20] = (dec[i][20]*100)/sum_dec[20]
    proc[i][21] = (dec[i][21]*100)/sum_dec[21]
    proc[i][22] = (dec[i][22]*100)/sum_dec[22]
    proc[i][23] = (dec[i][23]*100)/sum_dec[23]
    proc[i][24] = (dec[i][24]*100)/sum_dec[24]
    proc[i][25] = (dec[i][25]*100)/sum_dec[25]
    proc[i][26] = (dec[i][26]*100)/sum_dec[26]
    proc[i][27] = (dec[i][27]*100)/sum_dec[27]
    proc[i][28] = (dec[i][28]*100)/sum_dec[28]
    proc[i][29] = (dec[i][29]*100)/sum_dec[29]

for i in range (5):
    for j in range (30):
        proc[i][j] = round(proc[i][j], 2)

for i in range (5):
    print(proc[i])
'''  
import plotly.graph_objects as go

x=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
   'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
   'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX']
fig = go.Figure(go.Bar(x=x, y=proc[0], name='одн'))
fig.add_trace(go.Bar(x=x, y=proc[1], name='чр'))
fig.add_trace(go.Bar(x=x, y=proc[2], name='нф'))
fig.add_trace(go.Bar(x=x, y=proc[3], name='чр+нф'))
fig.add_trace(go.Bar(x=x, y=proc[4], name='парам'))


fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
fig.show()
'''
