"""
HPP: Housing Production Plan Tool
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import config


def main():
    app = QApplication([])

    layout = QVBoxLayout()
    layout.addWidget(QLabel('Hello World!'))

    window = QWidget()
    window.setWindowTitle(config.gui.TITLE)
    window.setLayout(layout)
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
