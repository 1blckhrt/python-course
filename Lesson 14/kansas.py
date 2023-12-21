from random import choice

capital = 'Topeka'

bird = 'Western Meadowlark'

flower = 'Sunflower'

song = 'Home on the Range'

def randomFunFact():
    funfacts = [
        'Kansas Fact 1',
        'Kansas Fact 2',
        'Kansas Fact 3',
        'Kansas Fact 4'
    ]

    index = choice('0123')

    print(funfacts[int(index)])

if __name__ == "__main__": # MUST INCLUDE
    randomFunFact()