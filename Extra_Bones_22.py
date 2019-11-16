data = input('Enter temperature data F or C: ')
sign = data[-1]
try:
    data = int(data[0:-1])
except:
    print('You entered a string')

if sign == 'C' or sign == 'c':
    data = round(data * (9/5) + 32)
    print(str(data) + 'F')
elif sign == 'F' or sign == 'f':
    data = round((data - 32) * (5/9))
    print(str(data) + 'C')
else:
    print('Data is not correct')