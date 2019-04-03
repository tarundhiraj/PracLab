"""
Complete this program to implement the rudimentary
interactive command shell. The program should
work as below:
  1. When this program is executed, it prompts a shell
     prompt "PyShell>" and expects user input.
  2. If the user types 'list' and presses Enter, it
     should call the listdir() function.
  3. If the user types 'whoami', likewise it should
     call the showuser() function
  4. The comments above each function definition indicates
     the command for which - the function should be invoked.
  5. If the user types arbitrary string, invalid_command()
     function should be invoked.
  6. Ensure that the logic is scalable (i.e., if..elif.. should
     be avoided as they do not scale if the number of commands
     are 100 or above.)

Implement the run() function below and make necessary
changes to ensure that the shell works as per the transcript
shown below:
-----------------------------------------------------------------------
    $ python3 pyshell.py
    PyShell> list /bin /usr /opt
    Listing contents of ("/bin", "/usr", "/opt")

    PyShell> date
    Tue Aug 01 09:30:00 2017

    PyShell> dslfjsdfdsf
    Invalid command - dslfjsdfdsf

    PyShell> pwd
    /Users/chandrashekar/Training/Python_Primers/Samples

    PyShell> whoami
    chandrashekar

    PyShell> exit
    $
-----------------------------------------------------------------------
Implement a scalable solution; i.e., adding new commands
must be mostly effortless and the shell command evaluation
must be performance efficient.

"""

quit = False


# Invoke this function if the command is 'list'
def listdir(*args):
    print("Listing contents of", args)

# Invoke this function if the command is 'whoami'
def show_user(*args):
    from getpass import getuser
    print(getuser())

# Invoke this function if the command is 'date'
def print_date(*args):
    from time import ctime
    print(ctime())

# Invoke this function if the command is 'pwd'
def show_curr_dir(*args):
    from os import getcwd
    print(getcwd())

# Invoke this function if the command is 'exit'
def exit_shell(*args):
    global quit
    quit = True

# Invoke this function if the command is anything else
def invalid_command(*args):
    print("Invalid command - ", args[0])

command_list = { "list": listdir,
                 "date": print_date,
                 "pwd": show_curr_dir,
                 "whoami":show_user,
                 "exit": exit_shell,
                } 


def run():
    while not quit:
        command = input("PyShell> ")
        args = command.split()
        rcom = command_list.get(args[0], invalid_command)
        rcom()
        

        

if __name__ == '__main__':
    run()

