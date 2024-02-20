## ODE Solver with GUI using Euler and Improved Euler Methods
# Overview
This Python program provides a graphical interface for solving ordinary differential equations (ODEs) using the Euler method and the improved Euler method. The Euler method is a simple numerical technique for approximating solutions to first-order ODEs, while the improved Euler method offers enhanced accuracy by using midpoint estimates.

## Features
- GUI interface for ease of use.
- Implementation of the Euler method and the improved Euler method for solving ODEs.
- Customizable initial conditions and parameters.
- Visualization of the numerical solution alongside the analytical solution (if available).
## Installation
1. Clone the repository to your local machine:
'''
git clone https://github.com/yourusername/ode-solver.git
'''
Navigate to the project directory:

bash
Copy code
cd ode-solver
Install the required dependencies:

Copy code
pip install -r requirements.txt
Usage
Run the program:

css
Copy code
python main.py
Enter the differential equation along with initial conditions and parameters.

Choose the method (Euler or Improved Euler) for solving the ODE.

Click the "Solve" button to visualize the numerical solution.

Example Equations
Example 1: dy/dx = x + y, Initial condition: y(0) = 1
Example 2: dy/dx = x - y, Initial condition: y(0) = 0
