
print('{0},{1},{3}'.format('apple','banana','carrat','mango'))
apple,banana,mango
print('{0},{1},{3}{2}{5}'.format('apple','banana','carrat','mango'))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print('{0},{1},{3}{2}{5}'.format('apple','banana','carrat','mango'))
IndexError: Replacement index 5 out of range for positional args tuple
print('{0},{1},{3}{2}{0}'.format('apple','banana','carrat','mango'))
apple,banana,mangocarratapple
print('{0},{1},{3}{1}{3}{0}{2}'.format('apple','banana','carrat','mango'))
apple,banana,mangobananamangoapplecarrat
print('{0},{1},{3} {1}  {3}  {0}   {2}'.format('apple','banana','carrat','mango'))
apple,banana,mango banana  mango  apple   carrat
print('{0},{1},{3} {1}  {3}  {0}   {2}'.format('apple','banana','carrat','mango'))
apple,banana,mango banana  mango  apple   carrat
print('{0},{1},{3}'.format('prabha','anju','prasad','reddy'))
prabha,anju,reddy
print('{0},{1},{3}{2}{1}{3}{0}{0}'.format('prabha','anju','prasad','reddy'))
prabha,anju,reddyprasadanjureddyprabhaprabha

