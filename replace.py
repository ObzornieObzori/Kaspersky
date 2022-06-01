alph='abcdefghijklmnopqrstuvwxyz'
def replace(t):
    ans=''
    t=t.split('|')
    print(t)
    for i in t:
        ans+=alph[int(i)-1]
    print(ans)
replace(input('Введите зашифрованное сообщение:'))