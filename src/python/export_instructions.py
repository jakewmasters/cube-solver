import pycuber as pc
from pycuber.solver import CFOPSolver

def in_matrix():
    mycube = pc.Cube()

    # pass over input that we don't really care about
    for i in range(6):
        skip = input()

    # Legend
    # 0 = green
    # 1 = orange
    # 2 = red
    # 3 = white
    # 4 = yellow
    # 5 = blue
    top_face = input().split(" ")
    top_face_colors = []
    for letter in top_face:
        if letter == "0":
            top_face_colors.append("g")
        elif letter == "1":
            top_face_colors.append("o")
        elif letter == "2":
            top_face_colors.append("r")
        elif letter == "3":
            top_face_colors.append("w")
        elif letter == "4":
            top_face_colors.append("y")
        elif letter == "5":
            top_face_colors.append("b")
    print("Top face is " + str(top_face_colors))

    bottom_face = input().split(" ")
    bottom_face_colors = []
    for letter in bottom_face:
        if letter == "0":
            bottom_face_colors.append("g")
        elif letter == "1":
            bottom_face_colors.append("o")
        elif letter == "2":
            bottom_face_colors.append("r")
        elif letter == "3":
            bottom_face_colors.append("w")
        elif letter == "4":
            bottom_face_colors.append("y")
        elif letter == "5":
            bottom_face_colors.append("b")
    print("Bottom face is " + str(bottom_face_colors))

    right_face = input().split(" ")
    right_face_colors = []
    for letter in right_face:
        if letter == "0":
            right_face_colors.append("g")
        elif letter == "1":
            right_face_colors.append("o")
        elif letter == "2":
            right_face_colors.append("r")
        elif letter == "3":
            right_face_colors.append("w")
        elif letter == "4":
            right_face_colors.append("y")
        elif letter == "5":
            right_face_colors.append("b")
    print("Right face is " + str(right_face_colors))

    left_face = input().split(" ")
    left_face_colors = []
    for letter in left_face:
        if letter == "0":
            left_face_colors.append("g")
        elif letter == "1":
            left_face_colors.append("o")
        elif letter == "2":
            left_face_colors.append("r")
        elif letter == "3":
            left_face_colors.append("w")
        elif letter == "4":
            left_face_colors.append("y")
        elif letter == "5":
            left_face_colors.append("b")
    print("Left face is " + str(left_face_colors))

    front_face = input().split(" ")
    front_face_colors = []
    for letter in front_face:
        if letter == "0":
            front_face_colors.append("g")
        elif letter == "1":
            front_face_colors.append("o")
        elif letter == "2":
            front_face_colors.append("r")
        elif letter == "3":
            front_face_colors.append("w")
        elif letter == "4":
            front_face_colors.append("y")
        elif letter == "5":
            front_face_colors.append("b")
    print("Front face is " + str(front_face_colors))

    back_face = input().split(" ")
    back_face_colors = []
    for letter in back_face:
        if letter == "0":
            back_face_colors.append("g")
        elif letter == "1":
            back_face_colors.append("o")
        elif letter == "2":
            back_face_colors.append("r")
        elif letter == "3":
            back_face_colors.append("w")
        elif letter == "4":
            back_face_colors.append("y")
        elif letter == "5":
            back_face_colors.append("b")
    print("Back face is " + str(back_face_colors))
    print("")

    # [['g','o','r','o','w','r','y','b','o'],
    #  ['p','g','w','y','y','g','b','y','r'],
    #  ['w','w','b','b','r','o','g','r','y'],
    #  ['y','w','b','b','o','r','o','g','y'],
    #  ['r','o','g','b','g','y','b','w','r'],
    #  ['w','y','o','g','b','w','g','r','w']]

    # generate the Cube object
    alg = pc.Formula()
    random_alg = alg.random()

    # cube state before solving
    mycube(random_alg)
    print(mycube)

    # example attribute set
    mycube.__setattr__(mycube["U"].colour, "blue")
    print(mycube.__getattr__(mycube["U"].colour))
    # doesn't work like one would expect

    solver = CFOPSolver(mycube)
    solution = solver.solve(suppress_progress_messages=True)
    # alter solution messages
    solution = str(solution).split()
    for instruction in solution:
        if instruction == "F":
            print("Rotate the Front face of the Cube 90 degrees in the clockwise direction.")
        elif instruction == "R":
            print("Rotate the Right face of the Cube 90 degrees in the clockwise direction.")
        elif instruction == "L":
            print("Rotate the Left face of the Cube 90 degrees in the clockwise direction.")
        elif instruction == "U":
            print("Rotate the Top face of the Cube 90 degrees in the clockwise direction.")
        elif instruction == "B":
            print("Rotate the Back face of the Cube 90 degrees in the clockwise direction.")
        elif instruction == "D":
            print("Rotate the Bottom face of the Cube 90 degrees in the clockwise direction.")
        elif instruction == "F'":
            print("Rotate the Front face of the Cube 90 degrees in the counter-clockwise direction.")
        elif instruction == "R'":
            print("Rotate the Right face of the Cube 90 degrees in the counter-clockwise direction.")
        elif instruction == "L'":
            print("Rotate the Left face of the Cube 90 degrees in the counter-clockwise direction.")
        elif instruction == "U'":
            print("Rotate the Top face of the Cube 90 degrees in the counter-clockwise direction.")
        elif instruction == "B'":
            print("Rotate the Back face of the Cube 90 degrees in the counter-clockwise direction.")
        elif instruction == "D'":
            print("Rotate the Bottom face of the Cube 90 degrees in the counter-clockwise direction.")
        elif instruction == "F2":
            print("Rotate the Front face of the Cube 180 degrees.")
        elif instruction == "R2":
            print("Rotate the Right face of the Cube 180 degrees.")
        elif instruction == "L2":
            print("Rotate the Left face of the Cube 180 degrees.")
        elif instruction == "U2":
            print("Rotate the Top face of the Cube 180 degrees.")
        elif instruction == "B2":
            print("Rotate the Back face of the Cube 180 degrees.")
        elif instruction == "D2":
            print("Rotate the Bottom face of the Cube 180 degrees.")

    print("")
    print(mycube)
    print("")


in_matrix()
