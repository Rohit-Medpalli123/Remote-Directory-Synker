#This module provides classes and functions for comparing sequences.
# It can be used for example, for comparing files, and can produce difference
#  information in various formats, including HTML and context and unified diffs.
#  For comparing directories and files, see also, the filecmp module.

import difflib

class Show_diff:
    """This class handles the comparision of two text files"""
    def __init__(self,remotefilepath,localfilepath):
        self.RemoteFilePath = remotefilepath
        self.LocalFilePath = localfilepath

    def comapre_files(self):
        text1 = open(self.RemoteFilePath).readlines()
        text2 = open(self.LocalFilePath).readlines()

        diff = difflib.unified_diff(text1, text2, lineterm='')
        print('\n'.join(list(diff)))