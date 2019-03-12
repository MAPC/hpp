"""
HPP - AbstractWriter

This abstract class outlines the common behaviors for 
writing the contents of a DataComposer to a file.
"""


def AbstractWriter(object):

    def __init__(self, composer):
        self.composer = composer


    def write(self):
        pass
