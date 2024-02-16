# aim of this file is get all the name into folder
import os


class Gothrough:
    def __init__(self):
        self.Mathmetics = "/Users/jack/Desktop/project/Examable.1.0/搜题题库/9709.qus"
        self.Computer = '/Users/jack/Desktop/project/Examable.1.0/搜题题库/9618.qus'
        # here is shown the path of the exam paper

    def get_filepaths(self):
        file_paths = []
        # Walk the tree.
        for root, directories, files in os.walk(self):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.

        return file_paths  # Self-explanatory.


# file = Gothrough()
# full_file_paths = Gothrough.get_filepaths(file.Mathmetics)
#
# counter = 0
# for file in full_file_paths:
#     counter += 1
#     type = file[-3:]
#     if type != 'pdf':
#         print(file)
#         print(counter)
#
#
# print(full_file_paths)
#
# for i in range(len(full_file_paths)):
#     print(full_file_paths[i])


# "/Users/jack/Desktop/Python/Python_project/Examable/搜题题库/9618.qus"
