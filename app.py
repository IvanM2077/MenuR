import sys
import os

# Agrega el directorio raíz del proyecto a sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import Views.View

# Inicializa la aplicación
myapp = Views.View.App()
myapp.initialize_app()
