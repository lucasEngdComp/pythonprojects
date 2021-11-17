# Project even or odd
while True:
    try:
        value = int(input('Enter positive number:'))
        if value % 2 == 0:
            print("even value")
        else:
            print("odd value")

    except:
        print('enter only numbers@')
