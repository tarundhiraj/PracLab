#program to show a progress bar
import time





def run():

	print('Starting the progress bar..')
	print('Progress : ',end=' ')
	for i in range(100):
 		print(i , end='')
 		time.delay(1000)


run()
