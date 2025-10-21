import requests
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from test_api import Ui_Test_Api

class Test_API(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Test_Api()
        self.ui.setupUi(self)
        self.setWindowTitle("Авторизация")
        self.url = f"http://localhost:4444/TransferSimulator/fullName"
        self.ui.btn_get.clicked.connect(self.get_info)
        self.ui.btn_send.clicked.connect(self.test_info)
    def get_info(self):
        answer = requests.get(self.url).json()["value"]
        print(answer)
        self.ui.label_info.setText(answer)
        self.ui.label_result.setText("")

    def test_info(self):
        a = self.ui.label_info.text()
        znaki = "1234567890!@#$%^&*()-+=/.:;\"\'><,`~"
        for i in a:
            if i in znaki:
                self.ui.label_result.setText("Присутствуют лишние символы")
                return 1
        self.ui.label_result.setText("Все чики-пуки")
if __name__ == "__main__":
    app = QApplication()
    root = Test_API()
    root.show()
    sys.exit(app.exec())