import sys
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
                            QTextBrowser, QComboBox, QHBoxLayout, QVBoxLayout

from books.spiders.book import BookSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from multiprocessing import Process, Manager
from scrapy.crawler import CrawlerProcess


def crawl(Q, ua, is_obey):
    # CrawlerProcess
    process = CrawlerProcess(settings={
        'USER_AGENT': ua,
        'ROBOTSTXT_OBEY': is_obey,
        # 'HTTPPROXY_ENABLED': False
        # 在Mac系统上，请加上'HTTPPROXY_ENABLED': False
    })

    process.crawl(BookSpider, Q=Q)
    process.start()

    # CrawlerRunner
    """runner = CrawlerRunner(settings={
        'USER_AGENT': ua,
        'ROBOTSTXT_OBEY': is_obey
        # 'HTTPPROXY_ENABLED': False
        # 在Mac系统上，请加上'HTTPPROXY_ENABLED': False
    })

    d = runner.crawl(BookSpider, Q=Q)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()"""


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle('PyQt5与Scrapy')

        self.ua_line = QLineEdit(self)                   # 输入USER_AGENT
        self.obey_combo = QComboBox(self)                # 选择ROBOTSTXT_OBEY
        self.obey_combo.addItems(['是', '否'])
        self.log_browser = QTextBrowser(self)            # 日志输出框
        self.crawl_btn = QPushButton('开始爬取', self)    # 开始爬取按钮
        self.crawl_btn.clicked.connect(self.crawl_slot)

        # 布局
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(QLabel('输入User-Agent'))
        self.h_layout.addWidget(self.ua_line)
        self.h_layout.addWidget(QLabel('是否遵循Robot协议'))
        self.h_layout.addWidget(self.obey_combo)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(QLabel('日志输出框'))
        self.v_layout.addWidget(self.log_browser)
        self.v_layout.addWidget(self.crawl_btn)
        self.setLayout(self.v_layout)

        self.Q = Manager().Queue()
        self.log_thread = LogThread(self)

    def crawl_slot(self):
        if self.crawl_btn.text() == '开始爬取':
            self.log_browser.clear()
            self.crawl_btn.setText('停止爬取')
            ua = self.ua_line.text().strip()
            is_obey = True if self.obey_combo.currentText() == '是' else False
            self.p = Process(target=crawl, args=(self.Q, ua, is_obey))
            self.p.start()
            self.log_thread.start()
        else:
            self.crawl_btn.setText('开始爬取')
            self.p.terminate()
            self.log_thread.terminate()

    def closeEvent(self, event):
        self.p.terminate()
        self.log_thread.terminate()


class LogThread(QThread):
    def __init__(self, gui):
        super(LogThread, self).__init__()
        self.gui = gui

    def run(self):
        while True:
            if not self.gui.Q.empty():
                self.gui.log_browser.append(self.gui.Q.get())

                # 确保滑动条到底
                cursor = self.gui.log_browser.textCursor()
                pos = len(self.gui.log_browser.toPlainText())
                cursor.setPosition(pos)
                self.gui.log_browser.setTextCursor(cursor)

                if '爬取结束' in self.gui.log_browser.toPlainText():
                    self.gui.crawl_btn.setText('开始爬取')
                    break

                # 睡眠10毫秒，否则太快会导致闪退或者显示乱码
                self.msleep(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
