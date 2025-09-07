
import random as rd
import json






class armor_piece():
    def __init__(self, owner_name, type=None, type_bonus=None, material=None, material_bonus=None, body_part=None, enchantments=None):
        self.owner_name = owner_name
        self.owner_history = [self.owner_name]

        if type is None:
            self.type = rd.choice(["Light", "Medium", "Heavy"])
        else:
            self.type = type

        if material is None:
            self.material = rd.choice(["Leather", "Chainmail", "Plate"])
        else:
            self.material = material

        if body_part is None:
            self.body_part = rd.choice(["Helmet", "Chestplate", "Leggings", "Boots", "Gauntlets"])
        else:
            self.body_part = body_part
            
        if enchantments is None:
            self.enchantments = []
        else:
            self.enchantments = enchantments




        self.name = f"{owner_name}'s {self.type} {self.material} {self.body_part}"


        self.defense = rd.randint(1, 10)
        self.weight = rd.randint(1, 10)
        self.durability = rd.randint(1, 10)

        self.stealth = rd.randint(1, 10)
        self.speed = rd.randint(1, 10)

        self.magic_resistance = rd.randint(1, 10)
        self.fire_resistance = rd.randint(1, 10)
        self.ice_resistance = rd.randint(1, 10)
        self.poison_resistance = rd.randint(1, 10)
        self.electric_resistance = rd.randint(1, 10)

        self.enchantment_power = rd.randint(1, 10)
        self.enchantment_duration = rd.randint(1, 10)
        self.enchantment_cooldown = rd.randint(1, 10)
        self.enchantment_cost = rd.randint(1, 10)


        if type_bonus == None:
            light_bonus = rd.randint(1, 7)
            medium_bonus = rd.randint(4, 10)
            heavy_bonus = rd.randint(7, 13)
        else:
            light_bonus = type_bonus
            medium_bonus = type_bonus
            heavy_bonus = type_bonus

        if self.type == "Light":
            
            self.defense    -= light_bonus + rd.randint(1, 3)
            self.weight     -= light_bonus + rd.randint(1, 3)
            self.durability -= light_bonus + rd.randint(1, 3)

            self.stealth += (light_bonus + rd.randint(1, 3)) 
            self.speed   += (light_bonus + rd.randint(1, 3))   

            self.enchantment_power    -= light_bonus + rd.randint(1, 3)   #these are all -ed because light armor is just less armor to enchant
            self.enchantment_duration -= light_bonus + rd.randint(1, 3)
            self.enchantment_cooldown -= light_bonus + rd.randint(1, 3)
            self.enchantment_cost     -= light_bonus + rd.randint(1, 3)
            

        elif self.type == "Medium":
            self.defense    += medium_bonus + rd.randint(1, 3)
            self.weight     += medium_bonus + rd.randint(1, 3)
            self.durability += medium_bonus + rd.randint(1, 3)

            self.stealth -= medium_bonus + rd.randint(1, 3)
            self.speed   -= medium_bonus + rd.randint(1, 3)

            self.enchantment_power    += medium_bonus - rd.randint(1, 3)
            self.enchantment_duration += medium_bonus - rd.randint(1, 3)
            self.enchantment_cooldown += medium_bonus - rd.randint(1, 3)
            self.enchantment_cost     += medium_bonus - rd.randint(1, 3)


        elif self.type == "Heavy":
            self.defense    += heavy_bonus + rd.randint(1, 3)
            self.weight     += heavy_bonus + rd.randint(1, 3)
            self.durability += heavy_bonus + rd.randint(1, 3)

            self.stealth -= heavy_bonus + rd.randint(1, 3)
            self.speed   -= heavy_bonus + rd.randint(1, 3)

            self.enchantment_power    += heavy_bonus + rd.randint(1, 3)
            self.enchantment_duration += heavy_bonus + rd.randint(1, 3)
            self.enchantment_cooldown += heavy_bonus + rd.randint(1, 3)
            self.enchantment_cost     += heavy_bonus + rd.randint(1, 3)




        if material_bonus == None:
            leather_bonus = rd.randint(1, 3)
            chainmail_bonus = rd.randint(4, 6)
            plate_bonus = rd.randint(7, 9)
        else:
            leather_bonus = material_bonus
            chainmail_bonus = material_bonus
            plate_bonus = material_bonus


        if self.material == "Leather":

            self.defense    -= leather_bonus + rd.randint(1, 2)
            self.weight     -= leather_bonus + rd.randint(1, 2)
            self.durability -= leather_bonus + rd.randint(1, 2)

            self.stealth += leather_bonus + rd.randint(1, 2)
            self.speed   += leather_bonus + rd.randint(1, 2)

            self.magic_resistance    += leather_bonus + rd.randint(5, 9) #magic dosen't well on formerly living things
            self.fire_resistance     -= leather_bonus + rd.randint(1, 2) #fire burns leather
            self.ice_resistance      += leather_bonus + rd.randint(1, 2) #ice is cold, and leather is insulating
            self.poison_resistance   -= leather_bonus + rd.randint(1, 2) #poison seeps into leather
            self.electric_resistance += leather_bonus + rd.randint(1, 2) #leather is terrible conductor

            self.enchantment_power    -= leather_bonus - rd.randint(1, 2) #leather is living, and living things have weaker enchants (formerly living)
            self.enchantment_duration -= leather_bonus - rd.randint(1, 2)
            self.enchantment_cooldown += leather_bonus - rd.randint(1, 2)
            self.enchantment_cost     += leather_bonus - rd.randint(1, 2) #leather more exspensive to enchant (again, formerly living)


        elif self.material == "Chainmail":

            self.defense    += chainmail_bonus + rd.randint(1, 2)
            self.weight     += chainmail_bonus + rd.randint(1, 2)
            self.durability += chainmail_bonus + rd.randint(1, 2)

            self.stealth -= chainmail_bonus - rd.randint(3, 6)
            self.speed   -= chainmail_bonus - rd.randint(3, 6)

            self.magic_resistance    += chainmail_bonus + rd.randint(3, 6) 
            self.fire_resistance     += chainmail_bonus + rd.randint(1, 2) 
            self.ice_resistance      -= chainmail_bonus + rd.randint(1, 2) 
            self.poison_resistance   -= chainmail_bonus - rd.randint(2, 4)
            self.electric_resistance -= chainmail_bonus - rd.randint(2, 4)

            self.enchantment_power    += chainmail_bonus - rd.randint(2, 4)
            self.enchantment_duration += chainmail_bonus - rd.randint(2, 4)
            self.enchantment_cooldown += chainmail_bonus - rd.randint(2, 4)
            self.enchantment_cost     += chainmail_bonus - rd.randint(2, 4)

        
        elif self.material == "Plate":

            self.defense    += plate_bonus + rd.randint(5, 10)
            self.weight     += plate_bonus + rd.randint(5, 10)
            self.durability += plate_bonus + rd.randint(5, 10)

            self.stealth -= plate_bonus + rd.randint(7, 10)
            self.speed   -= plate_bonus + rd.randint(7, 10)

            self.magic_resistance    -= plate_bonus + rd.randint(2, 4) 
            self.fire_resistance     -= plate_bonus + rd.randint(1, 4) 
            self.ice_resistance      -= plate_bonus - rd.randint(3, 5) 
            self.poison_resistance   += plate_bonus + rd.randint(3, 5)
            self.electric_resistance -= plate_bonus - rd.randint(3, 5)

            self.enchantment_power    += plate_bonus + rd.randint(3, 7)
            self.enchantment_duration += plate_bonus + rd.randint(3, 7)
            self.enchantment_cooldown += plate_bonus + rd.randint(3, 7)
            self.enchantment_cost     += plate_bonus + rd.randint(3, 7)

    def save_armor(self):
        armor_data = {
            "owner_name": self.owner_name,
            "owner_history": self.owner_history,
            "type": self.type,
            "material": self.material,
            "body_part": self.body_part,
            "enchantments": self.enchantments,
            "name": self.name,
            "defense": self.defense,
            "weight": self.weight,
            "durability": self.durability,
            "stealth": self.stealth,
            "speed": self.speed,
            "magic_resistance": self.magic_resistance,
            "fire_resistance": self.fire_resistance,
            "ice_resistance": self.ice_resistance,
            "poison_resistance": self.poison_resistance,
            "electric_resistance": self.electric_resistance,
            "enchantment_power": self.enchantment_power,
            "enchantment_duration": self.enchantment_duration,
            "enchantment_cooldown": self.enchantment_cooldown,
            "enchantment_cost": self.enchantment_cost
        }
        with open("armor history.json", "a") as file:
            json.dump(armor_data, file)
            

        

            
        








