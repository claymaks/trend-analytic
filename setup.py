import os


def install(requirements):
    f = open(requirements, "r")
    dep = f.read().split('\n')
    for module in dep:
        try:
            module_obj = __import__(module)
            globals()[module] = module_obj
            print(module, "already installed.")
        except ImportError:
            print(module, "not installed!")
            os.system("pip install {:s}".format(module))
            print(module, "now installed.")



install('requirements.txt')
