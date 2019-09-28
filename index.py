from Libraries.GlassBuilding import GlassBuilding
from Libraries.Robot import Robot

def create_robo_object(title, position):
    return Robot(title, position)

def create_glass_building_object(width, height):
    return  GlassBuilding(width, height)

if  __name__ == "__main__":

    print("Enter dimensions\n")
    width = int(input('Enter width'))
    height = int(input('Enter height'))
    glassBuilding  = create_glass_building_object(width, height)
    glassBuilding.construct_grid()
    glassBuilding.display()
    
    print("Enter initial position of robo1\n")
    initial_position = input().split(' ')
    int(initial_position[0])
    int(initial_position[1])
    robo1 = create_robo_object('Robo 1', initial_position)


    print(" Enter directions\n")
    command = list(input())
    robo1.process_command(command, glassBuilding)
    

    print("Enter initial position of robo2\n")
    initial_position = input().split(' ')
    int(initial_position[0])
    int(initial_position[1])
    robo2 = create_robo_object('Robo 2', initial_position)

    print(" Enter directions\n")
    command = list(input())
    robo2.process_command(command, glassBuilding)


    print('print the grid')
    glassBuilding.display()
