
print('#Вывод информаыии о системе')

import os

print("логин:",os.getlogin())
print('path:', os.path)
#print('os.sysconf:',os.sysconf())
sysConf = os.sysconf_names
print('Длинна os.sysconf_names:',len(sysConf), end=' ')
y_n =str( input("Выводим? y n? ")).lower()
if y_n[0]=='y':

  for syConf in sysConf:
     print('os.sysconf_names:',syConf)
     
print('os.name:',os.name)
print('os.system:', os.system)
print('os.cpu_count:',os.cpu_count(),'-количестчо ядер')
#print('pathconf_names:',os.pathconf_names)#какикто переменные среды
#print('sysconf_names:',os.sysconf_names)#какие то переменные среды

dirList = dir(os)
for proc in dirList:
  print(proc)