import random as rand

class Hjälte:
    def __init__(self,Hname , Hhealth, Hattack, Hinventory, Hutrustning ,Hnivå, Hxp):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.inventory = Hinventory
        self.utrustning = Hutrustning
        self.nivå = Hnivå
        self.xp = Hxp


   
    def getall(self):
        print(f"Din hälsa är {self.health} hp ")
        print(f"Din styrka är {self.attack} ")
        print(f"Din level är {self.nivå} ")
        #Funktion som skriver ut dina stats
    
    def setHealth(self, newHealth):
        self.health + newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLvl(self, newNivå):
        self.lvl = newNivå
    #Klassen för spelaren

class Monster:
    def __init__(self, Mname, Mhealth, Mattack):
        self.health = Mhealth
        self.attack = Mattack
        self.name = Mname
    #Klass för monster

def skapah():
    name = str(input("Välj ett namn för din hjälte \n"))
    Hinventory = ["Potion", "Potion", "Potion"]     
    Hutrustning = []
    Player = Hjälte(name, rand.randint(12,22), rand.randint(7,10), Hinventory, Hutrustning ,0, 0 )
    Player.getall()
    return Player
    #Funktion för att skapa sin gubbe

def skapam1():
    monsterna = ["Spöke", "Skelet", "Varg",]
    name = rand.choice(monsterna)
    monster1 = Monster(name, rand.randint(10,15), rand.randint(2,4))
    return monster1
    #Funktion för att skapa monster

def skapam2():
    monsterna = ["Djävul", "Ork", "Vampyr",]
    name = rand.choice(monsterna)
    monster2 = Monster(name, rand.randint(16,22), rand.randint(4,6))
    return monster2
    #Funktion för starkare monster när man når en viss level

def skapaboss():
    monster = Monster("Darkwing", 30, 10)
    return monster
    #Funktion för att skapa den sista bossen

def level(Player):
    Player.xp += rand.randint(10,20)
    if Player.xp < 10:
        Player.nivå = 1
        Player.attack += 1
    elif 10 < Player.xp <20:
        Player.nivå = 2
        Player.health += 2
    elif 20 < Player.xp <30:
        Player.nivå = 3
        Player.attack += 1
    elif 30 < Player.xp < 40:
        Player.nivå = 4
        Player.health += 2
    elif 40 < Player.xp < 50:
        Player.nivå  = 5
        Player.attack += 1
    elif 50 < Player.xp < 60:
        Player.nivå = 6
        Player.health += 2
    elif 60 < Player.xp < 70:
        Player.nivå = 7
        Player.attack += 1
    elif 70 < Player.xp < 80:
        Player.nivå = 8
        Player.health += 2
    elif 80 < Player.xp <90:
        Player.nivå = 9
        Player.attack += 2
    elif Player.xp >= 100:
        Player.nivå = 10
    return Player
    #Funktion för vårt level system
        
def potion(Player):
    p_svar = input("""
Vill du ta en potion?

Tryck [S] för att dricka en styrke potion
------------------------------------------
Tryck [H] för att dricka en healing potion
                    """)
    p_svar = p_svar.lower()
    if p_svar == "h":
        if "Potion" in Player.inventory:
            Player.health += 10
            Player.inventory.remove("Potion")
            print("Du drack en potion och fick 10 hp ")
        else:
            print("Du har inga healing potions ")

    elif p_svar == "s":
        if "Styrka Potion" in Player.inventory:
            Player.attack += 4
            print("Du drack en styrka potion ")
            print(f' Din attack är nu {Player.attack}')
        else: 
            print("Du har inga styrka potions ")
            pass
    #Funktion för att använda potions

    return Player
    
def equip(Player):
    if len(Player.utrustning) == 0:
        print("Du har ingen utrustning att sätta på \n")
        pass
    elif len(Player.utrustning) > 0:
        equip_svar = input("Vill du sätta på utrustning y/n \n ")
        equip_svar = equip_svar.lower()
        if equip_svar == "y":
            print(Player.utrustning)
            equi_svar = input("Svärd = [S] Armor = [A] Lie = [L] Yxa = [Y]")
            equi_svar = equi_svar.lower()
            if equi_svar == "s":
                Player.attack += 5
                Player.utrustning.remove("järn svärd")
                print(f'Din styrka är nu {Player.attack}')
            elif equi_svar == "a":
                Player.health += 10
                Player.utrustning.remove("armor")
                print(f'Din hp är nu {Player.health}')
            elif equi_svar == "l":
                Player.attack += 6
                Player.utrustning.remove("lie")
                print(f'Din styrka är nu {Player.attack}')
            elif equi_svar == "y":
                Player.attack += 6
                Player.utrustning.remove("yxa")
                print(f'Din styrka är nu {Player.attack}')
            else:
                print("Välj ett riktigt alternativ")
    
    return Player
        #Funktion för att sätta på sin utrustning man finner i kistorna


