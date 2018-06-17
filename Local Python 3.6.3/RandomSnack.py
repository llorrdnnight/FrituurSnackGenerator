import random

#snack = random.choice(open('Snack.txt').readlines())

#Specify filename, amount to generate
filename = 'Snack.txt'
amount = 2

def multiple_random_lines(n):
    for x in range(n):
        string = random.choice(open(filename).readlines())
        print(string)

#print out result
multiple_random_lines(amount)
