up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
down='abcdefghijklmnopqrstuvwxyz'
def UnCesar(t):
    for r in range(1,26):
        rot=[]
        for i in t:
            if i.isupper():
                rot.append(up[(up.index(i)-r)%26])
            elif i.islower():
                rot.append(down[(down.index(i)-r)%26])
            else:
                rot.append(i)
        print('rot ',r,': ',''.join(rot))
UnCesar(input('Введите зашифрованый текст: '))