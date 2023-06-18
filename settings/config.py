from pathlib import Path
import json
SETTINGS = r'settings'
SETTINNG_FOLDER= Path(Path.cwd()/SETTINGS)
DB_CONFIG_PATH = Path(SETTINNG_FOLDER/'db_config.json')

V_1= Path(Path.cwd()/'version'/'v1')
V_2= Path(Path.cwd()/'version'/'v2')

DATA_BASE= Path(Path.cwd()/'version'/'databases.py')

DOCS_FOLDER= Path(Path.cwd()/'docs')
