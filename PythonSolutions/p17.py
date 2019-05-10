#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Directory String Parser
#   Daily Problem #: 17
#   Author: John Deisher
#   Date Started: 5/8/2019
#   Date Finished: 5/8/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 
and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. 
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a 
file within our file system. For example, in the second example above, 
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
if there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""



class DirNodes(object):
    """docstring for DirNodes"""
    def __init__(self, fileName = None, parent = None):
        super(DirNodes, self).__init__()
        self.subfiles = []
        self.fileName = fileName
        self.parent = parent

    def getPathLen(self):
        longestChild = 0
        longestName = 0
        if len(self.subfiles) == 0:
            return self.fileName
        else:
            for item in self.subfiles:
                if len(item.getPathLen()) > longestName:
                    longestName = len(item.getPathLen())
                    longestChild = item
            return self.fileName + '/' + longestChild.getPathLen()
        pass

    def addChild(self, fileName):
        self.subfiles.append(DirNodes(fileName, self))
        pass

    def BuildTree(self, FileInfo):
        delimString1 = FileInfo.split('\n')
        delimString2 = []
    
        for string in delimString1:
            delimString2.append(string.split('\t'))
            
        rootItem = delimString2.pop(0)
        self.fileName = rootItem[-1]
        currentDepth = 1
        currentNode = self

        for item in delimString2:
            if currentDepth + 1 == len(item):
                #add as a child 
                currentNode.addChild(item[-1])

            elif currentDepth + 1 < len(item):
                currentNode = currentNode.subfiles[-1]
                currentDepth += 1

                currentNode.addChild(item[-1])

            elif currentDepth >= len(item):
                #reset depth to last child

                for _ in range((len(item) - 1)):
                    currentNode = currentNode.parent
                    currentDepth -= 1

                currentNode.addChild(item[-1])
        pass

def main():
    testString1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\tsomeotherrandomebigbutmaybenotneededfile.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\t\t\treallyreallybigfile.ext"
    testString2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    myTree1 = DirNodes()
    myTree1.BuildTree(testString1)
    longest_File_Path = myTree1.getPathLen()

    print(longest_File_Path)
    print("Length: " + str(len(longest_File_Path)))
    print()
    myTree2 = DirNodes()
    myTree2.BuildTree(testString2)
    longest_File_Path = myTree2.getPathLen()

    print(longest_File_Path)
    print("Length: " + str(len(longest_File_Path)))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:

dir/subdir1/someotherrandomebigbutmaybenotneededfile.ext
Length: 56

dir/subdir2/subsubdir2/file2.ext
Length: 32
[Finished in 0.2s]

"""