from ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QPushButton
import sys
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
import webbrowser
class UtilWindowUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UtilWindowUI,self).__init__()
        self.setupUi(self)
        self.dragging = False
        self.pushButton_6.clicked.connect(self.download)
        self.pushButton_13.clicked.connect(self.launch)
        self.pushButton_5.clicked.connect(self.setting)
        self.pushButton_14.clicked.connect(self.launch)
        self.pushButton_2.clicked.connect(self.download_mod_)
        self.pushButton.clicked.connect(self.download_auto)
        self.pushButton_11.clicked.connect(self.setting_version)
        self.pushButton_12.clicked.connect(self.setting_launcher)
        self.pushButton_10.clicked.connect(self.setting_about)
        self.pushButton_8.clicked.connect(self.setting_version_about)
        self.pushButton_4.clicked.connect(self.setting_version)
        self.pushButton_3.clicked.connect(self.setting_about)
        self.pushButton_18.clicked.connect(self.bilibili)
        self.pushButton_22.clicked.connect(self.web)
        self.pushButton_19.clicked.connect(self.launcher_title)
        self.pushButton_23.clicked.connect(self.launcher_title_1)
        self.anim = QPropertyAnimation(self.stackedWidget, b"geometry")
        self.anim2 = QPropertyAnimation(self.stackedWidget_2, b"geometry")

    

        self.timer = QTimer(self)# 1秒钟调用一次
        self.timer.timeout.connect(self.mouse_closs)
        self.timer.start()

        self.timer_2 = QTimer(self)# 1秒钟调用一次
        self.timer_2.timeout.connect(self.mouse_close_2)
        self.timer_2.start()

        # 自定义标题栏
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 标题栏部件
        self.titleBar = QtWidgets.QWidget(self)
        self.titleBar.setGeometry(0, 0, 906, 50)
        self.titleBar.setStyleSheet("background-color: rgba(244, 255, 239, 128)")

        # 标题标签
        self.titleLabel = QtWidgets.QLabel(self.titleBar)
        self.titleLabel.setText("River Minecraft Launcher v2.0")
        self.titleLabel.move(10, 15)
        font = QFont()
        font.setFamily("庞门正道标题体3.0")
        font.setPointSize(12)
        self.titleLabel.setFont(font)

        # 最小化按钮
        self.minimizeButton = QtWidgets.QPushButton(self.titleBar)
        self.minimizeButton.setIcon(QIcon('assets\icon\minimize.png'))
        self.minimizeButton.setGeometry(809, 0, 50,50)
        self.minimizeButton.clicked.connect(self.showMinimized)
        self.minimizeButton.setStyleSheet('border:none')

        # 关闭按钮
        self.closeButton = QtWidgets.QPushButton(self.titleBar)
        self.closeButton.setIcon(QIcon('assets\\icon\\quit.png'))
        self.closeButton.setIconSize(QtCore.QSize(25,25))
        self.closeButton.setGeometry(856, 0, 50, 50)
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setStyleSheet('border:none')



    def bilibili(self):
        webbrowser.open_new_tab('https://space.bilibili.com/521877155')
    def web(self):
        webbrowser.open_new_tab('rmcl.mdss6.com')

    def launcher_title(self):
        title = self.lineEdit_5.text()
        if title == '':
            self.lineEdit_5.setPlaceholderText('没有文本')
        else:
            self.titleLabel.setText(title)
    def launcher_title_1(self):
        self.titleLabel.setText("RiverMinecraftLauncher v2.0")




        # 定义一个方法来处理鼠标按下事件
    def mousePressEvent(self, event):
        # 检查是否在标题栏上按下鼠标左键
        if event.button() == QtCore.Qt.LeftButton and self.titleBar.underMouse():
            # 设置一个标志来表示窗口正在被拖动
            self.dragging = True
            # 记录鼠标和窗口的初始位置
            self.mousePos = event.globalPos()
            self.windowPos = self.pos()

    
    def mouse_closs(self):
        # 检查是否在标题栏上按下鼠标左键
        if self.closeButton.underMouse():
            self.closeButton.setIcon(QIcon('assets\\icon\\quit_2.png'))
        else:
            self.closeButton.setIcon(QIcon('assets\\icon\\quit.png'))

    def mouse_close_2(self):
        if self.minimizeButton.underMouse():
            self.minimizeButton.setIcon(QIcon('assets\\icon\\minimize_2.png'))
        else:
            self.minimizeButton.setIcon(QIcon('assets\\icon\\minimize.png'))




    def mouseMoveEvent(self, event):
        # 检查窗口是否正在被拖动
        if self.dragging:
            # 计算鼠标移动的偏移量
            offset = event.globalPos() - self.mousePos
            # 将窗口移动到新的位置
            self.move(self.windowPos + offset)

    # 定义一个方法来处理鼠标释放事件
    def mouseReleaseEvent(self, event):
        # 检查是否在标题栏上释放鼠标左键
        if event.button() == QtCore.Qt.LeftButton and self.titleBar.underMouse():
            # 重置标志来表示窗口不再被拖动
            self.dragging = False
    
    

    def download(self): 
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)

    def launch(self):
       
        self.stackedWidget.setCurrentIndex(0)

   
    def setting(self):
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)

    def download_mod_(self):

        self.stackedWidget_2.setCurrentIndex(0)

    def download_auto(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def setting_version(self):
        self.stackedWidget.setCurrentIndex(2)

        self.stackedWidget_3.setCurrentIndex(1)

    def setting_launcher(self):
        self.stackedWidget_3.setCurrentIndex(0)

    def setting_about(self):
        self.stackedWidget_3.setCurrentIndex(2)

    def setting_version_about(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(3)
    
    #以上方法都是切换页面




    
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = UtilWindowUI()
    widget.show()
    sys.exit(app.exec_())
    