def fight(Player, monster):
    while True:
        if monster.health <= 0:
            print(f"{Player.name} dödade {monster.name}")
            print("Du vann striden")
            Player = level(Player)
            return Player
            


        fight_svar = input(f"Tryck [L] för svag attack, [S] för stark attack eller tryck [P] för att heala. ")
        fight_svar = fight_svar.lower()
        

        if fight_svar == "l":
            Player.attack = Player.attack * 1
            monster.health = monster.health - Player.attack
            if monster.health < 0:
                print(f"Du gjorde {Player.attack} damage, {monster.name} har 0 hp kvar ")
            else:
                print(f"Du gjorde {Player.attack} damage, {monster.name} har {monster.health} hp kvar. ")




        elif fight_svar == "p":
            Player = potion(Player)

        elif fight_svar == "s":
            stark_attack = Player.attack * 1.5
            print(f'Du gick för en stark attack')
            stark_chans = rand.randint(1,4)
            if stark_chans == 3:
                print("Din attack missa")
            elif stark_chans !=3 and monster.health > 0:
                monster.health = monster.health - stark_attack
                print(f'Du gjorde {stark_attack}, {monster.name} har {monster.health} hp kvar. ')
            elif monster.health < 0:
                print(f"Du gjorde {Player.attack} och {monster.name} har 0 hp kvar. ")
        else:
            print("Du förlora din attack")
                
        print("---------------------------------------------------------------------------------------------------------------------------")
        
        if monster.health > 0:  
            dodge_svar = input(f"Tryck [D] för att undvika {monster.name} attack ")
            dodge_svar = dodge_svar.lower()
            print("---------------------------------------------------------------------------------------------------------------------------")

            if dodge_svar != "d":
                print("Felaktig input")
                print("Du missade timing och förlorade chansen att dodga ")
            dodge_chans = rand.randint(1,4)

            if dodge_svar == "d" and dodge_chans == 3:
                print(f"Du dodgade {monster.name}s attack")
                print("---------------------------------------------------------------------------------------------------------------------")
              
            if dodge_svar == "d" and monster.health > 0 and dodge_chans != 3:
                print(f"{monster.name} träffade dig ändå och gjorde {monster.attack} damage, Du har {Player.health} hp kvar")
                Player.health = Player.health - monster.attack
    #Funktion som är vårt fight system där man kan dodgea, heala, öka din attack eller slåss mot monstret.
        

