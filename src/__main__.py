"""
HPP: Housing Production Plan Tool
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


def main():
    app = QApplication([])

    label = QLabel('Hello World!')

    layout = QVBoxLayout()
    layout.addWidget(QLabel('Hello World!'))

    window = QWidget()
    window.setWindowTitle('HPP')
    window.setLayout(layout)
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
