from PyQt5.QtWidgets import  QWidget 
from companents import Label , Image



class Tizim_Window(QWidget):
     def __init__(self):
          super().__init__()

          self.resize(600 , 800 )
          self.image_tizim=Image("images.jpg" , self)
          self.image_tizim.setGeometry(0 , 0 , 600 , 800)
          self.setWindowTitle("Xush Kelibsiz")

          self.tizim_label=Label(self , "Xush Kelibsiz !" , 150,300)
          self.welcome_label=Label(self , " " , 180 , 400)



