print('Enter Number: ')

number = ''
try:
    number=int(input())

    while number!=1 :
        if number%2==0 :
            number = number //2
        else:
            number = 3*number+1
        print(number)

except:
    print('input must be an integer')
