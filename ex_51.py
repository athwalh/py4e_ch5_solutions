count = 0
total = 0


while True:
    sval = input('Enter Number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input!')
        continue

    count = count + 1
    total = total + fval

if count == 0:
    print('You must enter at least 1 input before typing done')
else:
    avg = total / count
    print('Count: ',count)
    print('Total: ',total)
    print('Average: ', avg)
