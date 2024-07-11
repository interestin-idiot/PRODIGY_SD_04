# Software Development Intern At Prodigy Infotech 
## Task 4 : Implement a Sudoku Solver

Create a program that solves Sudoku puzzles automatically. The program should take an input grid representing an unsolved Sudoku puzzle and use an algorithm to fill in the missing numbers.
It should use backtracking or other suitable techniques to explore possible solutions and find the correct arrangement of numbers for the puzzle. Once solved, the program should display the completed Sudoku grid.

# Dependencies 
1. Python 3.12
2. PySide6

# Objectives:

1. **User-Friendly Interface**: Create an intuitive and interactive graphical interface for solving Sudoku puzzles.
2. **Input and Output**: Allow users to input a Sudoku puzzle and view the solved puzzle.
3. **Accuracy and Efficiency**: Ensure the solver uses an efficient algorithm to provide accurate solutions.
4. **User Interaction**: Enable users to input custom puzzles and see the results in real-time.
5. **Clear Instructions and Feedback**: Provide clear guidance and feedback to users throughout the process.
# Project Structure

## Main Interface:

1. **Title and Instructions**: Display the application's title and instructions for the user.
2. **Input Grid**: A 9x9 grid where users can input their Sudoku puzzle.
3. **Solve Button**: A button to trigger the solving process.
4. **Output Grid**: Display the solved Sudoku puzzle.

## Solving Logic:

1. **User Input**: Users can enter a Sudoku puzzle into the grid.
2. **Backtracking Algorithm**: The application uses a backtracking algorithm to solve the puzzle.
3. **Display Results**: The solved puzzle is displayed in the grid.
4. **Error Handling**: Inform the user if the puzzle is unsolvable or if there are any issues with the input.

# Implementation Details
## Interface Setup:

1. The main window is designed to be visually appealing and easy to use.
2. The 9x9 grid allows users to input their Sudoku puzzle conveniently.
3. A button to solve the puzzle is easily accessible.
4. The results are displayed in the same grid for immediate feedback.

## Game Flow:

1. When the application starts, users can see a 9x9 grid for entering the Sudoku puzzle.
2. Users fill in the grid with their puzzle and press the solve button.
3. The application processes the input and displays the solved puzzle in the grid.
4. If the puzzle cannot be solved, the application informs the user.

## Feedback and Messages:

1. Clear instructions guide the user on how to input the puzzle and solve it.
2. The application provides feedback if the input is invalid or if the puzzle is unsolvable.
3. Accurate results are displayed, allowing the user to see the solved puzzle immediately.
