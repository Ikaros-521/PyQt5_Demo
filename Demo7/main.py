# 参考：https://zhuanlan.zhihu.com/p/341799530
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import demo


class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = demo.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

    # 槽函数
    def pushButton1_func(self):
        # 修改label的文本为 123
        self.ui.label.setText("123")

    # 槽函数
    def pushButton2_func(self):
        # 修改label的文本为 lineEdit 的内容
        self.ui.label.setText(self.ui.lineEdit.text())

    # 槽函数
    def actionUndo_triggered(self):
        # 修改label的文本为 lineEdit 的内容
        self.ui.label.setText(self.ui.lineEdit.text())

    def pushButton_down_func(self):
        last_index = self.ui.stackedWidget.count() - 1
        # 判断如果是最后一页就不允许往后翻页
        if self.ui.stackedWidget.currentIndex() == last_index:
            return
        target_index = self.ui.stackedWidget.currentIndex() + 1
        self.ui.stackedWidget.setCurrentIndex(target_index)

    def pushButton_up_func(self):
        # 判断如果是第一页就不允许往前翻页
        if self.ui.stackedWidget.currentIndex() == 0:
            return
        target_index = self.ui.stackedWidget.currentIndex() - 1
        self.ui.stackedWidget.setCurrentIndex(target_index)

    def actionOpen_triggered(self):
        # 存储着 文件绝对路径 和 文件类型
        file_info = QFileDialog.getOpenFileName(self, "选择txt文件", os.getcwd(), "txt files(*.txt)")
        print(file_info)

        # 打开文件读取内容
        f = open(file_info[0], 'r', encoding='utf8')
        content = f.read()
        f.close()
        print(content)

        self.ui.label_img.setText(content)

    def actionSave_triggered(self):
        file_info = QFileDialog.getSaveFileName(self, "保存文件", os.getcwd() + "/未命名", "txt files(*.txt)")

        # 打开文件 没有就创建，有就清空 准备写入
        f = open(file_info[0], 'w', encoding='utf8')
        # 获取lineEdit的文本写入文件
        f.write(self.ui.lineEdit.text())
        f.close()


    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        # pushButton1点击事件连接槽函数pushButton1_func
        self.ui.pushButton1.clicked.connect(self.pushButton1_func)

        icon = QPixmap('static/1.png')
        self.ui.label_img.setPixmap(icon)

        self.ui.pushButton2.clicked.connect(self.pushButton2_func)

        self.ui.actionUndo.triggered.connect(self.actionUndo_triggered)
        # 设置快捷键
        self.ui.actionUndo.setShortcut('Ctrl+E')

        # File -> Open
        self.ui.actionOpen.triggered.connect(self.actionOpen_triggered)
        self.ui.actionOpen.setShortcut('Ctrl+O')

        # File -> Save
        self.ui.actionSave.triggered.connect(self.actionSave_triggered)
        self.ui.actionSave.setShortcut('Ctrl+S')

        self.ui.pushButton_up1.clicked.connect(self.pushButton_up_func)
        self.ui.pushButton_up2.clicked.connect(self.pushButton_up_func)
        self.ui.pushButton_down1.clicked.connect(self.pushButton_down_func)
        self.ui.pushButton_down2.clicked.connect(self.pushButton_down_func)

        self.show()


# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())