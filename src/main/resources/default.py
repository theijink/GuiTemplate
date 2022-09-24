import untangle
import os
import sys
#root,dirs,files=next(os.walk(sys.argv[0][:-len(sys.argv[0].split('/')[-1])]+'../python/'))
#[sys.path.append(root+file) for file in files]
#import Windows, Menus, Frames, Widgets
#print(sys.path)

if __name__=="__main__":
    config=sys.argv[0].split('/')[-1][:-3]
    configfile=sys.argv[0][:-len(config)-3]+'configuration.xml'
    obj = untangle.parse(configfile)
    #root = getattr(getattr(getattr(getattr(obj.configurations, config), 'root'), 'class'))
    #root = setattr(getattr(getattr(obj.configurations, config), 'root')['class'])
    root = getattr(eval(getattr(obj.configurations, config).root['class'].split('.')[0]), getattr(obj.configurations, config).root['class'].split('.')[1])

if False:
    from xml.etree import ElementTree
    config=sys.argv[0].split('/')[-1][:-3]
    configfile=sys.argv[0][:-len(config)-3]+'configuration.xml'
    configurations=ElementTree.parse(configfile).getroot()
    print([i for i in configurations.findall(config)])