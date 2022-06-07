with open ('t.txt') as f:
  data=f.read()
keys=[]
fl=data[data.find('(')+1:data.find(')')].replace(' ','').split(",")
q=1
b=2
k=1
for i in fl:
  keys.append([i,'a'+str(q)])
  q+=1
for i in range (len(data)):
  if data[i] == '=' and data[i-1] not in '+-=*/%' and data[i+1]!='=':
    while data[i-b]!=' ':
      b+=1
    if data[i+1] == '[' or data[i+1:i+3] ==' [':
      keys.append([data[i-b+1:i],'R'+str(k)])
      k+=1
    else:
      keys.append([data[i-b+1:i],'a'+str(q)])
      q+=1  
for i in keys:
  data=data.replace(i[0],i[1])
print(data)
