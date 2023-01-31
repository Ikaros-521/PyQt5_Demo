# 参考：https://zhuanlan.zhihu.com/p/341564754
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import demo1


class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = demo1.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.show()


# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())