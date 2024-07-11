import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel, QMessageBox,
)
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt

class SudokuSolver(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app 
        self.setWindowTitle("Sudoku Solver")
        self.setGeometry(100, 100, 400, 450)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.grid_layout = QGridLayout()
        self.inputs = []

        for row in range(9):
            row_inputs = []
            for col in range(9):
                input_field = QLineEdit()
                input_field.setFixedSize(40, 40)
                input_field.setAlignment(Qt.AlignCenter)
                input_field.setMaxLength(1)
                input_field.setValidator(QIntValidator(1, 9, self))
                row_inputs.append(input_field)
                self.grid_layout.addWidget(input_field, row, col)
            self.inputs.append(row_inputs)

        self.layout.addLayout(self.grid_layout)

        self.solve_button = QPushButton("Solve Sudoku")
        self.solve_button.clicked.connect(self.solve_sudoku)
        self.layout.addWidget(self.solve_button)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

    def get_board(self):
        board = []
        for row in range(9):
            board_row = []
            for col in range(9):
                text = self.inputs[row][col].text()
                board_row.append(int(text) if text else 0)
            board.append(board_row)
        return board

    def set_board(self, board):
        for row in range(9):
            for col in range(9):
                self.inputs[row][col].setText(str(board[row][col]) if board[row][col] != 0 else "")

    def solve_sudoku(self):
        board = self.get_board()
        if solve_sudoku(board):
            self.set_board(board)
            self.result_label.setText("Sudoku Solved!")
        else:
            QMessageBox.warning(self, "Error", "This Sudoku puzzle is unsolvable!")

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

