# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_case_gen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(320, 20, 791, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setText("欢迎使用测试样例生成系统，请选择测试用例具体生成要求")
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setObjectName("title")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 230, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(501, 381, 199, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.data_request_low = QtWidgets.QLineEdit(self.centralwidget)
        self.data_request_low.setGeometry(QtCore.QRect(709, 382, 51, 21))
        self.data_request_low.setObjectName("data_request_low")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(470, 510, 171, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.data_request_high = QtWidgets.QLineEdit(self.centralwidget)
        self.data_request_high.setGeometry(QtCore.QRect(790, 380, 51, 21))
        self.data_request_high.setObjectName("data_request_high")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(740, 510, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.list_num_request_low = QtWidgets.QLineEdit(self.centralwidget)
        self.list_num_request_low.setGeometry(QtCore.QRect(679, 512, 51, 21))
        self.list_num_request_low.setClearButtonEnabled(False)
        self.list_num_request_low.setObjectName("list_num_request_low")
        self.list_num_request_high = QtWidgets.QLineEdit(self.centralwidget)
        self.list_num_request_high.setGeometry(QtCore.QRect(760, 510, 51, 21))
        self.list_num_request_high.setObjectName("list_num_request_high")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 320, 194, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.int_choose = QtWidgets.QRadioButton(self.layoutWidget)
        self.int_choose.setObjectName("int_choose")
        self.horizontalLayout_5.addWidget(self.int_choose)
        self.str_choose = QtWidgets.QRadioButton(self.layoutWidget)
        self.str_choose.setObjectName("str_choose")
        self.horizontalLayout_5.addWidget(self.str_choose)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(770, 380, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(520, 560, 123, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.list_extra_request = QtWidgets.QComboBox(self.centralwidget)
        self.list_extra_request.setGeometry(QtCore.QRect(700, 550, 101, 32))
        self.list_extra_request.setObjectName("list_extra_request")
        self.list_extra_request.addItem("")
        self.list_extra_request.setItemText(0, "")
        self.list_extra_request.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.odd_choose = QtWidgets.QComboBox(self.centralwidget)
        self.odd_choose.setGeometry(QtCore.QRect(680, 420, 81, 32))
        self.odd_choose.setObjectName("odd_choose")
        self.odd_choose.addItem("")
        self.odd_choose.setItemText(0, "")
        self.odd_choose.addItem("")
        self.odd_choose.addItem("")
        self.positive_choose = QtWidgets.QComboBox(self.centralwidget)
        self.positive_choose.setGeometry(QtCore.QRect(820, 420, 91, 32))
        self.positive_choose.setObjectName("positive_choose")
        self.positive_choose.addItem("")
        self.positive_choose.setItemText(0, "")
        self.positive_choose.addItem("")
        self.positive_choose.addItem("")
        self.prime_choose = QtWidgets.QComboBox(self.centralwidget)
        self.prime_choose.setGeometry(QtCore.QRect(960, 420, 81, 32))
        self.prime_choose.setObjectName("prime_choose")
        self.prime_choose.addItem("")
        self.prime_choose.setItemText(0, "")
        self.prime_choose.addItem("")
        self.list_request_title = QtWidgets.QLabel(self.centralwidget)
        self.list_request_title.setGeometry(QtCore.QRect(440, 470, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.list_request_title.setFont(font)
        self.list_request_title.setObjectName("list_request_title")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(501, 422, 123, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.functionname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.functionname_edit.setGeometry(QtCore.QRect(615, 110, 81, 21))
        self.functionname_edit.setObjectName("functionname_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 110, 77, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.paracount = QtWidgets.QComboBox(self.centralwidget)
        self.paracount.setGeometry(QtCore.QRect(637, 148, 63, 32))
        self.paracount.setObjectName("paracount")
        self.paracount.addItem("")
        self.paracount.addItem("")
        self.paracount.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 150, 92, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(532, 72, 123, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gn_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.gn_edit.setGeometry(QtCore.QRect(663, 72, 81, 21))
        self.gn_edit.setObjectName("gn_edit")
        self.closeWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeWinBtn.setGeometry(QtCore.QRect(900, 100, 113, 32))
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(550, 230, 115, 20))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.element_choose = QtWidgets.QRadioButton(self.layoutWidget1)
        self.element_choose.setObjectName("element_choose")
        self.horizontalLayout.addWidget(self.element_choose)
        self.list_choose = QtWidgets.QRadioButton(self.layoutWidget1)
        self.list_choose.setObjectName("list_choose")
        self.horizontalLayout.addWidget(self.list_choose)
        self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(540, 620, 113, 32))
        self.confirm_btn.setObjectName("confirm_btn")
        self.dec_inc_choose = QtWidgets.QComboBox(self.centralwidget)
        self.dec_inc_choose.setGeometry(QtCore.QRect(890, 550, 91, 32))
        self.dec_inc_choose.setObjectName("dec_inc_choose")
        self.dec_inc_choose.addItem("")
        self.dec_inc_choose.setItemText(0, "")
        self.dec_inc_choose.addItem("")
        self.dec_inc_choose.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(641, 422, 40, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(783, 422, 27, 16))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(920, 420, 40, 16))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(620, 560, 71, 16))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(830, 560, 60, 16))
        self.label_14.setObjectName("label_14")
        self.Request_of_who = QtWidgets.QLabel(self.centralwidget)
        self.Request_of_who.setGeometry(QtCore.QRect(270, 180, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Request_of_who.setFont(font)
        self.Request_of_who.setObjectName("Request_of_who")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closeWinBtn.clicked.connect(MainWindow.close) # type: ignore
        self.element_choose.clicked['bool'].connect(self.list_num_request_low.setDisabled) # type: ignore
        self.element_choose.clicked['bool'].connect(self.list_num_request_high.setDisabled) # type: ignore
        self.element_choose.clicked['bool'].connect(self.list_extra_request.setDisabled) # type: ignore
        self.list_choose.clicked['bool'].connect(self.list_extra_request.setEnabled) # type: ignore
        self.list_choose.clicked['bool'].connect(self.list_num_request_low.setEnabled) # type: ignore
        self.list_choose.clicked['bool'].connect(self.list_num_request_high.setEnabled) # type: ignore
        self.int_choose.clicked['bool'].connect(self.data_request_low.setEnabled) # type: ignore
        self.int_choose.clicked['bool'].connect(self.data_request_high.setEnabled) # type: ignore
        self.str_choose.clicked['bool'].connect(self.data_request_high.setDisabled) # type: ignore
        self.str_choose.clicked['bool'].connect(self.data_request_low.setDisabled) # type: ignore
        self.str_choose.clicked['bool'].connect(self.odd_choose.setDisabled) # type: ignore
        self.str_choose.clicked['bool'].connect(self.positive_choose.setDisabled) # type: ignore
        self.str_choose.clicked['bool'].connect(self.prime_choose.setDisabled) # type: ignore
        self.int_choose.clicked['bool'].connect(self.odd_choose.setEnabled) # type: ignore
        self.int_choose.clicked['bool'].connect(self.positive_choose.setEnabled) # type: ignore
        self.int_choose.clicked['bool'].connect(self.prime_choose.setEnabled) # type: ignore
        self.str_choose.clicked['bool'].connect(self.dec_inc_choose.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "参数类型："))
        self.label_7.setText(_translate("MainWindow", "数据范围：（int类型必选）"))
        self.label_16.setText(_translate("MainWindow", "列表元素个数限制(必选）："))
        self.label_17.setText(_translate("MainWindow", "~"))
        self.int_choose.setText(_translate("MainWindow", "int"))
        self.str_choose.setText(_translate("MainWindow", "str"))
        self.label_8.setText(_translate("MainWindow", "~"))
        self.label_13.setText(_translate("MainWindow", "列表特殊要求"))
        self.list_extra_request.setItemText(1, _translate("MainWindow", "exclusive"))
        self.label_11.setText(_translate("MainWindow", "元素要求（必选）："))
        self.odd_choose.setItemText(1, _translate("MainWindow", "even"))
        self.odd_choose.setItemText(2, _translate("MainWindow", "odd"))
        self.positive_choose.setItemText(1, _translate("MainWindow", "positive"))
        self.positive_choose.setItemText(2, _translate("MainWindow", "negative"))
        self.prime_choose.setItemText(1, _translate("MainWindow", "prime"))
        self.list_request_title.setText(_translate("MainWindow", "列表要求（不是列表则忽略）："))
        self.label_9.setText(_translate("MainWindow", "元素数据特殊要求"))
        self.label_3.setText(_translate("MainWindow", "测试函数名"))
        self.paracount.setItemText(0, _translate("MainWindow", "1"))
        self.paracount.setItemText(1, _translate("MainWindow", "2"))
        self.paracount.setItemText(2, _translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "函数参数个数"))
        self.label.setText(_translate("MainWindow", "生成测试样例个数"))
        self.closeWinBtn.setText(_translate("MainWindow", "关闭窗口"))
        self.element_choose.setText(_translate("MainWindow", "元素"))
        self.list_choose.setText(_translate("MainWindow", "列表"))
        self.confirm_btn.setText(_translate("MainWindow", "下一个"))
        self.dec_inc_choose.setItemText(1, _translate("MainWindow", "dec"))
        self.dec_inc_choose.setItemText(2, _translate("MainWindow", "inc"))
        self.label_2.setText(_translate("MainWindow", "奇偶："))
        self.label_6.setText(_translate("MainWindow", "正负"))
        self.label_10.setText(_translate("MainWindow", "素数："))
        self.label_12.setText(_translate("MainWindow", "可否重复："))
        self.label_14.setText(_translate("MainWindow", "升降序："))
        self.Request_of_who.setText(_translate("MainWindow", "第1个参数要求："))
