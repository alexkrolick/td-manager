#!/usr/bin/env python

todo_file = "todo.txt" # filepath
archive_file = "archive.txt"
arc = open(archive_file, 'a') # open archive
from datetime import datetime
import readline # for raw_input, allows up-arrowing

class tasklist:
    def __init__(self,src="todo.txt",contents=None):
        self.contents = contents or []
        self.src = src

    def __str__(self):
        n = 0
        result = ""
        for element in self.contents:
            result = result + `n` + '] ' + element
            n += 1
        return result

    def read(self):
        t = open(self.src, 'r') # open active list
        for line in t:
            self.contents.append(line)
        t.close()

    def finish(self):
        i = input('num: ')
        timestamp = str(datetime.now())
        arc.write(timestamp+"\t")
        arc.write(self.contents[i]+"\n")
        self.contents.pop(i)
        tw = open(self.src, 'w') # local name for todo file
        for element in self.contents:
            tw.write(element)
        tw.close()

    def add(self):
        task_item = raw_input('add: ')
        self.contents.append(task_item)
        ta = open(self.src, 'a')
        ta.write(task_item+"\n")
        ta.close()

    def edit(self):
        task_index = input('num: ')
        task_edit = raw_input('new: ')
        self.contents[task_index] = task_edit + "\n"
        tw = open(self.src, 'w')
        for element in self.contents:
            tw.write(element)
        tw.close()

    def move(self):
        i_s = input('num: ')
        i_e = input('to: ')
        T = self.contents.pop(i_s)
        self.contents.insert(i_e,T)
        tw = open(self.src, 'w')
        for element in self.contents:
            tw.write(element)
        tw.close()

tl = [tasklist("todo.txt")] # default tasklist, src = todo.txt in this directory
tl[0].read()
print "To Do:\n"
print tl[0]

# user interactions
action = raw_input('(f)inished, (a)dd, (e)dit, (m)ove, (h)elp, [enter] to close: ')
if action == "f":
    tl[0].finish()
    print 'removed'
    print tl[0]
elif action == "h":
    print "\nTo archive a task:\n Enter 'f' and then the number of the task you want to mark as finished."
    print " The text of the task will be timestamped and copied into the archive file."
    print "\nTo add a task:\n Enter'a' and then the text of the new item."
    print "\nTo edit a task:\n Enter 'e' and then the number of the task you want to change."
elif action == "a":
    tl[0].add()
    print 'added'
    print tl[0]
elif action == "e":
    tl[0].edit()
    print 'changed'
    print tl[0]
elif action == "m":
    tl[0].move()
    print 'moved'
    print tl[0]

arc.close()