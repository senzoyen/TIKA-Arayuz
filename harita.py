import sys
from PyQt5 import QtWidgets
from tikaArayuz import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Google Haritaları gösterecek QWebEngineView oluştur
        self.webview = QWebEngineView()

        api_key = 'AIzaSyAj7ypTczaVI3jfBYOQkenvxXwH1i7hqqg'
        location = '40.75611N,29.8176838E'
        url = f'https://www.google.com/maps/embed/v1/place?key={api_key}&q={location}'

        # URL'yi iframe olarak yükle
        self.webview.setHtml(f'<iframe width="100%" height="100%" frameborder="0" style="border:0" src="{url}" allowfullscreen></iframe>')

        # Ui_MainWindow içindeki 'map' adlı QFrame'e QWebEngineView'i ekleyin
        layout = QVBoxLayout(self.ui.map)
        layout.addWidget(self.webview)

def app():
        app = QApplication(sys.argv)
        win = MyApp()
        win.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app()