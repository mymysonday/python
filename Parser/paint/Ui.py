#coding:utf8

'''
Created on 2016年2月6日

@author: user
'''
from tkinter.filedialog import askdirectory
from tkinter import Tk, Frame, StringVar, Entry, Button, Message
from parser_py import parser

class Paint:
    
    def __init__(self):
        win = Tk()
        win.title("日志文件解析器")
        frame1 = Frame(win)
        frame1.pack()
        self.data_from = StringVar()
        self.data_To =StringVar()
        self.status = StringVar()
        
#       文件来源选择框
        entry_from = Entry(frame1,textvariable=self.data_from)
        mess_f = Message(frame1,text="文件读取路径")
        entry_to =Entry(frame1,textvariable=self.data_To)
        mess_t = Message(frame1,text="文件写入路径")
        self.setTatus_1()
        mess_s = Message(frame1,textvariable=self.status)
        
        button_f = Button(frame1,text="readPath",command=self.read_Path)
        button_to = Button(frame1,text="WritePath",command=self.write_Path)
        button_st = Button(frame1,text="Start_Operation",command=self.start_operation)
        
#       设置位置
        mess_f.grid(row=2,column=1,columnspan=2)
        entry_from.grid(row=2,column=3,columnspan=2)
        button_f.grid(row=2,column=5,columnspan=2)
        
        mess_t.grid(row=3,column=1,columnspan=2)
        entry_to.grid(row=3,column=3,columnspan=2)
        button_to.grid(row=3,column=5,columnspan=2)
        
        mess_s.grid(row=4,rowspan=2,column=3)
        button_st.grid(row=6,column=3)
#        填充
        newM = Message(frame1)
        newM.grid(row=7,rowspan=2)
        win.mainloop()
        
    def setTatus_1(self):
        self.status.set("休息中")
    def setTatus_2(self):
        self.status.set("进行中")
    def setTatus_3(self,sum):
        self.status.set("成功"+sum+"个")    
#        选取路径
    def read_Path(self):
        self.add_from=askdirectory()
        self.data_from.set(self.add_from)
#     写路径
    def write_Path(self):
        self.add_to = askdirectory()
        self.data_To.set(self.add_to)
    
#     开始操作
    def start_operation(self):
        try:
            self.setTatus_2()
            _py = parser.Parser()
            sum =_py.paser_(self.add_from,self.add_to)
            self.setTatus_3(str(sum))
        except:
            self.setTatus_3(str(sum))
# 调用       
Paint()