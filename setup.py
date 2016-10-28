#from ez_setup import use_setuptools
#use_setuptools()
#from setuptools import setup
from distutils.core import setup
import py2exe

'''setup(name = "Imca 1.0",
      version = "0.1",
      description = "Sistema de Administración del Instituto Municipal "\
      "de Cerámica de Avellaneda",
      author = "Gabriel García",
      author_email = "zootropo en gmail",
      url = "http://mundogeek.net/tutorial-python/",
      license = "GPL",
      scripts = ["imca.pyw"],
      packages = find_packages()
)'''
setup(console=['imca.pyw'])