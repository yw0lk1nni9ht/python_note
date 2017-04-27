#-*- coding:utf-8 -*-
from Tkinter import *
import os
def text(name):
   try:
      file_object = open(name)
   except IOError,e:
      text1.insert(INSERT, '“'+ name +'”的不存在')
   
   try: 
      all_the_text = file_object.read()
   finally:
      file_object.close()
   return all_the_text.decode("gb2312")


def printList(event):
   #print mylist.get(mylist.curselection())[4 :].encode("gb2312")
   for p in name_and_path.keys():
      if p == (mylist.get(mylist.curselection())[4 :] + '.txt').encode("gb2312"):
         text1.delete(0.0, END)
         text1.insert(INSERT, text(name_and_path[p]))

#控件申明
root = Tk()
root.title('手册')
root.iconbitmap('F:\\123.ico')

scrollbar = Scrollbar(root)
scrollbar2 = Scrollbar(root)
mylist = Listbox(root, yscrollcommand = scrollbar.set )
text1 = Text(root,width=80,height=40,yscrollcommand  = scrollbar2.set)

#文件名与目录的映射，用于读取
name_and_path = {}

#动态生成目录列表 和 映射
for i in os.listdir(os.getcwd()):
   if i =='nmaplook.py':
      continue
   mylist.insert(END, i.decode('gb2312') + ':')
   for j in os.listdir(os.getcwd() + '\\' + i):
      name_and_path[j] =  os.getcwd() + '\\' + i + '\\' + j[:-4] + '.txt'
      mylist.insert(END, "    " + j.decode('gb2312')[:-4])  
   mylist.insert(END, '\n')

   
mylist.bind('<ButtonRelease-1>',printList)


#布局
mylist.pack(side = LEFT,fill = Y)
scrollbar.pack(side = LEFT,fill=Y)
text1.pack(side = LEFT,fill = Y)
scrollbar2.pack(side = LEFT,fill=Y)
scrollbar.config(command = mylist.yview )
scrollbar2.config(command = text1.yview)
mainloop()
