# Form implementation generated from reading ui file 'tool_01DIY85_ui.ui',
# licensing of 'tool_01DIY85_ui.ui' applies.
#
# Created: Wed Jun 26 17:47:36 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(1124, 567)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName('gridLayout')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName('label')
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.pB_ON = QtWidgets.QPushButton(self.centralwidget)
        self.pB_ON.setObjectName('pB_ON')
        self.horizontalLayout.addWidget(self.pB_ON)
        self.pB_OFF = QtWidgets.QPushButton(self.centralwidget)
        self.pB_OFF.setObjectName('pB_OFF')
        self.horizontalLayout.addWidget(self.pB_OFF)
        self.pB_UP_ON = QtWidgets.QPushButton(self.centralwidget)
        self.pB_UP_ON.setObjectName('pB_UP_ON')
        self.horizontalLayout.addWidget(self.pB_UP_ON)
        self.pB_UP_KEEP = QtWidgets.QPushButton(self.centralwidget)
        self.pB_UP_KEEP.setObjectName('pB_UP_KEEP')
        self.horizontalLayout.addWidget(self.pB_UP_KEEP)
        self.pB_UP_OFF = QtWidgets.QPushButton(self.centralwidget)
        self.pB_UP_OFF.setObjectName('pB_UP_OFF')
        self.horizontalLayout.addWidget(self.pB_UP_OFF)
        self.pB_SET_POINT = QtWidgets.QPushButton(self.centralwidget)
        self.pB_SET_POINT.setObjectName('pB_SET_POINT')
        self.horizontalLayout.addWidget(self.pB_SET_POINT)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.pB_info = QtWidgets.QPushButton(self.centralwidget)
        self.pB_info.setObjectName('pB_info')
        self.horizontalLayout.addWidget(self.pB_info)
        self.pB_signal = QtWidgets.QPushButton(self.centralwidget)
        self.pB_signal.setObjectName('pB_signal')
        self.horizontalLayout.addWidget(self.pB_signal)
        self.ROOT = QtWidgets.QPushButton(self.centralwidget)
        self.ROOT.setObjectName('ROOT')
        self.horizontalLayout.addWidget(self.ROOT)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName('tableWidget')
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.pB_all = QtWidgets.QPushButton(self.centralwidget)
        self.pB_all.setObjectName('pB_all')
        self.horizontalLayout_2.addWidget(self.pB_all)
        self.pB_inverse = QtWidgets.QPushButton(self.centralwidget)
        self.pB_inverse.setObjectName('pB_inverse')
        self.horizontalLayout_2.addWidget(self.pB_inverse)
        self.pB_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pB_cancel.setObjectName('pB_cancel')
        self.horizontalLayout_2.addWidget(self.pB_cancel)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.MODIFY_SSID_PASSWORD = QtWidgets.QPushButton(self.centralwidget)
        self.MODIFY_SSID_PASSWORD.setObjectName('MODIFY_SSID_PASSWORD')
        self.horizontalLayout_2.addWidget(self.MODIFY_SSID_PASSWORD)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate(
                'MainWindow', 'MainWindow', None, -1
            )
        )
        self.label.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'DIY mode tool', None, -1
            )
        )
        self.pB_ON.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'ON', None, -1
            )
        )
        self.pB_OFF.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'OFF', None, -1
            )
        )
        self.pB_UP_ON.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Power-on-state-ON', None, -1
            )
        )
        self.pB_UP_KEEP.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Power-on-state-KEEP', None, -1
            )
        )
        self.pB_UP_OFF.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Power-on-state-OFF', None, -1
            )
        )
        self.pB_SET_POINT.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Batch Inching Setting', None, -1
            )
        )
        self.pB_info.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Info', None, -1
            )
        )
        self.pB_signal.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Signal', None, -1
            )
        )
        self.ROOT.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Firmware flash', None, -1
            )
        )
        self.pB_all.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Select all', None, -1
            )
        )
        self.pB_inverse.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Inverse selection', None, -1
            )
        )
        self.pB_cancel.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'Cancel selection', None, -1
            )
        )
        self.MODIFY_SSID_PASSWORD.setText(
            QtWidgets.QApplication.translate(
                'MainWindow', 'change SSID & Password', None, -1
            )
        )
