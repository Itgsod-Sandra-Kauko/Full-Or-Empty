# asks for a number
# prints if it is even or odd

number = input('Tell me a number')
if number > 90:
    print number, 'is full'

elif number > 59:
    print number, 'is almost full'

elif number > 39:
    print number, 'is half full'

elif number > 9:
    print number, 'is half empty'

elif number < 10:
    print number, 'is empty'



