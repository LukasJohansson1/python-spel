import random as rand

class Hero:
    def __init__(self,Hname , Hhealth, Hattack, Hinventory, Hutrustning ,Hlvl, Hxp):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.inventory = Hinventory
        self.utrustning = Hutrustning
        self.lvl = Hlvl
        self.xp = Hxp


   
    def getall(self):
        print(f"""
        === Spelarstatistik ===
        Namn: {self.name}
        Hälsa: {self.health} HP
        Styrka: {self.attack}
        Level: {self.lvl}
        XP: {self.xp}
        """)

            #Funktion som skriver ut dina stats
        
    def setHealth(self, newHealth):
        self.health += newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLvl(self, newLvl):
        self.lvl = newLvl
        #Klassen för spelaren

class Monster:
    def __init__(self, Mname, Mhealth, Mattack):
        self.health = Mhealth
        self.attack = Mattack
        self.name = Mname
    #Klass för monster

def createH():
    name = str(input("Välj ett namn för din hjälte \n"))
    Hinventory = ["Potion", "Potion", "Potion"]     
    Hutrustning = []
    player = Hero(name, rand.randint(12,22), rand.randint(7,10), Hinventory, Hutrustning ,0, 0 )
    player.getall()
    return player
    #Funktion för att create sin gubbe

def createM1():
    monsterna = ["Spöke", "Skelet", "Varg",]
    name = rand.choice(monsterna)
    monster1 = Monster(name, rand.randint(10,15), rand.randint(2,4))
    return monster1
    #Funktion för att create monster

def createM2():
    monsterna = ["Djävul", "Ork", "Vampyr",]
    name = rand.choice(monsterna)
    monster2 = Monster(name, rand.randint(16,22), rand.randint(4,6))
    return monster2
    #Funktion för starkare monster när man når en viss level

def createboss():
    monster = Monster("Darkwing", 30, 10)
    return monster
    #Funktion för att create den sista bossen

def level(player):
    xp_threshold = 10  
    attack_increase = 1 
    health_increase = 2 
    
    next_level = player.lvl + 1  
    
    if player.xp >= next_level * xp_threshold:
        player.lvl = next_level
        player.xp -= next_level * xp_threshold  # Ta bort förbrukad XP

        # Dynamiska attributuppdateringar
        if player.lvl % 2 == 0:  # Jämna levels förbättrar HP
            player.health += health_increase
        else:  # Ojämna levels förbättrar attack
            player.attack += attack_increase
        
        print(f"{player.name} nådde Level {player.lvl}!")
        print(f"HP: {player.health}, Attack: {player.attack}, XP kvar tills nästa level: {player.xp}")
    
    return player
    #Funktion för level system
        
def potion(player):
    p_svar = input("""
Vill du ta en potion?

Tryck [S] för att dricka en styrke potion
------------------------------------------
Tryck [H] för att dricka en healing potion
                    """)
    p_svar = p_svar.lower()
    if p_svar == "h":
        if "Potion" in player.inventory:
            player.health += 10
            player.inventory.remove("Potion")
            print("Du drack en potion och fick 10 hp ")
        else:
            print("Du har inga healing potions ")

    elif p_svar == "s":
        if "Styrka Potion" in player.inventory:
            player.attack += 4
            print("Du drack en styrka potion ")
            print(f' Din attack är nu {player.attack}')
        else: 
            print("Du har inga styrka potions ")
            pass
    #Funktion för att använda potions

    return player
    
def equip(player):
    if len(player.utrustning) == 0:
        print("Du har ingen utrustning att sätta på \n")
        pass
    elif len(player.utrustning) > 0:
        equip_svar = input("Vill du sätta på utrustning y/n \n ")
        equip_svar = equip_svar.lower()
        if equip_svar == "y":
            print(player.utrustning)
            equi_svar = input("Svärd = [S] Armor = [A] Lie = [L] Yxa = [Y]")
            equi_svar = equi_svar.lower()
            if equi_svar == "s":
                player.attack += 5
                player.utrustning.remove("järn svärd")
                print(f'Din styrka är nu {player.attack}')
            elif equi_svar == "a":
                player.health += 10
                player.utrustning.remove("armor")
                print(f'Din hp är nu {player.health}')
            elif equi_svar == "l":
                player.attack += 6
                player.utrustning.remove("lie")
                print(f'Din styrka är nu {player.attack}')
            elif equi_svar == "y":
                player.attack += 6
                player.utrustning.remove("yxa")
                print(f'Din styrka är nu {player.attack}')
            else:
                print("Välj ett riktigt alternativ")
    
    return player
        #Funktion för att sätta på sin utrustning man finner i kistorna


