# 参考：https://zhuanlan.zhihu.com/p/341799530
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
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
    def actionOpen_triggered(self):
        # 修改label的文本为 lineEdit 的内容
        self.ui.label.setText(self.ui.lineEdit.text())

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        # pushButton1点击事件连接槽函数pushButton1_func
        self.ui.pushButton1.clicked.connect(self.pushButton1_func)

        icon = QPixmap('static/1.png')
        self.ui.label_img.setPixmap(icon)

        self.ui.pushButton2.clicked.connect(self.pushButton2_func)

        self.ui.actionOpen.triggered.connect(self.actionOpen_triggered)
        # 设置快捷键
        self.ui.actionOpen.setShortcut('Ctrl+O')

        self.show()


# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())