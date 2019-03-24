import os


class DirectoryStructure:
    """This class performs the scanning operations"""

    def __init__(self,startpath):
        self.folder_to_scan = startpath
        open("list_of_files.txt", "w").close()

    def scan_directory(self):
        """This function scan the directories"""

        for root, dirs, files in os.walk(self.folder_to_scan):
            level = root.replace(self.folder_to_scan, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))

            with open("list_of_files.txt","a") as f:
                 f.write('{}{}/'.format(indent, os.path.basename(root)))
                 f.write("\n")

            subindent = ' ' * 4 * (level + 1)
            for fnames in files:
                print('{}{}'.format(subindent, fnames))
                with open("list_of_files.txt", "a") as fi:
                    fi.write('{}{}'.format(subindent, fnames))
                    fi.write("\n")