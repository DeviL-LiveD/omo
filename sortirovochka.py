# Часть 2

chastota = 'chacha.txt'
itog = 'itog.txt'

def get_key(item):
    return int(item.split()[2])

with open(chastota, 'r') as f:
    lines = f.readlines()
with open(chastota, 'w') as f:
    f.writelines(lines[1:])

fail = open(chastota)
content = ['{}    {}    {}'.format(s.split()[0],s.split()[1],s.split()[2]) for s in fail.read().split('\n')]
fail.close()

content.sort(key=get_key, reverse=True)

text = ''
fail2 = open(itog, 'w')
for i2n, i in enumerate(content, start=1):
    
    text = '\n{}    {}'.format(i2n, i)
    print(text)
    fail2.write(text)
fail2.close()

with open(itog, 'r') as f:
    lines = f.readlines()
with open(itog, 'w') as f:
    f.writelines(lines[1:])
