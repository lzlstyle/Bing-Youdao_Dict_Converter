#--coding:utf-8--

import xml.etree.ElementTree as ET

def GetElementRoot(xmlFile):
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	return root

def GetBingElementRoot(xmlFile):
	root = GetElementRoot(xmlFile)
	return root.find('Phrases')

def MergeYDDict(firstXmlRoot, secondXmlRoot):      
	return MergeDict('wordbook', firstXmlRoot, secondXmlRoot)  

def MergeBingDict(firstXmlRoot, secondXmlRoot):	
	return MergeDict('FCVocaPhraseList', firstXmlRoot, secondXmlRoot)        
	

def MergeDict(topElementName, firstXmlRoot, secondXmlRoot):
        root = ET.Element(topElementName)        
	firstXmlRoot.extend(secondXmlRoot.getchildren())
	root.append(firstXmlRoot)
	return root

def Save(root, outputPath='result.xml'):
	tree = ET.ElementTree(root)
	tree.write(outputPath, encoding='utf-8')


if __name__ == '__main__':
        '''
        Test example
        '''
        root = GetBingElementRoot('old.xml')
        second = GetBingElementRoot('new.xml')
        newroot = MergeBingDict(root, second)
        Save(newroot)

