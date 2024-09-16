from PyQt5.QtWidgets import QWidget
from companents import Label, Button, Image  

class Kirish_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 800)
        self.setWindowTitle("Uzbek_Chat")

        
        self.image = Image("images.jpg", self)
        self.image.setGeometry(0 , 0 , 600 , 800) 
        self.kirish_label = Label(self, "Xush Kelibsiz!", 150, 200)

       
        self.tizimga_kirish_btn = Button("Tizimga kirish", 400, self)
        self.royxat_otish_btn = Button("Ro'yxatdan o'tish", 480, self)

       