def lotta(Player, monster):
    kista = ["Potion", "Järn svärd", "Armor", "Styrka Potion", "Lie", "Yxa"]
    fällor = ["Det sköts av 8 pillar", "Du andades in giftig rök", "Det kom spjut från golvet", "Du gick i en björn fälla"]
    kista_chans = rand.choice(kista)
    fälla_chans = rand.choice(fällor)
 
    chance = rand.randint(1,5)
    if chance == 1:
        print('Du möttes av en kista \n')
        kista_svar = str(input("Vill du öppna kistan y/n \n"))
        kista_svar.lower()
        if kista_svar == "y":
            print(f"{Player.name} öppnade kistan och hittade " + kista_chans)
            if kista_chans == "Järn svärd":
                Player.utrustning.append("järn svärd")
                print("Järn svärdet ökar din attack med 5 \n")
            elif kista_chans == "Lie":
                Player.utrustning.append("lie")
                print("Lien ökar din attack med 6 \n ")
                kista.remove(kista_chans)
            elif kista_chans == "Yxa":
                Player.utrustning.append("yxa")
                print("Yxan ökar din attack med 6 \n")
            elif kista_chans == "Armor":
                Player.utrustning.append("armor")
                print("Armorn ökar ditt hp med 10 \n")
                kista.remove(kista_chans)
            elif kista_chans == "Styrka Potion":
                Player.inventory.append("Styrka Potion \n")
            elif kista_chans == "Potion":
                Player.inventory.append("Potion \n")

        elif kista_svar == "n":
            print(f"{Player.name} valde att inte öppna kistan och gick vidare")
        else:
            print("Felaktig input")
            pass

        return Player.inventory

    elif chance == 2:
        print("Du möttes av en fälla \n")
        print(fälla_chans)
        Player.health = Player.health - 4
        print("Du tog 4 dmg")
        print(f"Du har {Player.health} hp kvar")
        return Player.health
           
        
        
    elif chance >= 3:
        if Player.nivå <= 5:
            monster = skapam1()
            print(f'Du möttes av en {monster.name}')
            if monster.name == "Varg":
                print("""
                         _
                        / \         _
                      _/|  \-''- _ / \'
                  __-' { |            \'
                        /              \'
                        /       "o.  |o }
                        |            \ ;
                                    ',
                         \_         __\'
                             ''-_    \.//
                               / '-____'
                              /
                            _'
                        _-'

                
                """)
                fight(Player, monster)
            elif monster.name == "Spöke":
                print("""

                    .-----.
                    .' -   - '.
                    /  .-. .-.  \'
                    |  | | | |  |
                    \ \o/ \o/ /
                    _/    ^    \_
                   | \  '---'  / |
                    / /`       `\ \'
                    / /'---` `---'\ \'
                    '.__.       .__.'
                        `|     |`
                        |     \"
                        \      '--.
                        '.        `\'
                            `'---.   |
                            ,__) /
                                `..'


            """)
                fight(Player, monster)
            elif monster.name == "Skelet":
                print(""""

                    
                              ░░░░░░░
                         ░░░░░░░░░░░░░░░░░
                       │░░░░░░░░░░░░░░░░░░░│
                       │░░░░░░░░░░░░░░░░░░░│
                      ░└┐░░░░░░░░░░░░░░░░░┌┘░
                      ░░└┐░░░░░░░░░░░░░░░┌┘░░
                      ░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░
                       ░│██████▌░░░▐██████│░
                       ░│▐███▀▀░░▄░░▀▀███▌│░
                       ─┘░░░░░░░▐█▌░░░░░░░└─
                       ░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░
                         ─┘██▌░░░░░░░▐██└─
                         ░░▐█─┬┬┬┬┬┬┬─█▌░░
                         ░░░▀┬┼┼┼┼┼┼┼┬▀░░░
                          ░░░└┴┴┴┴┴┴┴┘░░░
                            ░░░░░░░░░░░
            """)
                fight(Player, monster)
        else:
            monster = skapam2()
            print(f'Du möttes av en {monster.name}')
        if monster.name == "Ork":
            print("""
            
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\'
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \"
                   /      ,               \,-`\`_,-`\_,..--'\'
                  ,`    ,/,              ,>,   )     \--`````\'
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \'
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (   _  )    (  __  )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo

            """)
    
            fight(Player, monster)
        elif monster.name == "Vampyr":
            print("""
            
                     __.......__
                   .-:::::::::::::-.
                 .:::''':::::::''':::.
                .:::'     `:::'     `:::. 
           .'\  ::'   ^^^  `:'  ^^^   '::  /`.
          :   \ ::   _.__       __._   :: /   ;
         :     \`: .' ___\     /___ `. :'/     ; 
        :       /\   (_|_)\   /(_|_)   /\       ;
         :      / .\   __.' ) ( `.__   /. \      ;
          :      \ (        {   }        ) /      ; 
           :      `-(     .  ^"^  .     )-'      ;
            `.       \  .'<`-._.-'>'.  /       .'
                `.      \    \;`.';/    /      .'
                `._    `-._       _.-'    _.'
                .'`-.__ .'`-._.-'`. __.-'`.
                .'       `.         .'       `.
            .'           `-.   .-'           `.
            """)
            fight(Player, monster)
        elif monster.name == "Djävul":
            print("""
            
                                       ,-.                               
                  ___,---.__          /'|`\          __,---,___          
                ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
            ,'        |           ~'\     /`~           |        `.      
            /      ___//              `. ,'          ,  , \___      \    
            |    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
            |   /          /\_  `   .    |    ,      _/\          \   |   
            \  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
             \  \           | `._   `\\  |  //'   _,' |           /  /      
              `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
                 ``       /     \    ,='/ \`=.    /     \       ''          
                         |__   /|\_,--.,-.--,--._/|\   __|                  
                        /  `./   \\`\ |  |  | /,//' \,'  \                  
                        /   /     ||--+--|--+-/-|     \   \                 
                       |   |     /'\_\_\ | /_/_/`\     |   |                
                        \   \__, \_     `~'     _/ .__/   /            
                        `-._,-'   `-._______,-'   `-._,-'

            """)
            fight(Player, monster)
    #Funktion för olika utfall när man fortsätter gå längre in i grottan.

def vägval(Player, monster):
    väg = str(input("Välj om du vill gå höger [R], vänster [L] eller i mitten [M] \n"))
    väg = väg.lower()
    if väg == "r":
        print(f"{Player.name} gick höger ")
        lotta(Player, monster)
    elif väg == "l":
        print(f"{Player.name} gick vänster ")
        lotta(Player, monster)
    elif väg == "m":
        print(f"{Player.name} gick framåt ")
        lotta(Player, monster)

    return Player
    #Funktion för slumpgöra vad som händer 

