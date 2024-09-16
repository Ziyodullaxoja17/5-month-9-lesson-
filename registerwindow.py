from PyQt5.QtWidgets import QWidget 
from companents import Label , Button , Input , Image

class Register_Window(QWidget):
     def __init__(self):
          super().__init__()
          self.resize(600 , 800)
          self.Image = Image("image2.jpg", self)
          self.Image.setGeometry(0 , 0 , 600 , 800)


          self.register_label=Label(self , "Registratsiya" ,160 ,200)
          
          self.surname_input=Input(self , "Surname" , 300)
          self.name_input=Input(self , "Name" , 370)
          self.userneme_input=Input(self , "Username" , 440) 
          self.password_input=Input(self , "Password" , 510)


          self.saqlash_btn=Button("Saqlash" , 600 , self)
          self.orqaga_register_btn=Button("Orqaga" , 670 , self)


