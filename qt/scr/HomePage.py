# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1286, 884)
        mainWindow.setMinimumSize(QtCore.QSize(1286, 884))
        mainWindow.setMaximumSize(QtCore.QSize(1286, 884))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet("/*全局样式*/\n"
"/*{    \n"
"    font-family:微软雅黑;\n"
"    font-size:16px;\n"
"    background-color:#c2ccd0;                                                    \n"
"}*/\n"
"*{\n"
"    background-color:#c2ccd0;                                                    \n"
"}\n"
"\n"
"Ltitle{    \n"
"    font-family:微软雅黑;\n"
"    font-size:24px;\n"
"    background-color:#c2ccd0;                                                    \n"
"}\n"
"\n"
"/*按钮样式*/\n"
"QPushButton{   \n"
"\n"
"font-size:25px;    \n"
" \n"
"border:3px outset rgb(125, 125, 125);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" background-color:rgb(125, 125, 125);  \n"
" border:3px outset rgb(125, 125, 125);\n"
"}\n"
"\n"
"/*QTableView 左上角样式*/\n"
"QTableView QTableCornerButton::section {\n"
"   /*  background: red;\n"
"    border: 2px outset red;*/\n"
"    color: red;\n"
"    background-color: rgb(64, 64, 64);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color: rgb(64, 64, 64);\n"
" }\n"
"\n"
" QTableView {\n"
"    color: white;                                       /*表格内文字颜色*/\n"
"    gridline-color: black;                              /*表格内框颜色*/\n"
"    background-color: #bacac6;               /*表格内背景色*/\n"
"    alternate-background-color: rgb(64, 64, 64);\n"
"    selection-color: white;                             /*选中区域的文字颜色*/\n"
"    selection-background-color: #808080;        /*选中区域的背景色*/\n"
"    border: 2px groove gray;\n"
"    border-radius: 0px;\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: #75878a;\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color: rgb(64, 64, 64);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color: rgb(64, 64, 64);\n"
"} \n"
"QRadioButton::indicator {width:15px;height:15px;border-radius:7px}\n"
"QRadioButton::indicator:checked {background-color:green;}\n"
"QRadioButton::indicator:unchecked {background-color:red;}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.Ltitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光黑变_CNKI")
        font.setPointSize(20)
        self.Ltitle.setFont(font)
        self.Ltitle.setObjectName("Ltitle")
        self.horizontalLayout_20.addWidget(self.Ltitle)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.verticalLayout_8.addLayout(self.horizontalLayout_20)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.Edit_IP = QtWidgets.QLineEdit(self.frame)
        self.Edit_IP.setMinimumSize(QtCore.QSize(335, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Edit_IP.setFont(font)
        self.Edit_IP.setObjectName("Edit_IP")
        self.horizontalLayout_2.addWidget(self.Edit_IP)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setMinimumSize(QtCore.QSize(189, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.Edit_Port = QtWidgets.QLineEdit(self.frame)
        self.Edit_Port.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Edit_Port.setFont(font)
        self.Edit_Port.setObjectName("Edit_Port")
        self.horizontalLayout.addWidget(self.Edit_Port)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_IP = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_IP.setFont(font)
        self.label_IP.setObjectName("label_IP")
        self.horizontalLayout_3.addWidget(self.label_IP)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.Local_Port = QtWidgets.QLineEdit(self.frame)
        self.Local_Port.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Local_Port.setFont(font)
        self.Local_Port.setObjectName("Local_Port")
        self.horizontalLayout_4.addWidget(self.Local_Port)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lradioButton_ConnectionStatus = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lradioButton_ConnectionStatus.setFont(font)
        self.lradioButton_ConnectionStatus.setObjectName("lradioButton_ConnectionStatus")
        self.horizontalLayout_5.addWidget(self.lradioButton_ConnectionStatus)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.radioButton_RunningStatus = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_RunningStatus.setFont(font)
        self.radioButton_RunningStatus.setObjectName("radioButton_RunningStatus")
        self.horizontalLayout_6.addWidget(self.radioButton_RunningStatus)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.ResetButton = QtWidgets.QPushButton(self.frame)
        self.ResetButton.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ResetButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/xin/.designer/backup/icon/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ResetButton.setIcon(icon)
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout_9.addWidget(self.ResetButton)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8.addWidget(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("ESRI North")
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.Data_a = QtWidgets.QLineEdit(self.tab_3)
        self.Data_a.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Data_a.setFont(font)
        self.Data_a.setObjectName("Data_a")
        self.horizontalLayout_10.addWidget(self.Data_a)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.Data_b = QtWidgets.QLineEdit(self.tab_3)
        self.Data_b.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Data_b.setFont(font)
        self.Data_b.setObjectName("Data_b")
        self.horizontalLayout_11.addWidget(self.Data_b)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.Tab3_ResetButton = QtWidgets.QPushButton(self.tab_3)
        self.Tab3_ResetButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Tab3_ResetButton.setFont(font)
        self.Tab3_ResetButton.setIcon(icon)
        self.Tab3_ResetButton.setObjectName("Tab3_ResetButton")
        self.verticalLayout_2.addWidget(self.Tab3_ResetButton)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.Tab4_StartButton = QtWidgets.QPushButton(self.tab_4)
        self.Tab4_StartButton.setMinimumSize(QtCore.QSize(0, 80))
        self.Tab4_StartButton.setIcon(icon)
        self.Tab4_StartButton.setObjectName("Tab4_StartButton")
        self.verticalLayout_3.addWidget(self.Tab4_StartButton)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(11, 11, 402, 442))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setMinimumSize(QtCore.QSize(400, 400))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(426, 11, 821, 441))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.label_rollLocation = QtWidgets.QLabel(self.widget1)
        self.label_rollLocation.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_rollLocation.setFont(font)
        self.label_rollLocation.setObjectName("label_rollLocation")
        self.horizontalLayout_13.addWidget(self.label_rollLocation)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.Tab1_ResetButton = QtWidgets.QPushButton(self.widget1)
        self.Tab1_ResetButton.setMinimumSize(QtCore.QSize(0, 80))
        self.Tab1_ResetButton.setIcon(icon)
        self.Tab1_ResetButton.setObjectName("Tab1_ResetButton")
        self.verticalLayout_5.addWidget(self.Tab1_ResetButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget2 = QtWidgets.QWidget(self.tab_2)
        self.widget2.setGeometry(QtCore.QRect(11, 11, 402, 442))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget2)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(400, 400))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(400, 400))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_6.addWidget(self.graphicsView_2)
        self.label_19 = QtWidgets.QLabel(self.widget2)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.widget3 = QtWidgets.QWidget(self.tab_2)
        self.widget3.setGeometry(QtCore.QRect(426, 11, 821, 431))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.widget3)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.label_TheEndPointOfThePath = QtWidgets.QLabel(self.widget3)
        self.label_TheEndPointOfThePath.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_TheEndPointOfThePath.setFont(font)
        self.label_TheEndPointOfThePath.setObjectName("label_TheEndPointOfThePath")
        self.horizontalLayout_16.addWidget(self.label_TheEndPointOfThePath)
        self.verticalLayout_7.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.label_ThePathStartPoint = QtWidgets.QLabel(self.widget3)
        self.label_ThePathStartPoint.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_ThePathStartPoint.setFont(font)
        self.label_ThePathStartPoint.setObjectName("label_ThePathStartPoint")
        self.horizontalLayout_17.addWidget(self.label_ThePathStartPoint)
        self.verticalLayout_7.addLayout(self.horizontalLayout_17)
        self.Tab2_ResetButton = QtWidgets.QPushButton(self.widget3)
        self.Tab2_ResetButton.setMinimumSize(QtCore.QSize(0, 80))
        self.Tab2_ResetButton.setIcon(icon)
        self.Tab2_ResetButton.setObjectName("Tab2_ResetButton")
        self.verticalLayout_7.addWidget(self.Tab2_ResetButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.TerminatesTheCurrentTask = QtWidgets.QPushButton(self.centralwidget)
        self.TerminatesTheCurrentTask.setMinimumSize(QtCore.QSize(0, 50))
        self.TerminatesTheCurrentTask.setIcon(icon)
        self.TerminatesTheCurrentTask.setObjectName("TerminatesTheCurrentTask")
        self.horizontalLayout_19.addWidget(self.TerminatesTheCurrentTask)
        self.endButton = QtWidgets.QPushButton(self.centralwidget)
        self.endButton.setMinimumSize(QtCore.QSize(0, 50))
        self.endButton.setIcon(icon)
        self.endButton.setObjectName("endButton")
        self.horizontalLayout_19.addWidget(self.endButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1286, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "运动物体监测系统"))
        self.Ltitle.setText(_translate("mainWindow", "运动物体监测系统-V1.0.0"))
        self.label_20.setText(_translate("mainWindow", " 成员： 杜若甫 贺韩冰马俊豪 "))
        self.label_10.setText(_translate("mainWindow", "下位机地址："))
        self.Edit_IP.setText(_translate("mainWindow", "0.00"))
        self.label_12.setText(_translate("mainWindow", "下位机端口："))
        self.Edit_Port.setText(_translate("mainWindow", "0.00"))
        self.label_4.setText(_translate("mainWindow", "本机IP地址："))
        self.label_IP.setText(_translate("mainWindow", "127.00.00.000       "))
        self.label_3.setText(_translate("mainWindow", "监听的端口："))
        self.Local_Port.setText(_translate("mainWindow", "8080"))
        self.label.setText(_translate("mainWindow", "下位机连接状态"))
        self.lradioButton_ConnectionStatus.setText(_translate("mainWindow", "未连接"))
        self.label_2.setText(_translate("mainWindow", "下位机运行状态"))
        self.radioButton_RunningStatus.setText(_translate("mainWindow", "OFF"))
        self.ResetButton.setText(_translate("mainWindow", "监听/重置连接"))
        self.label_9.setText(_translate("mainWindow", "   α角度："))
        self.Data_a.setText(_translate("mainWindow", "0.00"))
        self.label_17.setText(_translate("mainWindow", "°"))
        self.label_11.setText(_translate("mainWindow", "   β角度："))
        self.Data_b.setText(_translate("mainWindow", "0.00"))
        self.label_15.setText(_translate("mainWindow", "°"))
        self.Tab3_ResetButton.setText(_translate("mainWindow", "复位"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "角度计算"))
        self.label_5.setText(_translate("mainWindow", "     当前朝上面："))
        self.label_7.setText(_translate("mainWindow", "       TextLabel"))
        self.Tab4_StartButton.setText(_translate("mainWindow", "测量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("mainWindow", "测试当前面"))
        self.label_18.setText(_translate("mainWindow", "    实时路径"))
        self.label_6.setText(_translate("mainWindow", "当前路径："))
        self.label_rollLocation.setText(_translate("mainWindow", "当前路径"))
        self.label_13.setText(_translate("mainWindow", "当前朝上面："))
        self.label_8.setText(_translate("mainWindow", "TextLabel"))
        self.Tab1_ResetButton.setText(_translate("mainWindow", "复位"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "翻滚测试"))
        self.label_19.setText(_translate("mainWindow", "      预测结果"))
        self.label_14.setText(_translate("mainWindow", "   路径终点(红色)："))
        self.label_TheEndPointOfThePath.setText(_translate("mainWindow", "    待计算"))
        self.label_16.setText(_translate("mainWindow", "   路径起点(绿色)："))
        self.label_ThePathStartPoint.setText(_translate("mainWindow", "    待计算"))
        self.Tab2_ResetButton.setText(_translate("mainWindow", "复位"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "平移测试"))
        self.TerminatesTheCurrentTask.setText(_translate("mainWindow", "结束当前任务"))
        self.endButton.setText(_translate("mainWindow", "退出"))
