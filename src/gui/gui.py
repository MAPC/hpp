"""
HPP - Graphical User Interface

The GUI is used to collect requests from the user.
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import config


class GUI(object):

    def __init__(self, composer):
        self.app = QApplication([])

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Hello World!'))

        window = QWidget()
        window.setWindowTitle(config.gui.TITLE)
        window.setLayout(layout)
        self.window = window


    def launch(self):
        self.window.show()
        self.app.exec_()
