import os

if __name__=="__main__":
    for name in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if name.endswith(".py") and not name in __file__:
            #strip the extension
            module = name[:-3]
            # set the module name in the current global name space:
            globals()[module] = __import__(os.path.join(os.path.dirname(os.path.abspath(__file__)).split('/')[-1], name))