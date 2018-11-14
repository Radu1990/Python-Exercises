import time

x = time.time() #this is the current time in seconds since Epoch

seconds = 1

minutes = 60 * seconds

hours = 60 * minutes

day = 24 * hours

#print('Current seconds since Epoch:', x)

days_Epoch = x // day #days since Epoch

#print('Days since Epoch:', days_Epoch)

hours_Epoch = ( x - (days_Epoch * day) ) // hours #hours since Epoch

#print('Hours since Epoch:', hours_Epoch)

minutes_Epoch = ( x - ( (days_Epoch * day) + (hours_Epoch * hours) ) ) // minutes

#print('Minutes since Epoch:', minutes_Epoch)

seconds_Epoch = int ( ( x - ( (days_Epoch * day) + ( hours_Epoch * hours ) + ( minutes_Epoch * minutes ) ) ) %60 )

#print('Seconds since Epoch:', seconds_Epoch)

expression = print('Current GMT Time since Epoch is: \n', days_Epoch, 'days', hours_Epoch, 'hours', minutes_Epoch, 'minutes', seconds_Epoch, 'seconds')
