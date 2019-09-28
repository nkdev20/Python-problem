from  Libraries.GlassBuilding import GlassBuilding
class Robot:
    def __init__(self, title, data):
        self.title = 'Robot 1'
        self.x_cordinate = int(data[0])
        self.y_cordinate = int(data[1])
        self.direction = data[2]
        self.color = data[3]
        self.commands = ['L', 'R', 'F', 'I']

    def move_left(self):
        if self.direction == 'N':
            self.direction = 'W'
            return
        
        if self.direction == 'S':
            self.direction = 'E'
            return

        if self.direction == 'E':
            self.direction = 'N'
            return

        if self.direction == 'W':
            self.direction = 'S'
            return

    def move_right(self):
       
        if self.direction == 'N':       
            self.direction = 'E'
            return
        
        if self.direction == 'S':
            self.direction = 'W'
            return 

        if self.direction == 'E':
            self.direction = 'S'
            return
        
        if self.direction == 'W':
            self.direction = 'N'
            return


    def forward_by_one_cell(self):
        if self.direction == 'N':
            self.y_cordinate += 1
        
        if self.direction == 'S':
            self.y_cordinate -= 1

        if self.direction == 'W':
            self.x_cordinate -= 1
        
        if self.direction == 'E':
            self.x_cordinate += 1

        print("x =", self.x_cordinate)
        print("y =", self.y_cordinate)


    def get_array_index_using_coordinates(self, GlassBuilding):
        x_cordinate = GlassBuilding.array_x_origin - self.y_cordinate
        y_cordinate = self.x_cordinate
        return [x_cordinate, y_cordinate]



    def fill(self, GlassBuilding):
        grid = GlassBuilding.grid
        array_index = self.get_array_index_using_coordinates(GlassBuilding)
        array_x_index = array_index[0]
        array_y_index = array_index[1]

        if(grid[array_x_index][array_y_index] == 'E'):
            GlassBuilding.grid[array_x_index][array_y_index] = self.color
            GlassBuilding.display()
            return

        if((grid[array_x_index][array_y_index] == 'R'  and self.color == 'G') or (grid[array_x_index][array_y_index] == 'G' and self.color == 'R')):
            GlassBuilding.grid[array_x_index][array_y_index] = 'Y'
            return

    def process_command(self, commands, glassBuilding):  
        if(set(commands).issubset(set(self.commands)) == 'false'):
            return 'false'
        length = len(commands)

        for index in range(length):
            if commands[index] == 'F':
                self.forward_by_one_cell()

            if commands[index] == 'R':
                self.move_right()
            
            if commands[index] == 'L':
                self.move_left()

            if commands[index] == 'I':
                self.fill(glassBuilding)














