# Logic for solving Rubik's cube
# Created 4/11/18
# By Jake Masters and Patrick Warren

class CubeSolver:

    # cube = [row, col]

    cube = []

    def getSquare(self,row, col):
        return self.cube[(row*3) + col]

    def getFace(self,face):
        retFace = [[],[],[]]
        if face == 'top':
            retFace = [[self.cube[0][3], self.cube[0][4], self.cube[0][5]],
                       [self.cube[1][3], self.cube[1][4], self.cube[1][5]],
                       [self.cube[2][3], self.cube[2][4], self.cube[2][5]]]
        if face == 'bottom':
            pass
        if face == 'left':
            pass
        if face == 'right':
            pass
        if face == 'front':
            pass
        if face == 'back':
            pass
        return retFace

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
