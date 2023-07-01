# pyinstaller -D -w main.py -i main.ico -y
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from HomePageHandle import HomePage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../resources/img/icon/图标.png'))
    # 实例化主页面
    win_1 = HomePage()
    # 开启主页面
    win_1.show()
    sys.exit(app.exec_())


