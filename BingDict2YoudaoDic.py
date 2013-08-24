#--coding:utf-8--

import xml.etree.ElementTree as ET
import datetime

def GetElementRoot(xmlFile):
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	return root.find('Phrases')

def Bing2Youdao(bingXmlRoot):
	youdaoRoot = ET.Element('wordbook')
	bingItems = bingXmlRoot.getchildren() # get all the items from the root node
	for phrase in bingItems:
		item = ET.SubElement(youdaoRoot, 'item')
		BingNode2YoudaoNode(phrase, item)
	
	return youdaoRoot

Bing2YoudaoLamda = {
		'Eng': lambda value: {'word': value},
		'Phonetic': lambda value: {'phonetic': r'\<![CDATA[%s]]>' % value},
		'Date': lambda value: None,
		'Defi': lambda value: {'trans': (r'\<![CDATA[%s]]>' % value, ' ')[value is None or value =='' or value == u'\u7a7a']},
		}

def BingNode2YoudaoNode(bingElement, youdaoElement):
	for child in bingElement.getchildren():
		temp = Bing2YoudaoLamda[child.tag](child.text)
		if temp is not None:
			newNode = ET.SubElement(youdaoElement, temp.keys()[0])
			newNode.text = temp.values()[0]
	# add a tag node
	tagNode = ET.SubElement(youdaoElement, 'tags')
	tagNode.text = ''
	# add a progress node
	progressNode = ET.SubElement(youdaoElement, 'progress')
	progressNode.text = '1'

def Save(root, outputPath='result.xml'):
	tree = ET.ElementTree(root)
	tree.write(outputPath, encoding='utf-8')


if __name__ == '__main__':
        '''
        Test example
        '''
        root = GetElementRoot('example.xml')
        newroot = Bing2Youdao(root)
        Save(newroot)
