#--coding:utf-8--

import xml.etree.ElementTree as ET
import datetime

def GetElementRoot(xmlFile):
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	return root

def Youdao2Bing(youdaoXmlRoot):
	bingRoot = ET.Element('FCVocaPhraseList')
	phrases = ET.SubElement(bingRoot, 'Phrases')
	youdaoItems = youdaoXmlRoot.getchildren() # get all the items from the wordbook root node
	for item in youdaoItems:
		phrase = ET.SubElement(phrases, 'Phrase')
		YoudaoNode2BingNode(item, phrase)
	
	print bingRoot
	return bingRoot

Youdao2BingLamda = {
		'word': lambda value: {'Eng': value},
		'phonetic': lambda value: {'Phonetic': value},
		'tags': lambda value: None,
		'progress': lambda value: None,
		'trans': lambda value: {'Defi': (value, u'\u7a7a')[value is None]},
		}

def YoudaoNode2BingNode(youdaoElement, bingElement):
	datetimeofNow = GenTimeofNow()
	for child in youdaoElement.getchildren():
		temp = Youdao2BingLamda[child.tag](child.text)
		if temp is not None:
			newNode = ET.SubElement(bingElement, temp.keys()[0])
			newNode.text = temp.values()[0]
	# add a datetime node
	newNode = ET.SubElement(bingElement, 'Date')
	newNode.text = datetimeofNow

def GenTimeofNow():
	now = datetime.datetime.now()
	return now.strftime('%y-%m-%d %H:%M:%S')

def Save(root):
	tree = ET.ElementTree(root)
	tree.write('result.xml', encoding='utf-8')

if __name__ == '__main__':
        '''
        Test example
        '''
        root = GetElementRoot('youdaodict.xml')
        newroot = Youdao2Bing(root)
        Save(newroot)
