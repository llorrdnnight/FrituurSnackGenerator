import random

#Specify filename
file= ['curryworst special','loempia','boulet','lucifer', 'berepoot', 'fishstick', 'chicken fingers', 'mini lucifer', 'curryworst', 'servela special', 'frikandel', 'frikandel special', 'viandel', 'brochette', 'lookworst', 'kip nuggets', 'bitterballen', 'kipknots', 'zigeunerstick', 'vleeskroket', 'mexicano', 'bamischijf', 'mozzarella stick', 'twijfelaar', 'stoofvlees', 'kraker', 'sitostick']
#specify amount of snacks to generate
amount = 2

def multiple_random_lines(n):
    for x in range(n):
        string = random.choice((file))
        print(string)

#print out result
multiple_random_lines(amount)
