#!/usr/bin/env python

todo_file = 'todo.txt' # filepath
archive_file = 'archive.txt'
arc = open(archive_file, 'a') # open archive
t = open(todo_file, 'r') # open active list
from datetime import datetime
import readline # for raw_input, allows up-arrowing

class tasklist:
    def __init__(self,contents=None):
        self.contents = contents or []

    def __str__(self):
        n = 0
        result = ""
        for element in self.contents:
            result = result + `n` + '] ' + element
            n += 1
        return result

    def read(self):
        for line in t:
            self.contents.append(line)

    def finish(self,i):
        timestamp = str(datetime.now())
        arc.write(timestamp+"\t")
        arc.write(self.contents[i]+"\n")
        self.contents.pop(i)
        tw = open(todo_file, 'w') # use different local variable name
        for element in self.contents:
            tw.write(element)
        tw.close()

    def add(self,task_item):
        self.contents.append(task_item)
        ta = open(todo_file, 'a') # use different local variable name
        ta.write(task_item+"\n")
        ta.close()

    def edit(self,task_index, task_edit):
        self.contents[task_index] = task_edit + "\n"
        tw = open(todo_file, 'w') # use different local variable name
        for element in self.contents:
            tw.write(element)
        tw.close()

    def move(self,i_s,i_e):
        T = self.contents.pop(i_s)
        self.contents.insert(i_e,T)
        tw = open(todo_file, 'w') # use different local variable name
        for element in self.contents:
            tw.write(element)
        tw.close()

tl = tasklist()

tl.read()
t.close()
print "To Do:\n"
print tl

action = raw_input('(f)inished, (a)dd, (e)dit, (m)ove, (h)elp, [enter] to close: ')
if action == "f":
    index = input('num: ')
    tl.finish(index)
    print 'removed'
    print tl
elif action == "h":
    print " To archive a task:\n Enter 'd' and then the number of the task you want to delete."
    print " To add a task:\n Enter'a' and then the text of the new item."
    print " To edit a task:\n Enter 'e' and then the number of the task you want to change."
elif action == "a":
    item = raw_input('add: ')
    tl.add(item)
    print 'added'
    print tl
elif action == "e":
    index = input('num: ')
    edit = raw_input('new: ')
    tl.edit(index, edit)
    print 'changed'
    print tl
elif action == "m":
    index_start = input('num: ')
    index_end = input('to: ')
    tl.move(index_start, index_end)
    print 'moved'
    print tl

arc.close()