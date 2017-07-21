"""ui setup class"""
import os
from PyQt4 import QtGui, QtCore
from master import config


class MasterWindowUi():
    """ApduDiyDialogUi"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        self.setWindowTitle('698后台_{ver}'.format(ver=config.MASTER_WINDOW_TITLE_ADD))
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, config.MASTER_ICO_PATH)))
        self.menubar = self.menuBar()

        self.link_action = QtGui.QAction('&通信设置', self)
        self.link_action.setShortcut('F2')
        self.commu_menu = self.menubar.addMenu('&通信')
        self.commu_menu.addAction(self.link_action)

        self.get_set_service_action = QtGui.QAction('&读取/设置', self)
        self.get_set_service_action.setShortcut('F5')
        self.action_service_action = QtGui.QAction('&操作', self)
        self.action_service_action.setShortcut('F6')
        self.proxy_service_action = QtGui.QAction('&代理', self)
        self.proxy_service_action.setShortcut('F7')
        # self.commu_menu = self.menubar.addMenu('&服务')
        # self.commu_menu.addAction(self.get_set_service_action)
        # self.commu_menu.addAction(self.action_service_action)
        # self.commu_menu.addAction(self.proxy_service_action)

        self.general_cmd_action = QtGui.QAction('&常用命令', self)
        self.general_cmd_action.setShortcut('F9')
        self.apdu_diy_action = QtGui.QAction('&自定义APDU', self)
        self.apdu_diy_action.setShortcut('F10')
        self.msg_diy_action = QtGui.QAction('&自定义报文', self)
        self.msg_diy_action.setShortcut('F11')
        self.remote_update_action = QtGui.QAction('&远程升级', self)
        self.remote_update_action.setShortcut('F12')
        self.msg_menu = self.menubar.addMenu('&报文')
        self.msg_menu.addAction(self.general_cmd_action)
        self.msg_menu.addAction(self.apdu_diy_action)
        self.msg_menu.addAction(self.msg_diy_action)
        self.msg_menu.addAction(self.remote_update_action)

        self.about_action = QtGui.QAction('&关于', self)
        self.about_action.setShortcut('F1')
        self.help_menu = self.menubar.addMenu('&帮助')
        self.help_menu.addAction(self.about_action)

        self.tmn_list_w = QtGui.QWidget()
        self.tmn_table_vbox = QtGui.QVBoxLayout(self.tmn_list_w)
        self.tmn_table_vbox.setMargin(1)
        self.tmn_table_vbox.setSpacing(0)
        self.tmn_table = QtGui.QTableWidget(self.tmn_list_w)
        self.tmn_table.verticalHeader().setVisible(False)
        for count in range(5):
            self.tmn_table.insertColumn(count)
        self.tmn_table.setHorizontalHeaderLabels(['', '终端地址', '逻辑地址', '通道', ''])
        self.tmn_table.setColumnWidth(0, 15)
        self.tmn_table.setColumnWidth(1, 96)
        self.tmn_table.setColumnWidth(2, 40)
        self.tmn_table.setColumnWidth(3, 65)
        self.tmn_table.setColumnWidth(4, 25)
        self.tmn_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tmn_table.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tmn_table_scan_b = QtGui.QPushButton()
        self.tmn_table_scan_b.setText('扫描')
        self.tmn_table_add_b = QtGui.QPushButton()
        self.tmn_table_add_b.setText('新增')
        self.tmn_table_clr_b = QtGui.QPushButton()
        self.tmn_table_clr_b.setText('清空')
        self.tmn_table_clr_b.setMaximumWidth(70)
        self.tmn_table_btns_hbox = QtGui.QHBoxLayout()
        self.tmn_table_btns_hbox.addWidget(self.tmn_table_scan_b)
        self.tmn_table_btns_hbox.addWidget(self.tmn_table_add_b)
        self.tmn_table_btns_hbox.addWidget(self.tmn_table_clr_b)
        self.tmn_table_vbox.addWidget(self.tmn_table)
        self.tmn_table_vbox.addLayout(self.tmn_table_btns_hbox)

        self.quick_info_w = QtGui.QWidget()
        self.quick_vbox = QtGui.QVBoxLayout(self.quick_info_w)
        self.quick_hbox = QtGui.QHBoxLayout()
        self.oad_l = QtGui.QLabel()
        self.oad_l.setText('OAD')
        self.oad_box = QtGui.QLineEdit()
        # self.oad_box.setMaximumWidth(70)
        self.read_oad_b = QtGui.QPushButton()
        self.read_oad_b.setMaximumWidth(50)
        self.read_oad_b.setText('读取')
        self.oad_explain_l = QtGui.QLabel()
        self.quick_hbox.addWidget(self.oad_l)
        self.quick_hbox.addWidget(self.oad_box)
        self.quick_hbox.addWidget(self.read_oad_b)
        self.quick_vbox.addLayout(self.quick_hbox)
        self.quick_vbox.addWidget(self.oad_explain_l)
        self.quick_vbox.addStretch(1)

        self.msg_table_w = QtGui.QWidget()
        self.msg_table_vbox = QtGui.QVBoxLayout(self.msg_table_w)
        self.msg_table_vbox.setMargin(1)
        self.msg_table_vbox.setSpacing(0)
        self.msg_table = QtGui.QTableWidget()
        self.msg_table.verticalHeader().setVisible(False)
        for count in range(5):
            self.msg_table.insertColumn(count)
        self.msg_table.setHorizontalHeaderLabels(['时间', '终端', '通道/方向', '概览', '报文'])
        self.msg_table.setColumnWidth(0, 130)
        self.msg_table.setColumnWidth(1, 110)
        self.msg_table.setColumnWidth(2, 60)
        self.msg_table.setColumnWidth(3, 200)
        self.msg_table.setColumnWidth(4, 300)
        self.msg_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.msg_table.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.msg_table.setEditTriggers(QtGui.QTableWidget.NoEditTriggers) # 表格不可编辑
        self.msg_btn_hbox = QtGui.QHBoxLayout()
        self.clr_b = QtGui.QPushButton()
        self.clr_b.setText('清空报文')
        self.clr_b.setMaximumWidth(60)
        self.open_log_b = QtGui.QPushButton()
        self.open_log_b.setText('查看日志')
        self.msg_btn_hbox.addWidget(self.clr_b)
        self.msg_btn_hbox.addStretch(1)
        self.msg_btn_hbox.addWidget(self.open_log_b)
        self.msg_table_vbox.addWidget(self.msg_table)
        self.msg_table_vbox.addLayout(self.msg_btn_hbox)

        self.left_vsplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.left_vsplitter.addWidget(self.tmn_list_w)
        self.left_vsplitter.addWidget(self.quick_info_w)
        self.left_vsplitter.setStretchFactor(0, 1)
        self.left_vsplitter.setStretchFactor(1, 1)

        self.main_hsplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.main_hsplitter.addWidget(self.left_vsplitter)
        self.main_hsplitter.addWidget(self.msg_table_w)
        self.main_hsplitter.setStretchFactor(0, 1)
        self.main_hsplitter.setStretchFactor(1, 3)

        self.reply_rpt_cb = QtGui.QCheckBox()
        self.reply_rpt_cb.setText('回复上报')
        self.reply_link_cb = QtGui.QCheckBox()
        self.reply_link_cb.setText('维护登录/心跳')
        self.always_top_cb = QtGui.QCheckBox()
        self.always_top_cb.setText('置顶')
        self.foot_hbox = QtGui.QHBoxLayout()
        self.foot_hbox.addStretch(1)
        self.foot_hbox.addWidget(self.reply_rpt_cb)
        self.foot_hbox.addWidget(self.reply_link_cb)
        self.foot_hbox.addWidget(self.always_top_cb)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.setMargin(1)
        self.main_vbox.setSpacing(1)
        self.main_vbox.addWidget(self.main_hsplitter)
        self.main_vbox.addLayout(self.foot_hbox)
        self.main_widget = QtGui.QWidget()
        self.main_widget.setLayout(self.main_vbox)
        self.setCentralWidget(self.main_widget)
        self.resize(1000, 666)


class TransWindowUi():
    """ApduDiyDialogUi"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        self.setWindowTitle('698日志解析工具_{ver}'.format(ver=config.TRANS_WINDOW_TITLE_ADD))
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, 'imgs/698_o.png')))
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('&文件')
        self.open_action = QtGui.QAction('&打开...', self)
        self.open_action.setShortcut('Ctrl+o')
        self.close_action = QtGui.QAction('&清空', self)
        self.close_action.setShortcut('Ctrl+l')
        self.find_action = QtGui.QAction('查找', self)
        self.find_action.setShortcut('Ctrl+f')
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.close_action)
        self.file_menu.addAction(self.find_action)
        self.help_menu = self.menubar.addMenu('&帮助')
        self.about_action = QtGui.QAction('&关于', self)
        self.about_action.setShortcut('F1')
        self.help_menu.addAction(self.about_action)

        self.dummy_l = QtGui.QLabel()
        self.dummy_l.setText('   ')

        self.input_w = QtGui.QWidget()
        self.input_box = QtGui.QTextEdit()
        self.find_box = QtGui.QLineEdit()
        self.find_box.setPlaceholderText('搜索...')
        self.find_last_b = QtGui.QPushButton()
        self.find_last_b.setMaximumWidth(30)
        self.find_last_b.setText('<')
        self.find_next_b = QtGui.QPushButton()
        self.find_next_b.setMaximumWidth(30)
        self.find_next_b.setText('>')
        self.find_l = QtGui.QLabel()
        self.input_zoom_in_b = QtGui.QPushButton()
        self.input_zoom_in_b.setMaximumWidth(30)
        self.input_zoom_in_b.setText('+')
        self.input_zoom_out_b = QtGui.QPushButton()
        self.input_zoom_out_b.setMaximumWidth(30)
        self.input_zoom_out_b.setText('-')
        self.input_foot_hbox = QtGui.QHBoxLayout()
        self.input_foot_hbox.addWidget(self.find_box)
        self.input_foot_hbox.addWidget(self.find_last_b)
        self.input_foot_hbox.addWidget(self.find_next_b)
        self.input_foot_hbox.addWidget(self.find_l)
        self.input_foot_hbox.addStretch(1)
        self.input_foot_hbox.addWidget(self.input_zoom_in_b)
        self.input_foot_hbox.addWidget(self.input_zoom_out_b)
        self.input_vbox = QtGui.QVBoxLayout(self.input_w)
        self.input_vbox.setMargin(1)
        self.input_vbox.setSpacing(1)
        self.input_vbox.addWidget(self.input_box)
        self.input_vbox.addLayout(self.input_foot_hbox)

        self.output_w = QtGui.QWidget()
        self.output_box = QtGui.QTextEdit()
        self.output_zoom_in_b = QtGui.QPushButton()
        self.output_zoom_in_b.setMaximumWidth(30)
        self.output_zoom_in_b.setText('+')
        self.output_zoom_out_b = QtGui.QPushButton()
        self.output_zoom_out_b.setMaximumWidth(30)
        self.output_zoom_out_b.setText('-')
        self.output_foot_hbox = QtGui.QHBoxLayout()
        self.output_foot_hbox.addStretch(1)
        self.output_foot_hbox.addWidget(self.output_zoom_in_b)
        self.output_foot_hbox.addWidget(self.output_zoom_out_b)
        self.output_vbox = QtGui.QVBoxLayout(self.output_w)
        self.output_vbox.setMargin(1)
        self.output_vbox.setSpacing(1)
        self.output_vbox.addWidget(self.output_box)
        self.output_vbox.addLayout(self.output_foot_hbox)

        self.main_hsplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.main_hsplitter.addWidget(self.input_w)
        self.main_hsplitter.addWidget(self.output_w)
        self.main_hsplitter.setStretchFactor(0, 1)
        self.main_hsplitter.setStretchFactor(1, 1)

        self.proc_bar = QtGui.QProgressBar()
        # self.proc_bar.setEnabled(True)
        self.proc_bar.setMinimumSize(QtCore.QSize(200, 0))
        self.proc_bar.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed))
        self.proc_bar.setTextVisible(False)
        
        self.proc_l = QtGui.QLabel()
        self.proc_l.setText('就绪')
        self.show_level_cb = QtGui.QCheckBox()
        self.show_level_cb.setText('报文结构')
        self.show_dtype_cb = QtGui.QCheckBox()
        self.show_dtype_cb.setText('数据类型')
        self.always_top_cb = QtGui.QCheckBox()
        self.always_top_cb.setText('置顶')

        self.foot_hbox = QtGui.QHBoxLayout()
        self.foot_hbox.addWidget(self.proc_bar)
        self.foot_hbox.addWidget(self.proc_l)
        self.foot_hbox.addStretch(1)
        self.foot_hbox.addWidget(self.show_level_cb)
        self.foot_hbox.addWidget(self.show_dtype_cb)
        self.foot_hbox.addWidget(self.always_top_cb)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.setMargin(1)
        self.main_vbox.setSpacing(1)
        self.main_vbox.addWidget(self.main_hsplitter)
        self.main_vbox.addLayout(self.foot_hbox)
        self.main_widget = QtGui.QWidget()
        self.main_widget.setLayout(self.main_vbox)
        self.setCentralWidget(self.main_widget)
        self.resize(1000, 666)


