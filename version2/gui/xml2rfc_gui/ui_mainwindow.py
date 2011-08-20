# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Fri Aug 19 18:02:07 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1024, 768)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.mainFrame = QtGui.QWidget(mainWindow)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setMargin(8)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.settingsFrame = QtGui.QFrame(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsFrame.sizePolicy().hasHeightForWidth())
        self.settingsFrame.setSizePolicy(sizePolicy)
        self.settingsFrame.setObjectName(_fromUtf8("settingsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.settingsFrame)
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.settingsFrame)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setMargin(8)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.sourceLabel = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceLabel.sizePolicy().hasHeightForWidth())
        self.sourceLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        self.sourceLabel.setFont(font)
        self.sourceLabel.setObjectName(_fromUtf8("sourceLabel"))
        self.horizontalLayout_3.addWidget(self.sourceLabel)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.settingsFrame)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setMargin(8)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formatPaged = QtGui.QCheckBox(self.groupBox)
        self.formatPaged.setChecked(True)
        self.formatPaged.setObjectName(_fromUtf8("formatPaged"))
        self.horizontalLayout_2.addWidget(self.formatPaged)
        self.formatRaw = QtGui.QCheckBox(self.groupBox)
        self.formatRaw.setObjectName(_fromUtf8("formatRaw"))
        self.horizontalLayout_2.addWidget(self.formatRaw)
        self.formatHtml = QtGui.QCheckBox(self.groupBox)
        self.formatHtml.setObjectName(_fromUtf8("formatHtml"))
        self.horizontalLayout_2.addWidget(self.formatHtml)
        self.formatNroff = QtGui.QCheckBox(self.groupBox)
        self.formatNroff.setObjectName(_fromUtf8("formatNroff"))
        self.horizontalLayout_2.addWidget(self.formatNroff)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.convertButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convertButton.sizePolicy().hasHeightForWidth())
        self.convertButton.setSizePolicy(sizePolicy)
        self.convertButton.setMinimumSize(QtCore.QSize(100, 0))
        self.convertButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.horizontalLayout_2.addWidget(self.convertButton)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.settingsFrame)
        self.documentFrame = QtGui.QFrame(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.documentFrame.sizePolicy().hasHeightForWidth())
        self.documentFrame.setSizePolicy(sizePolicy)
        self.documentFrame.setStyleSheet(_fromUtf8("/* Disable tabwidget in-set bg\'s */\n"
"QTabWidget::pane {background: none;}"))
        self.documentFrame.setObjectName(_fromUtf8("documentFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.documentFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.documentFrame)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.xmlTab = QtGui.QWidget()
        self.xmlTab.setObjectName(_fromUtf8("xmlTab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.xmlTab)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setMargin(1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.textXml = LinedEditor(self.xmlTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textXml.sizePolicy().hasHeightForWidth())
        self.textXml.setSizePolicy(sizePolicy)
        self.textXml.setFrameShape(QtGui.QFrame.NoFrame)
        self.textXml.setReadOnly(False)
        self.textXml.setObjectName(_fromUtf8("textXml"))
        self.verticalLayout_8.addWidget(self.textXml)
        self.tabWidget.addTab(self.xmlTab, _fromUtf8(""))
        self.consoleGroupBox = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleGroupBox.sizePolicy().hasHeightForWidth())
        self.consoleGroupBox.setSizePolicy(sizePolicy)
        self.consoleGroupBox.setFlat(True)
        self.consoleGroupBox.setObjectName(_fromUtf8("consoleGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.consoleGroupBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textConsole = QtGui.QTextBrowser(self.consoleGroupBox)
        self.textConsole.setOpenLinks(False)
        self.textConsole.setObjectName(_fromUtf8("textConsole"))
        self.verticalLayout_5.addWidget(self.textConsole)
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.documentFrame)
        mainWindow.setCentralWidget(self.mainFrame)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuFormats = QtGui.QMenu(self.menuOptions)
        self.menuFormats.setObjectName(_fromUtf8("menuFormats"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(mainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(mainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAboutQt = QtGui.QAction(mainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionPreferences = QtGui.QAction(mainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionOpen = QtGui.QAction(mainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClear = QtGui.QAction(mainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionD = QtGui.QAction(mainWindow)
        self.actionD.setObjectName(_fromUtf8("actionD"))
        self.actionFormatPaged = QtGui.QAction(mainWindow)
        self.actionFormatPaged.setCheckable(True)
        self.actionFormatPaged.setChecked(True)
        self.actionFormatPaged.setObjectName(_fromUtf8("actionFormatPaged"))
        self.actionFormatRaw = QtGui.QAction(mainWindow)
        self.actionFormatRaw.setCheckable(True)
        self.actionFormatRaw.setObjectName(_fromUtf8("actionFormatRaw"))
        self.actionFormatHtml = QtGui.QAction(mainWindow)
        self.actionFormatHtml.setCheckable(True)
        self.actionFormatHtml.setObjectName(_fromUtf8("actionFormatHtml"))
        self.actionFormatNroff = QtGui.QAction(mainWindow)
        self.actionFormatNroff.setCheckable(True)
        self.actionFormatNroff.setObjectName(_fromUtf8("actionFormatNroff"))
        self.actionOptionVerbose = QtGui.QAction(mainWindow)
        self.actionOptionVerbose.setCheckable(True)
        self.actionOptionVerbose.setObjectName(_fromUtf8("actionOptionVerbose"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuFormats.addAction(self.actionFormatPaged)
        self.menuFormats.addAction(self.actionFormatRaw)
        self.menuFormats.addAction(self.actionFormatHtml)
        self.menuFormats.addAction(self.actionFormatNroff)
        self.menuOptions.addAction(self.menuFormats.menuAction())
        self.menuOptions.addAction(self.actionOptionVerbose)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionFormatPaged, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.formatPaged.setChecked)
        QtCore.QObject.connect(self.actionFormatRaw, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.formatRaw.setChecked)
        QtCore.QObject.connect(self.actionFormatHtml, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.formatHtml.setChecked)
        QtCore.QObject.connect(self.actionFormatNroff, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.formatNroff.setChecked)
        QtCore.QObject.connect(self.formatPaged, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.actionFormatPaged.setChecked)
        QtCore.QObject.connect(self.formatRaw, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.actionFormatRaw.setChecked)
        QtCore.QObject.connect(self.formatHtml, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.actionFormatHtml.setChecked)
        QtCore.QObject.connect(self.formatNroff, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.actionFormatNroff.setChecked)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "xml2rfc GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("mainWindow", "Input file", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceLabel.setText(QtGui.QApplication.translate("mainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.formatPaged.setText(QtGui.QApplication.translate("mainWindow", "Paginated Text", None, QtGui.QApplication.UnicodeUTF8))
        self.formatRaw.setText(QtGui.QApplication.translate("mainWindow", "Raw Text", None, QtGui.QApplication.UnicodeUTF8))
        self.formatHtml.setText(QtGui.QApplication.translate("mainWindow", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.formatNroff.setText(QtGui.QApplication.translate("mainWindow", "Nroff", None, QtGui.QApplication.UnicodeUTF8))
        self.convertButton.setText(QtGui.QApplication.translate("mainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xmlTab), QtGui.QApplication.translate("mainWindow", "XML", None, QtGui.QApplication.UnicodeUTF8))
        self.consoleGroupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("mainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFormats.setTitle(QtGui.QApplication.translate("mainWindow", "Output formats", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("mainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainWindow", "About Xml2rfc", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("mainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("mainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("mainWindow", "&Open Source", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("mainWindow", "Clear Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.actionD.setText(QtGui.QApplication.translate("mainWindow", "> df", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatPaged.setText(QtGui.QApplication.translate("mainWindow", "Paginated Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatRaw.setText(QtGui.QApplication.translate("mainWindow", "Raw Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatHtml.setText(QtGui.QApplication.translate("mainWindow", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatNroff.setText(QtGui.QApplication.translate("mainWindow", "Nroff", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptionVerbose.setText(QtGui.QApplication.translate("mainWindow", "Verbose console output", None, QtGui.QApplication.UnicodeUTF8))

from editor import LinedEditor
