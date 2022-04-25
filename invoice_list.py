import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from db_access import *
from invoice_window import InvoiceWindow
from invoice_controller import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.view_button = QPushButton("View", self)
        self.list_widget = QListWidget(self)
        self.invoice_window = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Print Invoice")
        self.resize(800, 600)
        self.center()

        self.list_widget.setGeometry(25, 100, 571, 411)
        self.invoice_display()

        self.view_button.setGeometry(630, 267, 141, 71)
        self.view_button.clicked.connect(self.view_invoice)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def invoice_display(self):
        invoice_list = displayData()
        for obj in invoice_list:
            invoice = QListWidgetItem(str(obj.id))
            invoice.setTextAlignment(Qt.AlignHCenter)
            self.list_widget.addItem(invoice)

    def view_invoice(self):
        self.invoice_window = InvoiceWindow()
        self.clicked = self.list_widget.currentItem().text()
        invoice_obj = get_one(int(self.clicked))
        file_path = generate(invoice_obj)
        wd = os.path.dirname(sys.argv[0])
        self.invoice_window.webView.setUrl(QUrl(f"file://{wd}/{'2_invoice.pdf'}"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
