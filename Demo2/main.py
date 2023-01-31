# 参考：https://zhuanlan.zhihu.com/p/341799530
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import demo2


class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = demo2.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

    # 槽函数
    def pushButton1_func(self):
        # 修改label的文本为 123
        self.ui.label.setText("123")

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        # pushButton1点击事件连接槽函数pushButton1_func
        self.ui.pushButton1.clicked.connect(self.pushButton1_func)
        self.show()


# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())