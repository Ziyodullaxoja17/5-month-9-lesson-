import mysql.connector 
from os import system
from colorama import init , Fore 

system("cls")
init(autoreset=True)



class Database:
     def __init__(self) -> None:
          self.data_base=mysql.connector.connect(
               host = "localhost",
              user = "root" ,
              password = "111317"
          )
          self.kursor=self.data_base.cursor()

          self.__Set_Up_Database()
     
     def __Set_Up_Database(self):
          self.kursor.execute("CREATE DATABASE IF NOT EXISTS DATABASE_USERS;")

          self.kursor.execute("USE DATABASE_USERS;")

          self.kursor.execute("""
          CREATE TABLE IF NOT EXISTS USERS (
          SURNAME VARCHAR(32),
          NAME VARCHAR(32),
          USERNAME VARCHAR(32) UNIQUE,
          PASSWORD INT
                              );
""")
          print(Fore.GREEN+ "# DATABASE YARATILINDI ")


     def INSERT_USER(self, surname , name , username , password):
          try:
               self.kursor.execute("""INSERT INTO USERS VALUES (%s , %s , %s , %s );""",(surname , name , username , password))

               self.data_base.commit()

               print(Fore.GREEN+ "# MA'LUMOT MUOFAQQIYATLI YOZILDI ")
          except :
               print(Fore.RED + "ERROR")
               return 1
     

     def Get_User(self , username , password):

          try:
               self.kursor.execute("SELECT USERNAME , PASSWORD  , NAME FROM USERS WHERE USERNAME = %s and PASSWORD = %s ;", (username , password))
               data_user=self.kursor.fetchone()
               data_user=list(data_user)

               return data_user
          except :
               print(Fore.RED +"# USER TOPILMADI")
               return 1
     

     def Get_Name(self ,username , password):
          self.kursor.execute("""
          SELECT NAME FROM USERS WHERE USERNAME = %s and PASSWORD = %s;
""" , (username , password))
          name_user=self.kursor.fetchone()
          name=str(name_user)
          return name
          
     












database=Database()
#database.INSERT_USER("Tursunboyev" , "Ziyodulla" , "Yakudza17" , 12345)
#data=database.Get_User("Yakudza17" , 12345)


