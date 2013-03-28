td-manager
==========
Command line to-do list manager in python. It also saves and timestamps stuff you already did in an archive.txt file, providing rudimentary version control.

To run:
Make sure a file called 'todo.txt' exists where the python script is looking for it (by default, the same directory).
Run 'python todo.py', or make the file executable and link it to a shell script in /usr/bin/local (or whatever). Then you can run something like 'todo' from the command line and access all your tasks.
The attached .desktop file shows how you might stick a link to the script in an XFCE desktop panel, for example.

Other:
The main class takes filenames as an argument and provides archiving, editing, etc. as functions. So, theoretically you could write a more complicated frontend that accepts multiple todo lists as 'categories,' or even a GUI in ncurses or GTK/wxpython.