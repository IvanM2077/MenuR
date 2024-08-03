import sys
import os
import Views.View
import Models.DB

# Agrega el directorio raíz del proyecto a sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#Inicia la app
myapp = Views.View.App()
myapp.initialize_app()
