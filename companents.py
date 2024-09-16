from PyQt5.QtWidgets import QLabel  , QWidget , QPushButton , QLineEdit
from PyQt5.QtGui import QPixmap



class Label(QLabel):
     def __init__(self ,oyna : QWidget , text ,x, y  ):
          super().__init__(oyna)
          self.setText(text)
          self.move(x, y)

          self.setStyleSheet("""
     font-size : 50px
""")
          

class Button(QPushButton):
     def __init__(self , text , y , oyna):
          super().__init__(oyna)
          self.setText(text)
          self.resize(200 , 50)
          self.move(200 , y)
          self.setStyleSheet("""
            QPushButton {
            background-color: white;
            font-size: 22px;
        }
        QPushButton:hover {
            background-color: green;
        }
        """)

          
class Input(QLineEdit):
     def __init__(self , oyna , text , y ):
          super().__init__(oyna)
          self.setPlaceholderText(text)
          self.resize(400 , 50)
          self.move(100 , y)
          self.setStyleSheet("""
          font-size : 22px;
          border  : 2px solid black;
          """)
          



class Image(QLabel):
    def __init__(self, image_path, window):
        super().__init__(window)
        try:
            pixmap = QPixmap(image_path)
            self.setPixmap(pixmap)
            self.setScaledContents(True)
        except Exception as e:
            print(e)
            self.setText("Image not found")