class TransPopDialogUi():
    """ApduDiyDialogUi"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('详细解析')
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, config.MASTER_ICO_PATH)))
        self.msg_box = QtGui.QPlainTextEdit()
        self.explain_box = QtGui.QTextEdit()
        self.splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitter.addWidget(self.msg_box)
        self.splitter.addWidget(self.explain_box)
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 6)

        self.always_top_cb = QtGui.QCheckBox()
        self.always_top_cb.setText('置顶')
        self.show_dtype_cb = QtGui.QCheckBox()
        self.show_dtype_cb.setText('数据类型')
        self.show_level_cb = QtGui.QCheckBox()
        self.show_level_cb.setText('显示结构')
        self.cb_hbox = QtGui.QHBoxLayout()
        self.cb_hbox.addStretch(1)
        self.cb_hbox.addWidget(self.show_level_cb)
        self.cb_hbox.addWidget(self.show_dtype_cb)
        self.cb_hbox.addWidget(self.always_top_cb)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.setMargin(1)
        self.main_vbox.setSpacing(1)
        self.main_vbox.addWidget(self.splitter)
        self.main_vbox.addLayout(self.cb_hbox)
        self.setLayout(self.main_vbox)
        self.resize(500, 700)


class CommuDialogUi():
    """ApduDiyDialogUi"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        self.setWindowTitle('通信控制面板')
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, config.MASTER_ICO_PATH)))
        self.master_addr_l = QtGui.QLabel()
        self.master_addr_l.setText('主站地址：')
        self.master_addr_box = QtGui.QLineEdit()
        self.master_addr_change_b = QtGui.QPushButton()
        self.master_addr_change_b.setText('切换')
        self.master_addr_change_b.setMaximumWidth(50)
        self.master_addr_box.setText(config.COMMU.master_addr)
        self.serial_label = QtGui.QLabel()
        self.serial_label.setText('串口：')
        self.serial_combo = QtGui.QComboBox()
        self.serial_baud = QtGui.QComboBox()
        self.serial_baud.addItems(('1200', '2400', '4800', '9600', '19200', '115200'))
        self.serial_baud.setCurrentIndex(3)
        self.serial_link_b = QtGui.QPushButton()
        self.serial_link_b.setMaximumWidth(50)
        self.serial_link_b.setText('连接')
        self.serial_cut_b = QtGui.QPushButton()
        self.serial_cut_b.setMaximumWidth(50)
        self.serial_cut_b.setText('刷新')
        self.frontend_label = QtGui.QLabel()
        self.frontend_label.setText('前置机：')
        self.frontend_ip_l = QtGui.QLabel()
        self.frontend_ip_l.setText('IP:PORT')
        self.frontend_box = QtGui.QLineEdit()
        self.frontend_box.setPlaceholderText('例 127.0.0.1:1080')
        self.frontend_link_b = QtGui.QPushButton()
        self.frontend_link_b.setMaximumWidth(50)
        self.frontend_link_b.setText('连接')
        self.frontend_cut_b = QtGui.QPushButton()
        self.frontend_cut_b.setMaximumWidth(50)
        self.frontend_cut_b.setText('断开')
        self.server_label = QtGui.QLabel()
        self.server_label.setText('服务器：')
        self.server_port_l = QtGui.QLabel()
        self.server_port_l.setText('端口')
        self.server_box = QtGui.QLineEdit()
        self.server_box.setPlaceholderText('例 1080')
        self.server_link_b = QtGui.QPushButton()
        self.server_link_b.setMaximumWidth(50)
        self.server_link_b.setText('启动')
        self.server_cut_b = QtGui.QPushButton()
        self.server_cut_b.setMaximumWidth(50)
        self.server_cut_b.setText('停止')
        self.close_b = QtGui.QPushButton()
        self.close_b.setText('关闭')
        self.dummy_l = QtGui.QLabel()
        self.commu_panel_gbox = QtGui.QGridLayout()
        self.commu_panel_gbox.setMargin(15)
        self.commu_panel_gbox.setSpacing(3)
        self.commu_panel_gbox.addWidget(self.master_addr_l, 0, 0)
        self.commu_panel_gbox.addWidget(self.master_addr_box, 0, 1)
        self.commu_panel_gbox.addWidget(self.master_addr_change_b, 0, 2)
        self.commu_panel_gbox.addWidget(self.dummy_l, 1, 0)
        self.commu_panel_gbox.addWidget(self.serial_label, 2, 0)
        self.commu_panel_gbox.addWidget(self.serial_combo, 3, 0)
        self.commu_panel_gbox.addWidget(self.serial_baud, 3, 1)
        self.commu_panel_gbox.addWidget(self.serial_link_b, 3, 2)
        self.commu_panel_gbox.addWidget(self.serial_cut_b, 3, 3)
        self.commu_panel_gbox.addWidget(self.dummy_l, 4, 0)
        self.commu_panel_gbox.addWidget(self.frontend_label, 5, 0)
        self.commu_panel_gbox.addWidget(self.frontend_ip_l, 6, 0)
        self.commu_panel_gbox.addWidget(self.frontend_box, 6, 1)
        self.commu_panel_gbox.addWidget(self.frontend_link_b, 6, 2)
        self.commu_panel_gbox.addWidget(self.frontend_cut_b, 6, 3)
        self.commu_panel_gbox.addWidget(self.dummy_l, 7, 0)
        self.commu_panel_gbox.addWidget(self.server_label, 8, 0)
        self.commu_panel_gbox.addWidget(self.server_port_l, 9, 0)
        self.commu_panel_gbox.addWidget(self.server_box, 9, 1)
        self.commu_panel_gbox.addWidget(self.server_link_b, 9, 2)
        self.commu_panel_gbox.addWidget(self.server_cut_b, 9, 3)
        self.commu_panel_gbox.addWidget(self.dummy_l, 10, 0)
        self.commu_panel_gbox.addWidget(self.close_b, 11, 0, 1, 4)
        self.setLayout(self.commu_panel_gbox)


