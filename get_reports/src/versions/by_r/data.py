from dataclasses import dataclass
from typing import List

'''
    1. 

'''
"Janux Therapeutics, Inc. : 0001817713"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017021001188"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017021003738"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017022004171"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017022008984"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017022016082"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017022024511"
"https://www.sec.gov/Archives/edgar/data/0001817713/000095017023007311"


@dataclass
class Company:
    title:          str
    comp_ticker:    str
    com_cik:        str
    comp_links:     List  # LIST of specific links: as R


JANX = Company(
    title="Janux Therapeutics, Inc.",
    comp_ticker="JANX",
    com_cik=str("0001817713"),
    comp_links=[
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017021001188",
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017021003738",
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017022004171",
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017022008984",
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017022016082",
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017022024511",
        "https://www.sec.gov/Archives/edgar/data/0001817713/000095017023007311",
    ],
)
ADSK = Company(
    comp_links=["https://www.sec.gov/Archives/edgar/data/0000769397/000119312509124260",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312509183342",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312509249297",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312510061070",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312510132539",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312510202279",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312510275686",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312511071209",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312511158515",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312511239152",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000119312511332153",
    "https://www.sec.gov/Archives/edgar/data/0000769397/000076939712000005",],
     title="Autodesk, Inc.",
     com_cik=str("0000769397"),
    comp_ticker="ADSK",
)

