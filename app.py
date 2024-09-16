from PyQt5.QtWidgets import QApplication , QMessageBox

from os import system

from mainwindow import Kirish_Window 
from loginwindow import Login_Window 
from registerwindow import Register_Window 
from tizim import Tizim_Window 

from database import Database


system("cls")



class App:
     def __init__(self) -> None:
          self.boshsahifa=Kirish_Window()
          self.registersahifa=Register_Window()
          self.loginsahifa=Login_Window()
          self.tizimsahifa=Tizim_Window()
          
          self.dbase=Database()


          self.boshsahifa.show()
          self.boshsahifa.tizimga_kirish_btn.clicked.connect(self.login_func)

          self.boshsahifa.royxat_otish_btn.clicked.connect(self.register_func)


     def register_func(self):
          self.registersahifa.show()
          self.boshsahifa.close()
          

          self.registersahifa.saqlash_btn.clicked.connect(self.malumot_saqlash_func)
          self.registersahifa.orqaga_register_btn.clicked.connect(self.back_main_window_func)

     def login_func(self):
          self.loginsahifa.show()
          self.boshsahifa.close()
          self.loginsahifa.tekshirish_btn.clicked.connect(self.tekshirsh_func)
          self.loginsahifa.orqaga_login_btn.clicked.connect(self.back_main_window_func)



          
         


     def back_main_window_func(self):
          self.boshsahifa.show()
          self.registersahifa.close()
          self.loginsahifa.close()
          


     def malumot_saqlash_func(self):
          surname=self.registersahifa.surname_input.text()

          name=self.registersahifa.name_input.text()

          username=self.registersahifa.userneme_input.text()

          password=self.registersahifa.password_input.text()

          try :
               password=int(password)
          except :
               self.msgbox=QMessageBox(self.registersahifa)
               self.msgbox.setText("Xato kiritilgan ma'lumot turi")
               self.msgbox.exec()
               return
          
          if surname and name and password and username :
                try :
                    self.dbase.INSERT_USER(surname , name , username , password)
                    self.msbox=QMessageBox(self.registersahifa)
                    self.msbox.setText("Ma'lumotlar muofaqqiyatli saqlandi ")
                    self.msbox.exec()
                    self.write_welcome_register()
                    self.tizimsahifa.show()
                    self.registersahifa.close()
                    
                    
               

                except :
                    self.msgbox=QMessageBox(self.registersahifa)
                    self.msgbox.setText("Xato kiritilgan ma'lumot turi")
                    self.msgbox.exec()
          else :
               self.msbox=QMessageBox(self.registersahifa)
               self.msbox.setText("Ma'lumotlar to'liq kiritilmadi !")
               self.msbox.exec()
               

     def tekshirsh_func(self):
          username=self.loginsahifa.username_input.text().strip()
          password=self.loginsahifa.password_input.text().strip()

          

          try:
               password=int(password)
          except :
               self.msbox=QMessageBox(self.loginsahifa)
               self.msbox.setText("Xato kiritilgan ma'lumot turi")
               self.msbox.exec()
               return
          

          data=self.dbase.Get_User(username , password)

          if data[0] == username and data[1] == password:
               self.msbox=QMessageBox(self.loginsahifa)
               self.msbox.setText("Muofaqiyatli tizimga kirdingiz")
               self.msbox.exec()
               self.write_welcome_login()

               self.tizimsahifa.show()
               self.loginsahifa.close()
               

          else :
               self.msbox=QMessageBox(self.loginsahifa)
               self.msbox.setText("Xato kiritilgan ma'lumotlar")
               self.msbox.exec()



     def write_welcome_register(self):
          user_name=self.registersahifa.userneme_input.text()
          password=self.registersahifa.password_input.text()
          password=int(password)
          data=self.dbase.Get_User(user_name, password)

          self.tizimsahifa.welcome_label.setText(data[2])


     def write_welcome_login(self):
          user_name=self.loginsahifa.username_input.text()
          password=self.loginsahifa.password_input.text()
          password=int(password)

          data=self.dbase.Get_User(user_name , password)

          self.tizimsahifa.welcome_label.setText(data[2])

           



app=QApplication([])
main=App()
app.exec()




