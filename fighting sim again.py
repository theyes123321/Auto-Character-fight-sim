
import random as rd







class armor_piece():
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


class Fighter:
    def __init__(self, name, health, attack, armor=None, speed=0, charisma=0, team=1):
        self.team = team

        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor if armor else []

        self.speed = 0  
        self.charisma = 0

        self.team = team

        self.initiative = rd.randint(1, 20)  # Random initiative for turn order
        if team == 1:
            team1.append(self)
        else:
            team2.append(self)

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0




def random_fighter(team):

    global fighter_num


    fighter_num += 1
    name = f"Fighter{fighter_num}"
    health = rd.randint(50, 100)
    attack = rd.randint(5, 20)
    armor = []
    armor.append(armor_piece("Leather", rd.randint(1, 5)))
    armor.append(armor_piece("Chainmail", rd.randint(5, 10)))
    armor.append(armor_piece("Plate", rd.randint(10, 15)))
    speed = rd.randint(1, 10)
    charisma = rd.randint(1, 10)



    return Fighter(name, health, attack, armor=armor, speed=speed, charisma=charisma, team=team)




def create_teams(num_fighters):
    for i in range(num_fighters):
        random_fighter(1)
        random_fighter(2)






def read_teams(team1, team2):


    print("Team 1 Fighters:")
    for i in range(len(team1)):
        fighter = team1[i]
        print(f"{fighter.name} - Health: {fighter.health}, Attack: {fighter.attack}")
        print(fighter.armor)

    print("\nTeam 2 Fighters:")
    for i in range(len(team2)):
        fighter = team2[i]
        print(f"{fighter.name} - Health: {fighter.health}, Attack: {fighter.attack}")
        print(fighter.armor)





def set_move_que(team1, team2):
    global move_que
    move_que = []
    for fighter in team1 + team2:

        move_que.append(fighter)
    move_que.sort(key=lambda x: x.initiative, reverse=True)  
    





def fight_tick (team1, team2, move_que, tick): 
  

    tick += 1
    print(f"\n--- Tick {tick} ---")
  
    for fighter in move_que:
        if fighter.is_alive():



            if fighter.team == 1:
                opponents = [f for f in team2 if f.is_alive()]
            else:
                opponents = [f for f in team1 if f.is_alive()]

            if opponents:
                target = rd.choice(opponents)
                target.take_damage(fighter.attack)





                if not target.is_alive():

                    print(f"{fighter.name} attacks {target.name} for {fighter.attack} damage! defeating {target.name} ")

                else:

                    print(f"{fighter.name} attacks {target.name} for {fighter.attack} damage! {target.name} now has {target.health} health.")

            else:
                #print(f"Team {fighter.team} wins!")
                return tick



    return tick



team1 = []

team2 = []

fighter_num = 0


create_teams(5)

read_teams(team1, team2)

move_que = []


set_move_que(team1, team2)




tick = 0

while True:
    if not any(f.is_alive() for f in team1):
        print("Team 2 wins the battle!")
        break
    if not any(f.is_alive() for f in team2):
        print("Team 1 wins the battle!")
        break
    tick = fight_tick (team1, team2, move_que, tick)









