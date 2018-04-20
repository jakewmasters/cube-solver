# Logic for solving Rubik's cube
# Created 4/11/18
# By Jake Masters and Patrick Warren

class CubeSolver:

    cube = []

    def getSquare(self,row, col):
        return self.cube[(row*3) + col]

    def getFace(self,face):
        if face == 'U':
            return self.cube[0:9]
        if face == 'D':
            return self.cube[9:18]
        if face == 'R':
            return self.cube[18:27]
        if face == 'L':
            return self.cube[27:36]
        if face == 'F':
            return self.cube[36:45]
        if face == 'B':
            return self.cube[45:54]

    def createCube(self):
        colors = ['R', 'G', 'B', 'Y', 'O', 'W']
        for i in range(6):
            color = colors[i]
            for j in range(9):
                self.cube.insert((i*9) + j, color)

    def rotate(self, op):
        pass

    def solve(self):
        pass



cube1 = CubeSolver()
cube1.createCube()
print(cube1.getFace('U'))
print(cube1.getFace('D'))
print(cube1.getFace('R'))
print(cube1.getFace('L'))
print(cube1.getFace('F'))
print(cube1.getFace('B'))
