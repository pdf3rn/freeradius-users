import sys

import requests
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from bs4 import BeautifulSoup

from ui import mainUI, loginwUI


def get_csrf_magic(text):
    var = 'var csrfMagicToken = "'
    pos = text.find(var) + len(var)
    return text[pos:pos + 55]


def get_page_title(txt):
    soup = BeautifulSoup(txt, "html.parser")
    div = soup.body.find("div", attrs={"class": "text-danger"})
    error = None if div is None else div.find("h4")
    return soup.title.string if error is None else str(error)


def get_title(txt):
    soup = BeautifulSoup(txt, "html.parser")
    return str(soup.title.string)


class Main:
    def __init__(self):
        self.login_ui = None
        self.main_ui = None
        self.main_window = None
        # self.dialog_login = None
        self.session = None
        self.cookies = None
        self.hots_port = ""
        self.csrf = ""

    def setup_window(self, ui):
        if self.main_window is not None:
            self.main_window.destroy()
        self.main_window = QtWidgets.QMainWindow()
        ui.setupUi(self.main_window)
        self.main_window.show()

    def login(self):
        app = QtWidgets.QApplication(sys.argv)
        # self.main_window = QtWidgets.QMainWindow()
        # self.dialog_login = QtWidgets.QDialog()
        self.login_ui = loginwUI.Ui_MainWindow()
        self.setup_window(self.login_ui)
        self.login_ui.ehost.setFocus()
        self.login_ui.blogin.clicked.connect(self.request_login)
        self.main_window.show()
        # Create session
        self.session = requests.Session()
        sys.exit(app.exec_())

    def init_main_ui(self):
        self.main_ui = mainUI.Ui_MainWindow()

        self.setup_window(self.main_ui)
        self.main_ui.tFile.setColumnWidth(0, 200)
        self.main_ui.tFile.setColumnWidth(1, 150)
        self.main_ui.tFile.setColumnWidth(3, 50)

        self.main_ui.bsearch.clicked.connect(self.select_path)
        self.main_ui.brandom.clicked.connect(self.random_pass)
        self.main_ui.bsend.clicked.connect(self.send_users)
        self.main_window.show()

    def show_login(self):
        self.login_ui.setupUi(self.main_window)
        self.main_window.show()

    def disable_inputs(self, enable=False):
        self.login_ui.chttp.setEnabled(enable)
        self.login_ui.ehost.setEnabled(enable)
        self.login_ui.eport.setEnabled(enable)
        self.login_ui.euser.setEnabled(enable)
        self.login_ui.epass.setEnabled(enable)
        self.login_ui.blogin.setEnabled(enable)

    def get__csrf_magic(self, url):
        response = self.session.get(url)
        return get_csrf_magic(response.text)

    def test_login(self):
        response = self.session.get(self.hots_port + "pkg.php?xml=freeradius.xml")
        self.csrf = get_csrf_magic(response.text)
        return "Login" in get_title(response.text)

    def request_login(self):
        if self.login_ui.ehost.text().strip() == "":
            self.login_ui.ehost.setFocus()
            return
        elif self.login_ui.euser.text().strip() == "":
            self.login_ui.euser.setFocus()
            return
        elif self.login_ui.epass.text().strip() == "":
            self.login_ui.epass.setFocus()
            return
        elif self.login_ui.eport.value() < 1000:
            self.login_ui.eport.setFocus()
            return
        self.disable_inputs()
        http = self.login_ui.chttp.currentText()
        host = self.login_ui.ehost.text()
        port = self.login_ui.eport.text()
        user = self.login_ui.euser.text()
        passw = self.login_ui.epass.text()
        self.hots_port = "{}://{}:{}/".format(http, host, port)
        url = "{}index.php".format(self.hots_port)
        self.test_login()
        payload = {
            "__csrf_magic": self.csrf,
            "usernamefld": user,
            "passwordfld": passw,
            "login": "Sign In"
        }
        response = self.session.request("POST", url, data=payload, cookies=self.cookies, verify=False)
        self.cookies = response.cookies

        if self.test_login():
            self.login_ui.lerror.setText(get_page_title(response.text))
            self.disable_inputs(True)
            # self.setup_window(self.login_ui)
            # self.main_window.show()
        else:
            self.init_main_ui()
            self.main_ui.ecount.setText(str(self.get_user_count()))

    def get_user_count(self):
        res = self.session.get(self.hots_port + "pkg.php?xml=freeradius.xml")
        self.csrf = get_csrf_magic(res.text)
        correct_text = res.text.replace('</tbody>', "").replace('<body>', "")
        soup = BeautifulSoup(correct_text, "html.parser")
        table = soup.body.find("table", {"id": "mainarea"})
        tbody = None if table is None else table.find("tbody")
        rows = [] if tbody is None else tbody.findAll("tr", "sortable")
        return len(rows)

    def select_path(self):
        fname = QFileDialog.getOpenFileName(self.main_window, 'Abrir archivo', '', "CSV (*.csv)")
        self.main_ui.epath.setText(fname[0])
        self.main_ui.tFile.setRowCount(0)
        if fname[0] != '':
            self.load_table(fname[0])

    def random_pass(self):
        import string
        import random
        string_length = 6
        letters = string.ascii_letters
        for i in range(0, self.main_ui.tFile.rowCount()):
            passw = ''.join(random.choice(letters) for i in range(string_length))
            self.main_ui.tFile.setItem(i, 1, QTableWidgetItem(passw))

    def disable_items(self, enable=False):
        self.main_ui.bsearch.setEnabled(enable)
        self.main_ui.bsend.setEnabled(enable)
        self.main_ui.brandom.setEnabled(enable)
        self.main_ui.tFile.setEnabled(enable)

    def send_users(self):
        self.main_ui.progressBar.setMaximum(self.main_ui.tFile.rowCount())
        self.disable_items()
        for i in range(0, self.main_ui.tFile.rowCount()):
            ret = self.make_user_request(i)
            self.main_ui.progressBar.setValue(i)
            item = QTableWidgetItem(ret)
            item.setForeground(QtGui.QBrush(QtGui.QColor("green")))
            self.main_ui.tFile.setItem(i, 2, item)
            print(self.main_ui.tFile.item(i, 0).text())
        self.disable_items(True)
        self.main_ui.progressBar.setValue(0)

    def make_user_request(self, index):
        url = self.hots_port + "pkg_edit.php?xml=freeradius.xml&id=9999999999"
        payload = {
            "__csrf_magic": self.csrf,
            "varusersusername": self.main_ui.tFile.item(index, 0).text(),
            "varuserspassword": self.main_ui.tFile.item(index, 1).text(),
            "varuserspasswordencryption": self.main_ui.varuserspasswordencryption.currentText(),
            "varusersauthmethod": self.main_ui.varusersauthmethod.currentText(),
            "varuserssimultaneousconnect": str(self.main_ui.varuserssimultaneousconnect.value()),
            "varusersmaxtotaloctets": str(self.main_ui.varusersmaxtotaloctets.value()),
            "varusersmaxtotaloctetstimerange": self.main_ui.varusersmaxtotaloctetstimerange.currentText(),
            "varusersmaxbandwidthdown": str(self.main_ui.varusersmaxbandwidthdown.value()),
            "varusersmaxbandwidthup": str(self.main_ui.varusersmaxbandwidthup.value()),
            "xml": "freeradius.xml",
            "id": "9999999999",
        }
        response = self.session.request("POST", url, data=payload, cookies=self.cookies, verify=False)
        self.csrf = get_csrf_magic(response.text)
        # self.cookies = response.cookies
        return "OK"

    def load_table(self, filename):
        import csv
        with open(filename, 'r') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            print(dialect)
            reader = csv.reader(csvfile, dialect)
            i = 0
            for row in reader:
                if len(row) > 0 and row[0].strip() != "":
                    print(i, row)
                    self.main_ui.tFile.setRowCount(i + 1)
                    self.main_ui.tFile.setItem(i, 0, QTableWidgetItem(row[0]))
                    if len(row) > 1 and row[1].strip() != "":
                        self.main_ui.tFile.setItem(i, 1, QTableWidgetItem(row[1]))
                    i += 1


if __name__ == "__main__":
    Main().login()
