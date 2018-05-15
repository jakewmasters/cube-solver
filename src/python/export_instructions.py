import pycuber as pc
from pycuber.solver import CFOPSolver

def in_matrix():
    for i in range(6):
        skip = input()

    top_face = input()
    bottom_face = input()
    right_face = input()
    left_face = input()
    front_face = input()
    back_face = input()




    matrix = [['g','o','r','o','w','r','y','b','o'],
              ['p','g','w','y','y','g','b','y','r'],
              ['w','w','b','b','r','o','g','r','y'],
              ['y','w','b','b','o','r','o','g','y'],
              ['r','o','g','b','g','y','b','w','r'],
              ['w','y','o','g','b','w','g','r','w']]
    print(matrix)
    print("")

    mycube = pc.Cube()
    alg = pc.Formula()
    random_alg = alg.random()
    mycube(random_alg)
    solver = CFOPSolver(mycube)
    solution = solver.solve(suppress_progress_messages=True)
    print(solution)
    print("")
    print(mycube)
    print("")


in_matrix()
