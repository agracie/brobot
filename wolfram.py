import urllib 
import os
from xml.etree import ElementTree as ET

wolfkey = os.environ["WOLFKEY"]
url = "http://api.wolframalpha.com/v2/query?input=" 

#text = raw_input()

def wolf_answer(text):
    
    tree = ET.parse(urllib.urlopen(url + text + "&appid=" + wolfkey))
    root = tree.getroot()
    pt_ans = {}
    for i in tree.findall('pod'):
        for g in [m for m in list(i) if m.tag=='subpod']:
            for x in [n for n in list(g) if n.tag=='plaintext']:
                if x.tag=='plaintext':
                    pt_ans[i.get('title')] = x.text

    return pt_ans

def get_result(text):
    result = wolf_answer(text)
    if 'Result' in result:
        return str(result['Result'])
    else:
        return "Please try another question."    
    
#print (get_result(text))

##math is still broken, need to add support for multiple results, and update test_brobot 
