
#def functionTest(x):
  #  print('hello', x)

#def main():
  #  var = input("Enter a name\n")
  #  functionTest(var)

#if __name__ == 'main':   # de aflat de ce folosim.
 #   main()





#def calc(*args):
    #print(args[0] + args[1]) # hello + name = helloname
   # print(args[0] - args[1])
  # print(args[0] * args[1]) # hello * 3 = hellohellohello , hello * string = illegal exception
    #print(args[0] / args[1])

#a = 2
#b = 3

#calc(a, b)


#def to_upper(word):
    #return word.upper() #primim rezulatul


#def to_uppercase(word):
    #print(word.upper()) #afisam rezultatul
#to_uppercase('hello')
#print(to_upper('hello'))

#for i in range(3, 5):
    #if i == 4:
        #print('dg')
        #continue # pentru a continua codul
        #break # pentru a opri codul

#def will_be_used_in_future()
    #pass #trece peste fara sa arunce RuntimeException (eroare)



max_hp = 100

player_hp = 100
player_life = 3
player_damage = 25
player_armor = 80
nr_hits = 1

player_name = input('Enter your nickname...\n')


def attack(player_hp, player_damage):
    global player_armor, nr_hits, player_life

    if player_armor - player_damage > 0:
        player_armor = player_armor - player_damage
    else:
        player_hp = player_hp - player_damage
        if player_hp == 0:
            player_life = player_life - 1

    return player_hp

def heal(player_hp, heal):
    global max_hp, player_life

    if player_hp + heal > max_hp:
        player_hp = max_hp
    else:
        player_hp = player_hp + heal
    return player_hp


#for i in range (1,20):
    #if player_hp > 0:
        #player_hp = attack(player_hp, player_damage)
    #else:
        #print('Game Over!')
        #break
    #print("Live ", player_hp)
    #print("Armor", player_armor)
    #print("Hit nr ", nr_hits)
#else:
    #print('Draw')

#print("You are dead.")

for i in range(1, 100):
    if player_hp > 0:
        nr_hits = nr_hits + 1

        if nr_hits % 3 == 0:
            pass
        else:
            player_hp = attack(player_hp, player_damage)
        print("----" + player_name + "----")
        print("Live = ", player_hp)
        print("Armor =", player_armor)
        print("Hits nr =", nr_hits)
    else:
        break

print("You are dead")

