from random import randint

if "__main__" == __name__:
    # you can solve this using a set
    
    numbers = [randint(0, 5) for i in range(7)]
    #  with the array above, leveraging the pigeonhole principle
    # there would always be a duplicate value in the array
    
    seen = set()
    duplicate = False
    for number in numbers:
        if number in seen:
            duplicate = True
            break
        seen.add(number)
    
    if duplicate:
        print('Duplicate exists')
    else:
        print('No duplicates')