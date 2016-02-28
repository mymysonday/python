#coding:utf8
'''
Created on 2016年2月6日

@author: user
'''
import os
import re
class Parser:
#     初始化
    def __init__(self):
        self.file_list = list()
        self.sum=0
        
#    解析 文本
    def paser_(self,readPath,writePath):
        try:
            self.getFilename(readPath)
            lst = self.getFile_list()
            self.setCss(writePath)
            for dirctory  in lst:
                file_Name = re.findall(r"[A-z0-9_]+(?=\.)",dirctory)
                self.read_data = open(dirctory)
                index=1
                count=0
                self.w_data = open(writePath+"/"+file_Name[0]+"_"+str(index)+".html","w")
                self.weiteHtmlHead(self.w_data)
                for line in self.read_data:
                    try:
                        if(count<7000):
                            self.w_data.write("<tr>")
                            self.w_data.write("<td>"+re.findall(r"\d+-\d+-\d+",line)[0]+"</td>")
                            self.w_data.write("<td>"+re.findall(r"\d+\:\d+\:\d+",line)[0]+"</td>")
                            self.w_data.write("<td>"+re.findall(r"\s[A-z,]+\s", line)[0]+"</td>")
                            self.w_data.write("<td>"+re.findall(r"/[A-z0-9/\.]+\s+", line)[0]+"</td>")
                            self.w_data.write("<td>"+re.findall(r"\s[A-z0-9\.]+\.[A-z]+|\w+_\w+",line)[0]+"</td>")
                            self.w_data.write("</tr>")
                            count+=1
                        else:
                            self.writeHtmlEnd(self.w_data)
                            self.w_data.close()
                            index+=1
                            count=0
                            self.w_data = open(writePath+"/"+file_Name[0]+"_"+str(index)+".html","w")
                            self.weiteHtmlHead(self.w_data)
                    except:
                        pass
                    line =self.read_data.readline()
                self.writeHtmlEnd(self.w_data)
                self.w_data.close()
                self.read_data.close()
                self.sum=self.sum+1
        except:
            self.sum=self.sum-1
        return  self.sum
    
#     获取文件名字列表           
    def getFile_list(self):
        return self.file_list
        
#     递归获取文件名
    def getFilename(self,readPath):
        if(os.path.isfile(readPath)):
            self.file_list.append(readPath)
        else:
            lst = os.listdir(readPath)
            for subDirctory in lst:
                self.getFilename(readPath+"/"+subDirctory)
    
#     网页头
    def weiteHtmlHead(self,w_data):
        w_data.write("<html>")
        w_data.write("<head>")
        w_data.write("<title>")
        w_data.write("数据展示")
        w_data.write("</title>")
        w_data.write("<link href='main.css' rel='stylesheet' type='text/css'>")
        w_data.write("</head>")
        w_data.write("<body>")
        w_data.write("<h1>结果</h1><br>")
        w_data.write("<table>")
        w_data.write("<tr>")
        w_data.write("<td>"+"日期："+"</td>")
        w_data.write("<td>"+"时间："+"</td>")
        w_data.write("<td>"+"动作："+"</td>")
        w_data.write("<td>"+"路径："+"</td>")
        w_data.write("<td>"+"文件："+"</td>")
        w_data.write("</tr>")
    
#     写入网页结尾
    def writeHtmlEnd(self,w_data):
        w_data.write("</table>")
        w_data.write("</body>")
        w_data.write("</html>")
    
#      设置css样式
    def setCss(self,writePath):
        print(writePath+"/"+"main.css")
        wr = open(writePath+"/"+"main.css","w")
        wr.write("@CHARSET 'UTF-8';")
        wr.write("table{color:black;}")
        wr.write("tr{border: 1px solid red;}")
        wr.write("td{border: 1px solid red;}")
        wr.close()