class ApduDiyDialogUi():
    """ApduDiyDialogUi"""
    def __init__(self):
        self.setup_ui()


    def setup_ui(self):
        """set layout"""
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('自定义APDU')
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, config.MASTER_ICO_PATH)))

        self.se_clr_b = QtGui.QPushButton()
        self.se_clr_b.setText('清空')
        self.send_b = QtGui.QPushButton()
        self.send_b.setText('发送')
        self.se_btn_hbox = QtGui.QHBoxLayout()
        self.se_btn_hbox.addWidget(self.se_clr_b)
        self.se_btn_hbox.addStretch(1)
        self.se_btn_hbox.addWidget(self.send_b)

        self.se_msg_box = QtGui.QPlainTextEdit()
        self.se_explain_box = QtGui.QTextEdit()
        self.se_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.se_splitter.addWidget(self.se_msg_box)
        self.se_splitter.addWidget(self.se_explain_box)
        self.se_splitter.setStretchFactor(0, 1)
        self.se_splitter.setStretchFactor(1, 6)

        self.re_clr_b = QtGui.QPushButton()
        self.re_clr_b.setText('清空')
        self.re_btn_hbox = QtGui.QHBoxLayout()
        self.re_btn_hbox.addWidget(self.re_clr_b)
        self.re_btn_hbox.addStretch(1)

        self.re_msg_box = QtGui.QPlainTextEdit()
        self.re_explain_box = QtGui.QTextEdit()
        self.re_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.re_splitter.addWidget(self.re_msg_box)
        self.re_splitter.addWidget(self.re_explain_box)
        self.re_splitter.setStretchFactor(0, 1)
        self.re_splitter.setStretchFactor(1, 6)

        self.chk_valid_cb = QtGui.QCheckBox()
        self.chk_valid_cb.setText('检查合法性')
        self.always_top_cb = QtGui.QCheckBox()
        self.always_top_cb.setText('置顶')
        self.show_level_cb = QtGui.QCheckBox()
        self.show_level_cb.setText('显示结构')
        self.show_dtype_cb = QtGui.QCheckBox()
        self.show_dtype_cb.setText('数据类型')
        self.cb_hbox = QtGui.QHBoxLayout()
        self.cb_hbox.addStretch(1)
        self.cb_hbox.addWidget(self.chk_valid_cb)
        self.cb_hbox.addWidget(self.show_level_cb)
        self.cb_hbox.addWidget(self.show_dtype_cb)
        self.cb_hbox.addWidget(self.always_top_cb)

        self.se_w = QtGui.QWidget()
        self.se_vbox = QtGui.QVBoxLayout(self.se_w)
        self.se_vbox.setMargin(1)
        self.se_vbox.setSpacing(1)
        self.se_vbox.addLayout(self.se_btn_hbox)
        self.se_vbox.addWidget(self.se_splitter)

        self.re_w = QtGui.QWidget()
        self.re_vbox = QtGui.QVBoxLayout(self.re_w)
        self.re_vbox.setMargin(1)
        self.re_vbox.setSpacing(1)
        self.re_vbox.addLayout(self.re_btn_hbox)
        self.re_vbox.addWidget(self.re_splitter)

        self.main_splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.main_splitter.addWidget(self.se_w)
        self.main_splitter.addWidget(self.re_w)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.setMargin(1)
        self.main_vbox.setSpacing(1)
        self.main_vbox.addWidget(self.main_splitter)
        self.main_vbox.addLayout(self.cb_hbox)
        self.setLayout(self.main_vbox)
        self.resize(1000, 700)


