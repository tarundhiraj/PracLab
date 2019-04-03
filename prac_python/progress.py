import time



def run(index):
 print('Starting the test..')
 
 print('Progess : 0%', end='')
 print(' [', end='\r')
 bar = '['
 for i in range(index):
  print('Progress : ', end='')
  print(str(i+1) + '% ', end='')
  bar = bar + '='
  if index-1 == i:
   print(bar + '>]', end='\r')
  else:
   print(bar + '>', end='\r')
  time.sleep(1)
 print('')
 print('\nDone.')
  

run(15)