def fight(player, monster):
    while True:
        if monster.health <= 0:
            print(f"{player.name} dödade {monster.name}")
            print("Du vann striden")

            xp_gained = rand.randint(10, 20)
            player.xp += xp_gained
            print(f"Du fick {xp_gained} XP!")
            
            player = level(player)  # Uppdatera spelarens nivå
            return player
            


        fight_svar = input(f"Tryck [L] för svag attack, [S] för stark attack eller tryck [P] för att heala. ")
        fight_svar = fight_svar.lower()
        

        if fight_svar == "l":
            player.attack = player.attack * 1
            monster.health = monster.health - player.attack
            if monster.health < 0:
                print(f"Du gjorde {player.attack} damage, {monster.name} har 0 hp kvar ")
            else:
                print(f"Du gjorde {player.attack} damage, {monster.name} har {monster.health} hp kvar. ")




        elif fight_svar == "p":
            player = potion(player)

        elif fight_svar == "s":
            stark_attack = player.attack * 1.5
            print(f'Du gick för en stark attack')
            stark_chans = rand.randint(1,4)
            if stark_chans == 3:
                print("Din attack missa")
            elif stark_chans !=3 and monster.health > 0:
                monster.health = monster.health - stark_attack
                print(f'Du gjorde {stark_attack}, {monster.name} har {monster.health} hp kvar. ')
            elif monster.health < 0:
                print(f"Du gjorde {player.attack} och {monster.name} har 0 hp kvar. ")

        while fight_svar not in ["l", "s", "p"]:
            print("Felaktig input, försök igen!")
            fight_svar = input("Tryck [L], [S], eller [P]: ").lower()

                
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
                print(f"{monster.name} träffade dig ändå och gjorde {monster.attack} damage, Du har {player.health} hp kvar")
                player.health = player.health - monster.attack
    #Funktion som är vårt fight system där man kan dodgea, heala, öka din attack eller slåss mot monstret.
        

def lotta(player, monster):
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
            print(f"{player.name} öppnade kistan och hittade " + kista_chans)
            if kista_chans == "Järn svärd":
                player.utrustning.append("järn svärd")
                print("Järn svärdet ökar din attack med 5 \n")
            elif kista_chans == "Lie":
                player.utrustning.append("lie")
                print("Lien ökar din attack med 6 \n ")
                kista.remove(kista_chans)
            elif kista_chans == "Yxa":
                player.utrustning.append("yxa")
                print("Yxan ökar din attack med 6 \n")
            elif kista_chans == "Armor":
                player.utrustning.append("armor")
                print("Armorn ökar ditt hp med 10 \n")
                kista.remove(kista_chans)
            elif kista_chans == "Styrka Potion":
                player.inventory.append("Styrka Potion \n")
            elif kista_chans == "Potion":
                player.inventory.append("Potion \n")

        elif kista_svar == "n":
            print(f"{player.name} valde att inte öppna kistan och gick vidare")
        else:
            print("Felaktig input")
            pass

        return player.inventory

    elif chance == 2:
        print("Du möttes av en fälla \n")
        print(fälla_chans)
        player.health = player.health - 4
        print("Du tog 4 dmg")
        print(f"Du har {player.health} hp kvar")
        return player.health
           
        
        
    elif chance >= 3:
        if player.lvl <= 5:
            monster = createM1()
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
                fight(player, monster)
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
                fight(player, monster)
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
                fight(player, monster)
        else:
            monster = createM2()
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
    
            fight(player, monster)
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
            fight(player, monster)
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
            fight(player, monster)
    #Funktion för olika utfall när man fortsätter gå längre in i grottan.

def vägval(player, monster):
    väg = str(input("Välj om du vill gå höger [R], vänster [L] eller i mitten [M] \n"))
    väg = väg.lower()
    if väg == "r":
        print(f"{player.name} gick höger ")
        lotta(player, monster)
    elif väg == "l":
        print(f"{player.name} gick vänster ")
        lotta(player, monster)
    elif väg == "m":
        print(f"{player.name} gick framåt ")
        lotta(player, monster)

    return player
    #Funktion för slumpgöra vad som händer 

def meny():
    player = createH()
    boss = createboss()
    monster = createM1()
    monster = createM2()
    
    print(f"{player.name} går in i grottan")

    while player.health > 0:
        if player.lvl == 10:
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
            fight(player, boss)
            if boss.health < 0:
                print(f"{player.name} dödade bossen och klara spelet ")
                break
        
            

        val = str(input("""
        .____________________________________________________________________________________________________________.
        |                                                                                                            |
        | Vad vill du göra, Fortsätt med spelet[F] Öppna inventory [I] Kolla stats [S] Använd potion [P] Avsluta [A] |
        |____________________________________________________________________________________________________________|
        """))
        val = val.lower()
        if val == "i":
            print(player.inventory)
            print(player.utrustning)
            player = equip(player)
        elif val == "s":
            player.getall()
        elif val == "p":
            player = potion(player)
        elif val == "f":
            player = vägval(player, monster)
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
