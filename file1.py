f1=open('abc.txt','w')
f1.write('hello ueser \n')
l=['this is paris \n' , 'this is los angles \n','this is san fransico \n']
f1.writelines(l)
f1.close()

f1=open('abc.txt','r')
print(f1.read())
f1.close()
