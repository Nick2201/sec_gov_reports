from pathlib import Path

from bs4 import BeautifulSoup
import re
import pandas as pd
# D:\4. Programming\ProjectsSoftware\2_ai\get_reports\docs\10-Q_1.html
print(Path.cwd('..'))

# load_link = Path(Path.cwd()/"docs"/"10-Q_1.html")
#
# with open(load_link,'r') as f:
#     doc = f.read()
#
# # after = "Document - Document and Entity"
#
# soup = BeautifulSoup(doc, 'html.parser')
#
#
# tables = soup.find_all('table')
# print(len(tables))
#
# '''
#     CHECK first potential first worked table
# '''
# _tables = []
# for table in tables[6:7]:
#     rows = table.find_all('tr')
#     for row in rows:
#         cells = row.find_all('td')
#         if cells:
#             row_data = [cell.text.strip() for cell in cells]
#             # print(row_data)
#             _tables.append(row_data)
#
# frame = pd.DataFrame(data=_tables)
# print(frame.to_string())