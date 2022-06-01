#coding:utf-8
import os
import os.path
import xml.dom.minidom
 
#path="../xml/"
path='/home/mozhe/test/fire_hydrant/Annotations/'
files=os.listdir(path) 
for xmlFile in files:
	if not os.path.isdir(xmlFile): 
		dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
		root=dom.documentElement
		name=root.getElementsByTagName('name')#获取特定tag的内容
		for i in range(len(name)):
			print(name[i].firstChild.data)
			if name[i].firstChild.data=='fire_faucet':
				name[i].firstChild.data='firefaucet'#修改tag		
		#save
		with open(os.path.join(path,xmlFile),'w') as fh:
			dom.writexml(fh)
			print('Success!')