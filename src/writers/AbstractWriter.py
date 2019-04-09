"""
HPP - AbstractWriter

This abstract class outlines the common behaviors for 
writing the contents of a DataComposer to a file.
"""

import config
from datetime import datetime
from random import getrandbits
from os import listdir, path, unlink


class AbstractWriter(object):

    output_dir = 'src/web/compositions'

    def __init__(self, composer, include_metadata):
        self.composer = composer
        self.include_metadata = include_metadata

        hash_len = 10
        random_hash = "%0x" % getrandbits(hash_len * 4)
        now = datetime.now()

        self.file_name = "hpp-%s-%s" % (now.strftime("%Y-%m-%d"), random_hash)

        self.cleanup_output_dir()


    def get_file(self):
        return "%s.%s" % (self.file_name, self.file_ext)


    def get_output_path(self):
        return path.join(self.output_dir, self.file_name)


    def write(self):
        pass


    def cleanup_output_dir(self):
        compositions = [fd for fd in [path.join(self.output_dir, fd) for fd in listdir(self.output_dir)] if path.isfile(fd)]

        # To protect any compositions being created concurrently when the quantity
        # of compositions nears the limit of MAX_COMPOSITIONS, we only consider deletion
        # for compositions that were created over an hour ago.
        hour = 60 * 60
        now = datetime.now().timestamp()
        an_hour_ago = now - hour
        old_compositions = [c for c in compositions if path.getmtime(c) < an_hour_ago]

        if len(old_compositions) >= config.writer.MAX_COMPOSITIONS:
            for composition in old_compositions:
                try:
                    unlink(composition) 
                except Exception as e:
                    print(e)
