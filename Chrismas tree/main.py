b = 34
c = 0
while b> 0 and c <33 :
    print('\33[1;32;48m'+' '*b+'*'+'*'*c+'\33[0m')
    b-= 1
    c+= 2
for r in range(3):
    print(' '*33,'||')
print(' '*32, end = '\====/')
print('')