class MsgDiyDialogUi():
    """MsgDiyDialogUi"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('自定义报文')
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, config.MASTER_ICO_PATH)))

        self.se_clr_b = QtGui.QPushButton()
        self.se_clr_b.setText('清空')
        self.chan_l = QtGui.QLabel()
        self.chan_l.setText('通道 ')
        self.chan_cb = QtGui.QComboBox()
        self.chan_cb.addItems(('串口', '前置机', '服务器'))
        self.send_b = QtGui.QPushButton()
        self.send_b.setText('发送')
        self.se_btn_hbox = QtGui.QHBoxLayout()
        self.se_btn_hbox.addWidget(self.se_clr_b)
        self.se_btn_hbox.addStretch(1)
        self.se_btn_hbox.addWidget(self.chan_l)
        self.se_btn_hbox.addWidget(self.chan_cb)
        self.se_btn_hbox.addStretch(1)
        self.se_btn_hbox.addWidget(self.send_b)

        self.se_msg_box = QtGui.QPlainTextEdit()
        self.se_explain_box = QtGui.QTextEdit()
        self.se_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.se_splitter.addWidget(self.se_msg_box)
        self.se_splitter.addWidget(self.se_explain_box)
        self.se_splitter.setStretchFactor(0, 1)
        self.se_splitter.setStretchFactor(1, 6)

        self.re_clr_b = QtGui.QPushButton()
        self.re_clr_b.setText('清空')
        self.re_btn_hbox = QtGui.QHBoxLayout()
        self.re_btn_hbox.addWidget(self.re_clr_b)
        self.re_btn_hbox.addStretch(1)

        self.re_msg_box = QtGui.QPlainTextEdit()
        self.re_explain_box = QtGui.QTextEdit()
        self.re_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.re_splitter.addWidget(self.re_msg_box)
        self.re_splitter.addWidget(self.re_explain_box)
        self.re_splitter.setStretchFactor(0, 1)
        self.re_splitter.setStretchFactor(1, 6)

        self.chk_valid_cb = QtGui.QCheckBox()
        self.chk_valid_cb.setText('检查合法性')
        self.always_top_cb = QtGui.QCheckBox()
        self.always_top_cb.setText('置顶')
        self.show_level_cb = QtGui.QCheckBox()
        self.show_level_cb.setText('显示结构')
        self.show_dtype_cb = QtGui.QCheckBox()
        self.show_dtype_cb.setText('数据结构')
        self.cb_hbox = QtGui.QHBoxLayout()
        self.cb_hbox.addStretch(1)
        self.cb_hbox.addWidget(self.chk_valid_cb)
        self.cb_hbox.addWidget(self.show_level_cb)
        self.cb_hbox.addWidget(self.show_dtype_cb)
        self.cb_hbox.addWidget(self.always_top_cb)

        self.se_w = QtGui.QWidget()
        self.se_vbox = QtGui.QVBoxLayout(self.se_w)
        self.se_vbox.setMargin(1)
        self.se_vbox.setSpacing(1)
        self.se_vbox.addLayout(self.se_btn_hbox)
        self.se_vbox.addWidget(self.se_splitter)

        self.re_w = QtGui.QWidget()
        self.re_vbox = QtGui.QVBoxLayout(self.re_w)
        self.re_vbox.setMargin(1)
        self.re_vbox.setSpacing(1)
        self.re_vbox.addLayout(self.re_btn_hbox)
        self.re_vbox.addWidget(self.re_splitter)

        self.main_splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.main_splitter.addWidget(self.se_w)
        self.main_splitter.addWidget(self.re_w)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.setMargin(1)
        self.main_vbox.setSpacing(1)
        self.main_vbox.addWidget(self.main_splitter)
        self.main_vbox.addLayout(self.cb_hbox)
        self.setLayout(self.main_vbox)
        self.resize(1000, 700)


class RemoteUpdateDialogUI():
    """RemoteUpdateDialogUI"""
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """set layout"""
        self.setWindowTitle('远程文件升级')
        self.setWindowIcon(QtGui.QIcon(os.path.join(config.SORTWARE_PATH, config.MASTER_ICO_PATH)))

        self.file_label = QtGui.QLabel()
        self.file_label.setText('文件:')
        self.file_open_b = QtGui.QPushButton()
        self.file_open_b.setMaximumWidth(50)
        self.file_open_b.setText('打开...')
        self.file_path_box = QtGui.QLineEdit()
        self.file_path_box.setPlaceholderText('请选择或拖入文件')

        self.block_size_label = QtGui.QLabel()
        self.block_size_label.setText('传输块大小:')
        self.block_size_combo = QtGui.QComboBox()
        self.block_size_combo.addItem('128字节')
        self.block_size_combo.addItem('256字节')
        self.block_size_combo.addItem('512字节')
        self.block_size_combo.addItem('1024字节')

        self.file_size_label = QtGui.QLabel()
        self.file_size_label.setText('文件大小')
        self.file_size_num_label = QtGui.QLabel()
        self.file_size_num_label.setText('0字节')
        self.block_label = QtGui.QLabel()
        self.block_label.setText('共计')
        self.block_num_label = QtGui.QLabel()
        self.block_num_label.setText('0包')

        self.start_update_b = QtGui.QPushButton()
        self.start_update_b.setText('开始升级')
        self.stop_update_b = QtGui.QPushButton()
        self.stop_update_b.setText('停止')

        self.dummy_l = QtGui.QLabel()
        self.remote_update_gbox = QtGui.QGridLayout()
        self.remote_update_gbox.setMargin(15)
        self.remote_update_gbox.setSpacing(3)
        self.remote_update_gbox.addWidget(self.file_label, 1, 0)
        self.remote_update_gbox.addWidget(self.file_open_b, 1, 1)

        self.remote_update_gbox.addWidget(self.file_path_box, 2, 0, 1, 5)

        self.remote_update_gbox.addWidget(self.dummy_l, 3, 0)

        self.remote_update_gbox.addWidget(self.block_size_label, 4, 0)
        self.remote_update_gbox.addWidget(self.block_size_combo, 4, 1)

        self.remote_update_gbox.addWidget(self.dummy_l, 5, 0)

        self.remote_update_gbox.addWidget(self.file_size_label, 6, 0)
        self.remote_update_gbox.addWidget(self.file_size_num_label, 6, 1)
        self.remote_update_gbox.addWidget(self.block_label, 6, 3)
        self.remote_update_gbox.addWidget(self.block_num_label, 6, 4)

        self.remote_update_gbox.addWidget(self.dummy_l, 7, 0)

        self.remote_update_gbox.addWidget(self.start_update_b, 8, 0, 1, 4)
        self.remote_update_gbox.addWidget(self.stop_update_b, 8, 4)
        self.setLayout(self.remote_update_gbox)

