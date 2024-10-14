from PyQt5 import QtWidgets
from tikaArayuz import Ui_MainWindow
import sys
import cv2
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout,QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class myApp(QtWidgets.QMainWindow):
    def __init__(self, camera_url):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.cap = cv2.VideoCapture(camera_url)
        if not self.cap.isOpened():
            print("hata")
            sys.exit()

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        
        # layout1 = QVBoxLayout(self.ui.modelt)
        # layout1.addWidget(self.webview)
        

        
        self.initUI()
        self.maps()
        

    def initUI(self):
        self.setWindowTitle('Kamera Görüntüsü')
        self.image_label = QLabel(self)
        self.ui.camera.addWidget(self.image_label)  

    def maps(self):      
        self.webview = QWebEngineView()

        api_key = 'AIzaSyAj7ypTczaVI3jfBYOQkenvxXwH1i7hqqg'
        location = '40.75611N,29.8176838E'
        url = f'https://www.google.com/maps/embed/v1/place?key={api_key}&q={location}'

        # URL'yi iframe olarak yükle
        self.webview.setHtml(f'<iframe width="100%" height="100%" frameborder="0" style="border:0" src="{url}" allowfullscreen></iframe>')

        # Ui_MainWindow içindeki 'map' adlı QFrame'e QWebEngineView'i ekleyin
        layout = QVBoxLayout(self.ui.map)
        layout.addWidget(self.webview)



    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (500, 500))  # Boyutlandırma
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Görüntüyü RGB formatına dönüştür
            height, width, channel = frame.shape
            step = channel * width  # Her piksel için bit adedi
            qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)  

            self.image_label.setPixmap(QPixmap.fromImage(qImg))  

    def closeEvent(self, event):
        self.cap.release()  
def app():
    app = QtWidgets.QApplication(sys.argv)
    camera_url = "http://192.168.117.164:8080/video"  
    win = myApp(camera_url)
    win.show() 
    sys.exit(app.exec_())  

if __name__ == "__main__":
    app()