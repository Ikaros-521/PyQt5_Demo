QtDesigner建了个MainWindow，添加了Label控件，修改了控件文本；  
添加了push button按钮控件，修改了其objectName为pushButton1      
pyuic5 -o demo2.py demo2.ui  生成UI源码  
main.py编写了相关的信号和槽函数，实现按钮点击修改label文本的功能  
python main.py 运行程序  