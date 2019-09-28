class GlassBuilding:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.defaultColor = 'E'
        self.array_x_origin = height-1
        self.array_y_origin = 0

    def construct_grid(self):
        self.grid = [ [self.defaultColor] * self.width for i1 in range(self.height) ]
    

    def display(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.grid[i][j], end=' ')
            print("\n")
