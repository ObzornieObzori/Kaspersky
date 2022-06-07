a=input('Введите название файла: ')
with open (a, 'rb') as f:
  text=str(f.readline())
print(text[2:4])
if text[2:4]=='MZ':
  print('executable, OS Windows')
else:
  print('non-executable')
