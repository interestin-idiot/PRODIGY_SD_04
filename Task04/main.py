from PySide6.QtWidgets import QApplication
import sys
from sudokuSolver import SudokuSolver

app = QApplication(sys.argv)
window = SudokuSolver(app)

window.show()
app.exec()