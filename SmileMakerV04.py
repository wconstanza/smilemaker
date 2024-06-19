import random
import webbrowser
import csv
import time

data = []
url = []

with open('images.csv') as images:
    reader = csv.reader(images)
    for row in reader:
        data.append(row)

cute_cats = [x[0] for x in data]
funny_cats = [x[1] for x in data]
cute_dogs = [x[2] for x in data]
funny_dogs = [x[3] for x in data]
cute_birds = [x[4] for x in data]
funny_birds = [x[5] for x in data]
cute_herptiles = [x[6] for x in data]
funny_herptiles = [x[7] for x in data]
cute_rodents = [x[8] for x in data]
funny_rodents = [x[9] for x in data]
cute_rats = [x[10] for x in data]
funny_rats = [x[11] for x in data]
cute_kids = [x[12] for x in data]
funny_kids = [x[13] for x in data]
memes = [x[14] for x in data]
dark_humor = [x[15] for x in data]
#lit_humor = [x[16] for x in data]

smile = 'n'
play_again = 'y'
while play_again == ('y'):
    url.clear()
    print('Welcome to the Smile Maker! All choices are case sensitive.')
    q1 = input('Which of these do you prefer: Wholesome, Humor ')
    if q1 == ('Wholesome'):
        wholesome = input('Which of these do you prefer: Animals, Kids ')
        if wholesome == ('Animals'):
            animals = input('Which of these do you prefer: Dogs, Cats, or Something Else ')
            if animals == ('Cats'):
                cat_tag = input('Which of these do you prefer: Cute, Funny ')
                if cat_tag == ('Cute'):
                    print('Check your browser for a cute cat')
                    url = cute_cats
                else:
                    print('Check your browser for a funny cat ')
                    url = funny_cats
            elif animals == ('Dogs'):
                dog_tag = input('Which of these do you prefer: Cute, Funny ')
                if dog_tag == ('Cute'):
                    print('Check your browser for a cute dog')
                    url = cute_dogs
                else:
                    print('Check your web browser for a funny dog')
                    url = funny_dogs
            else:
                other_animals = input('Which of these do you prefer: Rodents, Herptiles(Reptiles/Amphibians) ')
                if other_animals == ('Rodents'):
                    rats = input('Are mice and rats okay? (y/n) ')
                    if rats == ('y'):
                        rat_tag = input('Which of these do you prefer: Cute, Funny ')
                        if rat_tag == ('Cute'):
                            print('Check your browser for a cute rat')
                            url = cute_rats
                        else:
                            print('Check your browser for a funny rat')
                            url = funny_rats
                    else:
                        rodent_tag = input('Which of these do you prefer: Cute, Funny ')
                        if rodent_tag == ('Cute'):
                            print('Check your browser for a cute Rodent')
                            url = cute_rodents
                        else:
                            print('Check your browser for a funny Rodent')
                            url = funny_rodents
                else:
                    herp_tag = input('Which of these do you prefer: Cute, Funny ')
                    if herp_tag == ('Cute'):
                        print('Check your browser for a cute Herptile')
                        url = cute_herptiles
                    else:
                        print('Check your browser for a funny Herptile')
                        url = funny_herptiles
                
        else:
            kids = input('Which of these do you prefer: Cute, Funny ')
            if kids == ('Cute'):
                print('Check your web browser for a cute kid')
                url = cute_kids
            else:
                print('Check your web browser for a funny kid')
                url = funny_kids
    else:
        humor = input('Which of these do you prefer: Memes, Dark, Literary ')
        if humor == ('Memes'):
           print('Check your browser for a Meme')
           url = memes
        elif humor == ('Dark'):
            print('Check your browser for some Dark Humor')
            url = dark_humor
        elif humor == ('Literary'):
            url = lit_humor

    links = [x for x in url if len(x.strip()) > 0]
    webbrowser.open(random.choice(links))
    smile = input('Did you smile? (y/n) ')
    if smile == ('n'):
        try_again = input('Would you like to try that choice again? (y/n) ')
        if try_again == ('y'):
            print('Here comes another!')
            webbrowser.open(random.choice(links))
            smile = input('Did you smile? (y/n) ')
        else:
            print('Lets start from the top')
            play_again = ('y') #?
    elif smile == ('y'):
        play_again = input('Glad we could make you smile! Would you like to play again? (y/n) ')

print('Thanks for playing!')        
        
