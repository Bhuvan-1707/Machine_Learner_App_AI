import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout
import simplecalc

class MyApp(QWidget):
    def __init__(self):
        super().__init__()  
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 0, 100, 200)

        layout = QVBoxLayout()

        # ----- Label tag as html ----- #
        self.label = QLabel('Enter two numbers:', self)
        layout.addWidget(self.label)

        # ----- Taking in number 1 ----- #
        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText('Enter a')
        layout.addWidget(self.input1)

        # ----- Taking in number 2 ----- #
        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText('Enter b')
        layout.addWidget(self.input2)

        # Buttons for different operations

        button_layout1 = QHBoxLayout()
        button_layout2 = QHBoxLayout()
        # Add
        self.add_button = QPushButton('⬚+⬚', self)
        self.add_button.clicked.connect(self.calculate_sum)
        button_layout1.addWidget(self.add_button)

        # Subtract
        self.subtract_button = QPushButton('⬚-⬚', self)
        self.subtract_button.clicked.connect(self.calculate_difference)
        button_layout1.addWidget(self.subtract_button)

        # Multiply
        self.multiply_button = QPushButton('⬚x⬚', self)
        self.multiply_button.clicked.connect(self.calculate_product)
        button_layout1.addWidget(self.multiply_button)

        # Divide
        self.divide_button = QPushButton('⬚/⬚', self)
        self.divide_button.clicked.connect(self.calculate_quotient)
        button_layout1.addWidget(self.divide_button)

        layout.addLayout(button_layout1)

        # ----- Taking in number 3 ----- #
        self.input3 = QLineEdit(self)
        self.input3.setPlaceholderText('Enter c')
        layout.addWidget(self.input3)

        # Exponent
        self.exponent_button = QPushButton('e^⬚', self)
        self.exponent_button.clicked.connect(self.calculate_exponent)
        button_layout2.addWidget(self.exponent_button)

        # Log of a to base b 
        self.logba_button = QPushButton('ln(⬚)', self)
        self.logba_button.clicked.connect(self.calculate_log_ba)
        button_layout2.addWidget(self.logba_button)

        layout.addLayout(button_layout2)

        # Showcasing the result
        self.result_label = QLabel('Result: ', self)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def calculate_sum(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = simplecalc.add(num1, num2)  # Call the C++ function
            self.result_label.setText(f'Result: {result:.6f}')
        except ValueError:
            self.result_label.setText('Invalid input!')

    def calculate_difference(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = simplecalc.subtract(num1, num2)  # Call the C++ function
            self.result_label.setText(f'Result: {result:.6f}')
        except ValueError:
            self.result_label.setText('Invalid input!')

    def calculate_product(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = simplecalc.multiply(num1, num2)  # Call the C++ function
            self.result_label.setText(f'Result: {result:.6f}')
        except ValueError:
            self.result_label.setText('Invalid input!')

    def calculate_quotient(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = simplecalc.divide(num1, num2)  # Call the C++ function
            self.result_label.setText(f'Result: {result:.6f}')
        except ValueError:
            self.result_label.setText('Invalid input!')

    def calculate_exponent(self):
        try:
            num3 = float(self.input3.text())
            result = simplecalc.exponent(num3)  # Call the C++ function
            self.result_label.setText(f'Result: {result:.6f}')
        except ValueError:
            self.result_label.setText('Invalid input!')

    def calculate_log_ba(self):
        try:
            num3 = float(self.input3.text())
            result = simplecalc.logarithm(num3)  # Call the C++ function
            self.result_label.setText(f'Result: {result:.6f}')
        except ValueError:
            self.result_label.setText('Invalid input!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())