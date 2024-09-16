from PyQt5.QtWidgets import  QWidget 
from os import system 
from companents import Label , Input , Button , Image



class Login_Window(QWidget):
     def __init__(self):
          super().__init__()

          self.resize(600 , 800)

          self.setWindowTitle("Login Window")

          self.image = Image("image1.jpg", self)
          self.image.setGeometry(0 , 0 , 600 , 800)

          self.login_label=Label(self , "Tizimga Kirish" ,150, 300)

          self.username_input=Input(self , "Username" , 400)
          self.password_input=Input(self , "Password" , 470)


          self.tekshirish_btn=Button("Kirish" , 600 , self)
          self.orqaga_login_btn=Button("Orqaga" , 670 , self)





