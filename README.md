# Cube-Solver

A project for COS 351.  
Made by Jake Masters, Patrick Warren, and Josh Teigland.  

## Build Instructions

### Python

To develop Cube-Solver locally:  
1. Clone the repository.
2. Open the repository in PyCharm.  
3. Create a virtual environment called `venv` using the `virtualenv` command or PyCharm's virtualenv setup tool.  
4. Create a `.gitignore` file. 
5. Populate your `.gitignore` file with the following contents:  
~~~
*venv/
*.idea/
.gitignore
~~~

### C++

To develop the vision I/O portion locally:  
1. Clone the repository.
2. Open the repository in CLion. 
3. Compile using the following command:  
~~~
$ gcc src/main.cpp -lstdc++ -o cube-solver
~~~

4. Run the executable:
~~~
$ ./cube-solver
~~~