def meny():
    Player = skapah()
    Boss = skapaboss()
    monster = skapam1()
    monster = skapam2()
    
    print(f"{player.name} går in i grottan")

    while Player.health > 0:
        if Player.nivå == 10:
            print("Du möttes av en gigantisk drake, för att lämna grottan så måste du besegra den")
            print("""
                            
                                                            _\/
                                                        .-'.'`)
                                                    .-' .'  
                            .                  .-'     `-.          __\/
                                \.    .  |,   _.-'       -:````)   _.-'.'``)
                                \`.  |\ | \.-_.           `._ _.-' .'`
                                __) )__\ |! )/ \_.          _.-'      `.
                            _.-'__`-' =`:' /.' / |      _.-'      -:`````)
                    __.--' ( (@> ))  = \ ^ `'. |_. .-'           `.
                    : @       `^^^    == \ ^   `. |<                `.
                    VvvvvvvvVvvvv)    =  ;   ^  ;_/ :           -:``````)
                    (^^^^^^^^^^=  ==   |      ; \. :            `.
                    ((  `-----------.  == |  ^   ;_/   :             `.
                    /\             /==   /       : \.  :     _..--``````)
                __\ \_          ; ==  /  ^     :_/   :      `.
                ><__   _```---.._/ ====/       ^ : \. :         `.    
                    / / `._  ^  ;==   /  ^        :/ .            `.
                    \/ ((  `._ / === /       ^    `.'       _.--`````)
                    (( /\     ;===  /      ^     .'        `.
                    __\ \_  : === | ^ /                     `. 
                >><__   _``--...__.-'   ^  /  ^              `.
                    / / `._        ^    .'              .--`````)     .--..
                    \/   :=`--...____.-'  ^     .___.-'|            .' .--.`.   (
                    ((    | ===    \                  `.|__.         ; ^:   `.'   )
                            :  ====  \  ^      ^         `. |          ;  `;   `../__
                        .-'\====    \    .       ^      `.|___.       ;^  `;       \'
                        .-'    :  ===   \.-'              ^  `.  |        ;  ^ `;      )
                    .-'    ^   \==== .-'         ^            `.|___.     ;     ;    (
                .-'         ^  :=.-'                 ^        `.   |      ;     ;
                .'      ^       .-'          ^               ^    ;_/__.    ;  ^   ;
                : ^        ^ .-'     ^                   ^   ;     ;   |    ;       ;
                :    ^    .-'    ^          ^      ^     _.-'    ^  ;_/    ; ^      ;
                :  ^    .'                           _.-"    ^      ; \.  ;      ^  ;
                `.   ^ :   ^         ^       ^__.--"               ;_/  ;          ;
                `.^  :                __.--"\         ^     ^    ; \ ;     ^     ;
                    `-.:       ^___.---"\ ===  \   ^               ;_/'        ^  ;
                        ``.^         `.   `\===  \         ^     ^       ^        ;
                        `.     ^    `.   `-. ==\                          ^   ;
                            _`-._        `.    `\= \    ^           ^           ;
                    __..--''    _`-._^     `.    `-.`\         ^          ^    ;
                (-(-(-(-(--''     `-._  ^ `.     `\`\              ^      .'
                                __..---''     `._     `-. ^      ^      ^ .'
                        __..---''    ___....---'`-`)      `---...____..---'
                    (-(-(-(-(---''             '





            """)
            fight(Player, Boss)
            if Boss.health < 0:
                print(f"{Player.name} dödade bossen och klara spelet ")
                break
        
            

        val = str(input("""
        .____________________________________________________________________________________________________________.
        |                                                                                                            |
        | Vad vill du göra, Fortsätt med spelet[F] Öppna inventory [I] Kolla stats [S] Använd potion [P] Avsluta [A] |
        |____________________________________________________________________________________________________________|
        """))
        val = val.lower()
        if val == "i":
            print(Player.inventory)
            print(Player.utrustning)
            player = equip(Player)
        elif val == "s":
            Player.getall()
        elif val == "p":
            Player = potion(Player)
        elif val == "f":
            Player = vägval(Player, monster)
        elif val == "a":
            print("Nu avslutas spelet \n")
            break
        else:
            print("Felaktig input")
    
    else:
        print("Du dog")
        print("Spelet avslutas")
    #Meny är huvudfunktionen som kallar på alla andra funktioner
meny()
