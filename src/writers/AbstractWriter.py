"""
HPP - AbstractWriter

This abstract class outlines the common behaviors for 
writing the contents of a DataComposer to a file.
"""

from os import path
from random import getrandbits
from datetime import datetime


class AbstractWriter(object):

    output_dir = 'src/web/compositions'

    def __init__(self, composer, include_metadata):
        self.composer = composer
        self.include_metadata = include_metadata

        hash_len = 10
        random_hash = "%0x" % getrandbits(hash_len * 4)
        now = datetime.now()

        self.file_name = "hpp-%s-%s" % (now.strftime("%Y-%m-%d"), random_hash)


    def get_file(self):
        return "%s.%s" % (self.file_name, self.file_ext)


    def get_output_path(self):
        return path.join(self.output_dir, self.file_name)


    def write(self):
        pass
