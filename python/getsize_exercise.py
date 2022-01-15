import os.path

"""
Exercise:
---------
Implement the functions below by following the instructions
in the docstrings.

"""

def getfilesize(path=".", extension=None):
    """
    Returns the total size of all files in a directory path
    If extension is specified as a string, only calculate
    and return the total size (in bytes) of files of the
    specified extension.

    Example (might not work in doctest)
    -----------------------------------
        # Get total size of all files with .conf extension in /etc folder
        >>> getfilesize("/etc", ".conf")
        21345

    """

    return sum([ os.path.getsize(x) for x in os.listdir(path) if x.endswith(extension)])
    




def getsize(path="."):
    """
    Calculates the total size (in bytes) of all files and directories
    in a given path recursively and returns the same.

    Example (might not work in doctest)
    -----------------------------------
        # Get total size of /etc folder structure
        >>> getsize("/etc")
        4455334

    """
    pass # TODO: Implement the logic here.

if __name__ == '__main__':
    path = input("Enter path to scan: ")
    ext = input("Enter file extension to scan (or empty): ")

    fsize = getfilesize(path, ext if ext else None)
    total_size = getsize(path)

    print("The total size of files with {} extension in {} is {}".format(
            ext if ext else "all", path, fsize))

    print("The total size of directory {} is {}".format(
            path, total_size))
