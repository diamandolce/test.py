#cest le debut de mon apprentissage , je sais que ça va etre dur!!!

name1 = input('Entrez le nom du 1er joueur : ').capitalize()
pv1 = int(input('Et son nombre de PV : '))

name2 = input('Entrez le nom du 2ème joueur : ').capitalize()
pv2 = int(input('Et son nombre de PV : '))

print()

message = name1 + ' (' + str(pv1) + ' PV) affronte ' + name2 + ' (' + str(pv2) + ' PV)'
print('+' * (len(message)+4))
print('+', message, '+')
print('+' * (len(message)+4))

# pour l'instant Ça va.

menu = ''' quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-50 PV)'''

print(name1 + menu)
att1 = input('> ').lower()

if att1 == '1' or att1 == 'charge':
    damages = 20
elif att1 == '2' or att1 == 'tonnerre':
    damages = 50
else:
    print('erreur de saisie')
    damages = 0

pv2 -= damages
print(name1, 'attaque', name2, 'qui perd', damages , 'pv')

print(name2 + menu)
att2 = input('> ').lower()

if att2 == '1' or att2 == 'charge':
    damages = 20
elif att2 == '2' or att2 == 'tonnerre':
    damages = 50
else:
    print('erreur de saisie')
    damages = 0

pv1 -= damages
print(name2, 'attaque', name1, 'qui perd', damages)

if pv1 == pv2:
    print('match nul')
elif pv1 > pv2:
    print(name1, ' remporte le combat')
else:
    print(name2, ' remporte le combat')

