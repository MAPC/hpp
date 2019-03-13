"""
HPP - AbstractWriter

This abstract class outlines the common behaviors for 
writing the contents of a DataComposer to a file.
"""

from random import getrandbits
from datetime import datetime


class AbstractWriter(object):

    def __init__(self, composer, file_name = None):
        self.composer = composer

        if not file_name:
            hash_len = 10
            random_hash = "%0x" % getrandbits(hash_len * 4)
            now = datetime.now()

            file_name = "hpp-%s-%s" % (now.strftime("%Y-%m-%d"), random_hash)

        self.file_name = file_name


    def write(self):
        pass
