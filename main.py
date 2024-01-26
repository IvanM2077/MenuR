import math as m
import Login as L
import User as U
import OrderNtoN as O
import sqlite3 as sq
import Menu
import DB

#Crear bases de datos y tablas
DB.CreateDB()
DB.CreateTableOrderN()
DB.CreateTableProduct()
DB.CreateTableUser()



#Ejecución del menu
Menu.menu()




#user = U.Employee(2,3,4)




