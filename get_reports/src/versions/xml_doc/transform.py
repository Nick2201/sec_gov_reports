from pathlib import Path
# from settings.config import DOCS_FOLDER
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re



file_1 = r'2_FilingSummary.xml'
file_2 = r'FilingSummary.xml'
file_3 = r'3_FilingSummary.xml'

DOCS_FOLDER = Path(r'D:\4. Programming\ProjectsSoftware\2_ai\get_reports\docs')

def get_info(file_name):
    xml_path = Path(DOCS_FOLDER/file_name)


    tree = ET.parse(xml_path)
    root = tree.getroot()
    # Print the tag and text of each element
    reports = []

    for elem in root.iter():

        if (elem.tag) == 'Report':
            _list = []
            for i in elem.iter():

                if (i.tag) == 'LongName':
                    el = i.text.split(' - ')
                    _list.extend(f for f in (el))
                if (i.tag) == 'ShortName':
                    _list.append(i.text)
                if (i.tag) == 'HtmlFileName':
                    _list.append(i.text)
            reports.append(_list)

    return(reports[:-1])



file_name = Path(DOCS_FOLDER/file_1)

comp_ticker='ABEO'
check_list = comp_ticker

all_ = []
for i in range(1,6):
    inner_path = (f'{comp_ticker}_{i}.xml')
    xml_path = Path(DOCS_FOLDER/inner_path)
    files = get_info(xml_path)
    all_.extend(files)
