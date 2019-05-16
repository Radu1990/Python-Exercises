import time

# this is the current time in seconds since Epoch
x = time.time()

seconds = 1

minutes = 60 * seconds

hours = 60 * minutes

day = 24 * hours

# days since Epoch
days_Epoch = x // day

# hours since Epoch
hours_Epoch = (x - (days_Epoch * day)) // hours

minutes_Epoch = (x - ((days_Epoch * day) + (hours_Epoch * hours))) // minutes

seconds_Epoch = int((x - ((days_Epoch * day) + (hours_Epoch * hours) + (minutes_Epoch * minutes))) % 60)

print('Current GMT Time since Epoch is: \n', days_Epoch, 'days',
      hours_Epoch, 'hours', minutes_Epoch, 'minutes', seconds_Epoch, 'seconds')
