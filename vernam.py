def vernam(t):
    alph="qwertyuiopasdfghjklzxcvbnm_{}1234567890"
    gamma="thekey"
    ans=''
    g=0
    for i in t:
        ans+=alph[int((alph.index(i)) + int(alph.index(gamma[g%6]))) % 39]
        g+=1
    return ans

print(vernam(input('Введите сообщение: ')))
