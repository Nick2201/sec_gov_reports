from pathlib import Path
from settings.config import DOCS_FOLDER
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re



file_2 = r'FilingSummary.xml'

# Parse an XML file
xml_path = Path(DOCS_FOLDER/"janx-20210630.xsd.xml")
xml_path = Path(DOCS_FOLDER/file_2)

def extract(_path_file):
    tree = ET.parse(_path_file)
    root = tree.getroot()

    # Print the tag and text of each element
    reports = []
    word = "Parenthetical"
    for elem in root.iter():

        if elem.tag == "{http://www.xbrl.org/2003/linkbase}definition":
            if re.search(word,elem.text):
                pass
            else:
                reports.append(elem.text)
    return (reports)


print(extract(xml_path))