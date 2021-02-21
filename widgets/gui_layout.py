# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_layout.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 974)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"eplink_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionLoad_data = QAction(MainWindow)
        self.actionLoad_data.setObjectName(u"actionLoad_data")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        self.actionLoad_data.setFont(font1)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setFont(font1)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionSettings.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 700))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMinimumSize(QSize(1100, 450))
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(True)
        self.widget_6 = QWidget(self.splitter)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(1100, 200))
        self.gridLayout_3 = QGridLayout(self.widget_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(200, 0))
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.loadDirButton = QPushButton(self.widget_4)
        self.loadDirButton.setObjectName(u"loadDirButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loadDirButton.sizePolicy().hasHeightForWidth())
        self.loadDirButton.setSizePolicy(sizePolicy2)
        self.loadDirButton.setMinimumSize(QSize(150, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.loadDirButton.setFont(font2)
        self.loadDirButton.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.loadDirButton, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 226, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 0, 0, 1, 1)

        self.treeViewLoad = QTreeWidget(self.widget_6)
        self.treeViewLoad.setObjectName(u"treeViewLoad")
        sizePolicy1.setHeightForWidth(self.treeViewLoad.sizePolicy().hasHeightForWidth())
        self.treeViewLoad.setSizePolicy(sizePolicy1)
        self.treeViewLoad.setMinimumSize(QSize(1000, 0))
        self.treeViewLoad.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        self.treeViewLoad.setFont(font3)
        self.treeViewLoad.setContextMenuPolicy(Qt.PreventContextMenu)
        self.treeViewLoad.setAcceptDrops(True)
        self.treeViewLoad.setAutoFillBackground(True)
        self.treeViewLoad.setFrameShape(QFrame.Box)
        self.treeViewLoad.setFrameShadow(QFrame.Sunken)
        self.treeViewLoad.setLineWidth(1)
        self.treeViewLoad.setMidLineWidth(1)
        self.treeViewLoad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeViewLoad.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.treeViewLoad.setAlternatingRowColors(True)
        self.treeViewLoad.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeViewLoad.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeViewLoad.setAnimated(False)
        self.treeViewLoad.setColumnCount(0)
        self.treeViewLoad.header().setVisible(True)
        self.treeViewLoad.header().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.treeViewLoad, 0, 1, 1, 1)

        self.splitter.addWidget(self.widget_6)
        self.widget_8 = QWidget(self.splitter)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.widget_8.setMinimumSize(QSize(1100, 250))
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_5 = QWidget(self.widget_8)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(200, 0))
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.outDirButton = QPushButton(self.widget_5)
        self.outDirButton.setObjectName(u"outDirButton")
        sizePolicy2.setHeightForWidth(self.outDirButton.sizePolicy().hasHeightForWidth())
        self.outDirButton.setSizePolicy(sizePolicy2)
        self.outDirButton.setMinimumSize(QSize(150, 30))
        self.outDirButton.setFont(font2)
        self.outDirButton.setLayoutDirection(Qt.LeftToRight)
        self.outDirButton.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.outDirButton, 0, 0, 1, 1)

        self.sText = QLabel(self.widget_5)
        self.sText.setObjectName(u"sText")
        self.sText.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sText.sizePolicy().hasHeightForWidth())
        self.sText.setSizePolicy(sizePolicy3)
        self.sText.setMinimumSize(QSize(175, 0))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.sText.setFont(font4)
        self.sText.setAlignment(Qt.AlignCenter)
        self.sText.setWordWrap(True)

        self.gridLayout_6.addWidget(self.sText, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 211, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_5, 0, 0, 1, 1)

        self.treeViewOutput = QTreeWidget(self.widget_8)
        self.treeViewOutput.setObjectName(u"treeViewOutput")
        sizePolicy1.setHeightForWidth(self.treeViewOutput.sizePolicy().hasHeightForWidth())
        self.treeViewOutput.setSizePolicy(sizePolicy1)
        self.treeViewOutput.setMinimumSize(QSize(1000, 0))
        self.treeViewOutput.setFont(font3)
        self.treeViewOutput.setContextMenuPolicy(Qt.PreventContextMenu)
        self.treeViewOutput.setAcceptDrops(True)
        self.treeViewOutput.setAutoFillBackground(True)
        self.treeViewOutput.setFrameShape(QFrame.Box)
        self.treeViewOutput.setFrameShadow(QFrame.Sunken)
        self.treeViewOutput.setLineWidth(1)
        self.treeViewOutput.setMidLineWidth(1)
        self.treeViewOutput.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeViewOutput.setAlternatingRowColors(True)
        self.treeViewOutput.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeViewOutput.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeViewOutput.setColumnCount(0)
        self.treeViewOutput.header().setVisible(True)
        self.treeViewOutput.header().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.treeViewOutput, 0, 1, 1, 1)

        self.splitter.addWidget(self.widget_8)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 2)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.widget_7.setMinimumSize(QSize(200, 250))
        self.widget_7.setMaximumSize(QSize(16777215, 300))
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.widget_7)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(190, 200))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.groupBox.setFont(font5)
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.deidentifyInputDir = QCheckBox(self.groupBox)
        self.deidentifyInputDir.setObjectName(u"deidentifyInputDir")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.deidentifyInputDir.sizePolicy().hasHeightForWidth())
        self.deidentifyInputDir.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        self.deidentifyInputDir.setFont(font6)

        self.gridLayout_9.addWidget(self.deidentifyInputDir, 0, 0, 1, 1)

        self.offsetDate = QCheckBox(self.groupBox)
        self.offsetDate.setObjectName(u"offsetDate")
        sizePolicy4.setHeightForWidth(self.offsetDate.sizePolicy().hasHeightForWidth())
        self.offsetDate.setSizePolicy(sizePolicy4)
        self.offsetDate.setFont(font6)
        self.offsetDate.setChecked(False)

        self.gridLayout_9.addWidget(self.offsetDate, 1, 0, 1, 1)

        self.dryRun = QCheckBox(self.groupBox)
        self.dryRun.setObjectName(u"dryRun")
        sizePolicy4.setHeightForWidth(self.dryRun.sizePolicy().hasHeightForWidth())
        self.dryRun.setSizePolicy(sizePolicy4)
        self.dryRun.setFont(font6)

        self.gridLayout_9.addWidget(self.dryRun, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_7, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(900, 200))
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(900, 0))
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy5)
        self.cancelButton.setMinimumSize(QSize(150, 0))
        self.cancelButton.setMaximumSize(QSize(150, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.cancelButton.setPalette(palette)
        self.cancelButton.setFont(font5)
        self.cancelButton.setStyleSheet(u"background-color: rgb(255,0,0);\n"
"color: black")
        self.cancelButton.setFlat(False)

        self.gridLayout_8.addWidget(self.cancelButton, 0, 1, 1, 1)

        self.convertButton = QPushButton(self.widget)
        self.convertButton.setObjectName(u"convertButton")
        sizePolicy5.setHeightForWidth(self.convertButton.sizePolicy().hasHeightForWidth())
        self.convertButton.setSizePolicy(sizePolicy5)
        self.convertButton.setMinimumSize(QSize(150, 0))
        self.convertButton.setMaximumSize(QSize(150, 16777215))
        self.convertButton.setFont(font2)
        self.convertButton.setStyleSheet(u"background-color: rgb(79, 232, 109);\n"
"color: black")

        self.gridLayout_8.addWidget(self.convertButton, 0, 2, 1, 1)

        self.spredButton = QPushButton(self.widget)
        self.spredButton.setObjectName(u"spredButton")
        sizePolicy5.setHeightForWidth(self.spredButton.sizePolicy().hasHeightForWidth())
        self.spredButton.setSizePolicy(sizePolicy5)
        self.spredButton.setMinimumSize(QSize(150, 0))
        self.spredButton.setMaximumSize(QSize(150, 16777215))
        self.spredButton.setFont(font5)
        self.spredButton.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: black")

        self.gridLayout_8.addWidget(self.spredButton, 0, 3, 1, 1)

        self.imagingButton = QPushButton(self.widget)
        self.imagingButton.setObjectName(u"imagingButton")
        sizePolicy5.setHeightForWidth(self.imagingButton.sizePolicy().hasHeightForWidth())
        self.imagingButton.setSizePolicy(sizePolicy5)
        self.imagingButton.setMinimumSize(QSize(150, 0))
        self.imagingButton.setMaximumSize(QSize(150, 16777215))
        self.imagingButton.setFont(font5)
        self.imagingButton.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: black")

        self.gridLayout_8.addWidget(self.imagingButton, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)


        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(900, 0))
        self.label.setFont(font5)

        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)

        self.conversionStatus = QPlainTextEdit(self.widget_3)
        self.conversionStatus.setObjectName(u"conversionStatus")
        sizePolicy.setHeightForWidth(self.conversionStatus.sizePolicy().hasHeightForWidth())
        self.conversionStatus.setSizePolicy(sizePolicy)
        self.conversionStatus.setMinimumSize(QSize(0, 150))
        self.conversionStatus.setMaximumSize(QSize(16777215, 300))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(9)
        self.conversionStatus.setFont(font7)
        self.conversionStatus.setFrameShape(QFrame.Box)
        self.conversionStatus.setMidLineWidth(1)
        self.conversionStatus.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.conversionStatus, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font8 = QFont()
        font8.setFamily(u"Arial")
        self.statusbar.setFont(font8)
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1242, 23))
        self.menuBar.setFont(font1)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font1)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_data)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.actionLoad_data.triggered.connect(self.loadDirButton.showMenu)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"edf2bids converter", None))
        self.actionLoad_data.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.loadDirButton.setText(QCoreApplication.translate("MainWindow", u"Input Directory", None))
        self.outDirButton.setText(QCoreApplication.translate("MainWindow", u"Output Directory", None))
        self.sText.setText(QCoreApplication.translate("MainWindow", u"Checked items are already in output directory.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Settings Panel", None))
        self.deidentifyInputDir.setText(QCoreApplication.translate("MainWindow", u"De-identify input directory", None))
        self.offsetDate.setText(QCoreApplication.translate("MainWindow", u"Offset dates", None))
        self.dryRun.setText(QCoreApplication.translate("MainWindow", u"Dry run (no EDF)", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.spredButton.setText(QCoreApplication.translate("MainWindow", u"SPReD", None))
        self.imagingButton.setText(QCoreApplication.translate("MainWindow", u"Imaging", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Conversion Status", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

