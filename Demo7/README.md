# 前言
参考：https://zhuanlan.zhihu.com/p/341564754

## UI设计
QtDesigner建了个MainWindow，添加了Label控件，修改了控件文本；  
添加了push button按钮控件，修改了其objectName为pushButton1    
添加了Label控件，改名为 label_img
添加了lineEdit 可以编辑的文本框，和对应的pushButton2  
增加menu餐单栏的一级二级餐单  

## UI源码生成
pyuic5 -o demo.py demo.ui  生成UI源码  

## 功能描述
main.py编写了相关的信号和槽函数，实现按钮点击修改label文本的功能；  
点击 pushButton2 将 lineEdit的文本赋值给 Label  
点击 餐单栏的Edit->Undo 将 lineEdit的文本赋值给 Label  
点击 餐单栏的Edit->Open 读取文件信息  
点击 餐单栏的Edit->Save 将 lineEdit的文本写入Save配置的文件中    

## 运行
python main.py 运行程序  