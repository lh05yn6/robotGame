"""
     ██╗██╗  ██╗ ██████╗ ███████╗███████╗██╗     ██╗███╗   ██╗         ██╗██╗  ██╗ ██████╗ ███████╗███████╗██╗     
     ██║██║  ██║██╔═══██╗██╔════╝██╔════╝██║     ██║████╗  ██║         ██║██║  ██║██╔═══██╗██╔════╝██╔════╝██║     
     ██║███████║██║   ██║███████╗█████╗  ██║     ██║██╔██╗ ██║         ██║███████║██║   ██║███████╗███████╗██║     
██   ██║██╔══██║██║   ██║╚════██║██╔══╝  ██║     ██║██║╚██╗██║    ██   ██║██╔══██║██║   ██║╚════██║╚════██║██║     
╚█████╔╝██║  ██║╚██████╔╝███████║███████╗███████╗██║██║ ╚████║    ╚█████╔╝██║  ██║╚██████╔╝███████║███████║███████╗
 ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝     ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
"""

"""
Descripción del Código:

Este código implementa un sistema para crear y gestionar robots de combate.

1. **Clases Principales**:
   - **Part**: Define partes del robot (cabeza, brazos, etc.) con atributos como ataque, defensa y consumo de energía.
   - **Robot**: Representa un robot completo, con métodos para atacar, comprar mejoras y mostrar su estado.

2. **Funciones Principales**:
   - `build_robot()`: Permite al usuario crear un robot ingresando su nombre y eligiendo un color.
   - `choose_color()`: Muestra y permite elegir colores para el robot.
   - `valid_value_part_to_use()`: Valida la selección de partes para ataques.

3. **Funcionamiento**:
   - El usuario crea un robot, visualiza su estado y puede atacar o mejorar sus partes.
   - Manejo de errores para entradas no válidas.
"""
# -----------------------------------------------------------------------------------------

robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
                                
"""

ascii_art = r"""
_  _ ____ __   ____ ____ _    ____   ____ ____   ____ _  _ ____   ____ ___  _    ____   
||| \| __\| |  | __\|   ||\/\ | __\  |_ _\|   |  |_ _\||_|\| __\  |  _\|  \ |\/\ | __\  
||\ /|  ]_| |__| \__| . ||   \|  ]_    || | . |    || | _ ||  ]_  | [ \| . \|   \|  ]_  
|/\/ |___/|___/|___/|___/|/v\/|___/    |/ |___/    |/ |/ |/|___/  |___/|/\_/|/v\/|___/   
                                                                                                                                                                                                  
