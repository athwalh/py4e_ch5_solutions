count = 0
total = 0
largest = None
smallest = None

while True:
    sval = input('Enter Number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input!')
        continue
    if largest is None or largest < fval:
        largest = fval


    if smallest is None or smallest > fval:
        smallest = fval

    count = count + 1
    total = total + fval

if count == 0:
    print('You must enter at least 1 input before typing done')
else:
    avg = total / count
    print('Count: ',count)
    print('Total: ',total)
    print('Average: ', avg)
    print('Largest: ', largest)
    print('Smallest: ', smallest)