class Fighter:
    def __init__(self, name, name_id, health, attack, armor=None, speed=0, charisma=0, team=1):
        self.team = team

        self.name = name
        self.name_id = name_id
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


def get_name():
    with open("names.txt", "r") as file:
        names = file.readlines()
    return rd.choice(names).strip()



def random_fighter(team):

    global fighter_num


    fighter_num += 1
    fighter_id_name = f"Fighter{fighter_num}"
    fighter_actual_name = get_name()
    health = rd.randint(50, 100)
    attack = rd.randint(5, 20)
    armor = []



    armor.append(armor_piece(fighter_actual_name,body_part="helmet"))
    armor.append(armor_piece(fighter_actual_name,body_part="chestplate"))
    armor.append(armor_piece(fighter_actual_name,body_part="leggings"))
    armor.append(armor_piece(fighter_actual_name,body_part="boots"))
    armor.append(armor_piece(fighter_actual_name,body_part="gauntlets"))
    for piece in armor:
        piece.save_armor()


    speed = rd.randint(1, 10)
    charisma = rd.randint(1, 10)



    return Fighter(fighter_actual_name, fighter_id_name, health, attack, armor=armor, speed=speed, charisma=charisma, team=team)




def create_teams(num_fighters):
    for i in range(num_fighters):
        random_fighter(1)
        random_fighter(2)






def read_teams(team1, team2):


    print("Team 1 Fighters:")
    for i in range(len(team1)):
        fighter = team1[i]
        print(f"{fighter.name} - Health: {fighter.health}, Attack: {fighter.attack}")
        for piece in fighter.armor :
            print(piece.name,)

    print("\nTeam 2 Fighters:")
    for i in range(len(team2)):
        fighter = team2[i]
        print(f"{fighter.name} - Health: {fighter.health}, Attack: {fighter.attack}")
        for piece in fighter.armor :
            print(piece.name,)




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









