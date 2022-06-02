alph='abcdefghijklmnopqrstuvwxyz'
def replace(num):
    ans=''
    num=num[num.find('{')+1:-1].split('|')
    for i in num:
        ans+=alph[int(i)-1]
    return ans
print(replace(input('Введите зашифрованное сообщение:')))