"""

colors = {
        "Black": '\x1b[90m',
        "Blue": '\x1b[94m',
        "Cyan": '\x1b[96m',
        "Green": '\x1b[92m',
        "Magenta": '\x1b[95m',
        "Red": '\x1b[91m',
        "White": '\x1b[97m',
        "Yellow":'\x1b[93m',
    }
cost_attack = {
    "0": 2, "1": 0, "2": 1, "3": 1, "4": 1, "5": 1
}
class Part():
    
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption


    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }


    def reduce_edefense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0

    def is_available(self):
        return self.defense_level <= 0


class Robot:

    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=30, defense_level=30, energy_consumption=30),
            Part("Weapon", attack_level=30, defense_level=30, energy_consumption=30),
            Part("Left Arm", attack_level=20, defense_level=20, energy_consumption=20),
            Part("Right Arm", attack_level=20, defense_level=20, energy_consumption=20),
            Part("Left Leg", attack_level=10, defense_level=10, energy_consumption=10),
            Part("Right Leg", attack_level=10, defense_level=10, energy_consumption=10),
        ]
        
    def print_status(self):
        try:
            print(self.color_code)
            str_robot = robot_art.format(**self.get_part_status())
            self.greet()
            self.print_energy()
            print(str_robot)
            print(colors["White"])
        except KeyError as e:
            print(f"Error printing status: Missing key {e}")  
    
    def greet(self):
        print("Hello, my name is", self.name)
    
    def print_energy(self):
        print("We have", self.energy, " percent energy left")

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status
    
    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].reduce_edefense(self.parts[part_to_use].attack_level) 
        self.energy -= self.parts[part_to_use].energy_consumption

    
    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False
    
    def is_on(self):
        return self.energy >= 0

    def sum_coins(self, piece_attaq):
        if piece_attaq == 0:
            return 2
        elif piece_attaq == 1: 
            return 0
        else:
            return 1

    def buy_store(self, coins):
        print(colors["Magenta"] + "-----------------------------------------" + '\x1b[0m')
        print(colors["Magenta"] + "       WELCOME TO THE STORE!       " + '\x1b[0m')
        print(colors["Magenta"] + "-----------------------------------------" + '\x1b[0m')

        print("0. Head")
        print("1. Weapon")
        print("2. Left Arm")
        print("3. Right Arm")
        print("4. Left Leg")
        print("5. Right Leg")
        print("---------------------------------")

        try:
            choose_part = int(input("Choose a number? (0,1,2,3,4,5): "))
            if choose_part < 0 or choose_part > 5:
                raise ValueError("Part number out of range.")
            var = input("Do you want to improve attack or defense? (a/d): ").lower()
            if var not in ["a", "d"]:
                raise ValueError("Invalid choice, must be 'a' or 'd'.")
            
            count = 0
            while count <= 5:
                if count == choose_part:
                    level = self.parts[count].attack_level if var == "a" else self.parts[count].defense_level
                    improvement = (level * (coins * 10)) / 100
                    if var == "a":
                        self.parts[count].attack_level += improvement
                    else:
                        self.parts[count].defense_level += improvement
                    break
                count += 1
        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

def build_robot():
    try:
        print("---------------------------------")
        robot_name = input("Robot name: ")
        print("---------------------------------")
        color_code = choose_color()
        robot = Robot(robot_name, color_code)
        robot.print_status()
        return robot
    except Exception as e:
        print(f"Error building robot: {e}")

def choose_color():
    try:
        available_colors = colors
        again = 0
        print("Available colors:")
        for key, value in available_colors.items():
            print(value, key)
        print(colors["White"])
        
        while again == 0:
            chosen_color = input("Choose a color (Write a color): ")
            valor = chosen_color.lower()
            ups = valor.capitalize()
            for key, value in available_colors.items():
                if key == ups:
                    again = 1
                    color_code = available_colors[ups] 
                    break
                else:
                    again = 0 
        return color_code
    except Exception as e:
        print(f"Error choosing color: {e}")

def valid_value_part_to_use():
    print("What part should I use to attack?:")
    flag = True
    while flag:
        part_to_use = input("Choose a number part: ")
        part_to_use = int(part_to_use)
        if part_to_use == 0 or part_to_use == 1 or part_to_use == 2 or part_to_use == 3 or part_to_use == 4 or part_to_use == 5:
            flag = False
        else:
            flag = True
    return part_to_use

def valid_value_part_to_attaq():
    print("Which part of the enemy should we attack?")
    flag = True
    while flag:
        part_to_attack = input("Choose a number part: ")
        part_to_attack = int(part_to_attack)
        if part_to_attack == 0 or part_to_attack == 1 or part_to_attack == 2 or part_to_attack == 3 or part_to_attack == 4 or part_to_attack == 5:
            flag = False
        else:
            flag = True
    return part_to_attack

def play():
    count_player_2 = 0
    playing = True
    print(colors["Red"] + "**********************************" + '\x1b[0m')
    print(colors["Yellow"] + ascii_art + '\x1b[0m')  
    print(colors["Yellow"] + "   WELCOME TO THE GAME!         " + '\x1b[0m')  
    print(colors["Green"] + "**********************************" + '\x1b[0m')
    print("Enter name and color for player 1:")
    robot_one = build_robot()
    print("Enter name and color for player 2:")
    robot_two = build_robot()
    
    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0
    coin = 0
    coin_enemy = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
            current_robot.print_status()
            part_to_use = valid_value_part_to_use()
            enemy_robot.print_status()
            part_to_attack = valid_value_part_to_attaq()
            coin = coin + current_robot.sum_coins(part_to_attack)
            store = input("Do you want to go to store? (y/n): ")
            store = str(store)
            if store == "y":
                count_player_1 = 0 
                if count_player_1 <= 2:
                    if coin >= 1:
                        current_robot.buy_store(coin)
                        current_robot.print_status()
                        count_player_1 +=1 
                    else:
                        print ("Sorry but you don't have a money ")
                else:
                    print ("You can't to go to store, because you can go only two times")
            
        else:
            current_robot = robot_two
            enemy_robot = robot_one
            current_robot.print_status()

            part_to_use = valid_value_part_to_use()
            enemy_robot.print_status()
            part_to_attack = valid_value_part_to_attaq()
            coin_enemy =  coin_enemy + enemy_robot.sum_coins(part_to_attack)

            store = input("Do you want to go to store? (y/n): ")
            store = str(store)

            if store == "y":
                if count_player_2 <= 2:
                    if coin_enemy >= 1:
                        current_robot.buy_store(coin_enemy)
                        current_robot.print_status()
                        count_player_2 +=1 
                    else:
                        print ("Sorry but you don't have a money ")
                else:
                    print ("You can't to go to store, because you can go only two times")
            
# ------------------------------------------------------------------------------------------
        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        print("-------------------------------------------------")
        print ("Coins earned in the Attack ",rount)
        print("-------------------------------------------------")
        print("Coins of player 1: ",coin)
        print("Coins of player 2: ",coin_enemy)
        print ("-------------------------------------------------")
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print(colors["Cyan"] + "**********************************" + '\x1b[0m')
            print(colors["Cyan"] + "      CONGRATULATIONS, YOU WON        " + '\x1b[0m')  
            print(colors["Cyan"] + "**********************************" + '\x1b[0m')

play()