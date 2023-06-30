# DataFrames
## Basic
#RAW : df_descriptive : ['id', 
    'symbol', 'longName', 
    'sector', 'industry', 'country','exchange'
       
    'longBusinessSummary', 'fullTimeEmployees', 
    'website', 'logo_url',
       ]


#RAW : df_report_links_raw : ['id', 
    'cik', 'ticker', 'title', 
    'date_added', 'date_publication',
    'quartal', 'url_report'
    ]

## GROUPED

df_companies: ['symbol',"sector",'industry','country',"longName","longBusinessSummary",'fullTimeEmployees','unique_url']

## worked
worked_df : ['ticker','date_publication','quartal','url_report','sector','industry']

selected_first_5


###
test_group_df: 
    - ['ticker', 'date_publication', 'quartal', 'url_report', 'sector', 'industry']
test_group_tickers:  ['A', 'ABC', 'ABEO', 'ABIO', 'ABT', 'ABVC', 'ACAD', 'ACER', 'ACHC',
       'ACOR', 'ACRX', 'ADMP', 'ADUS', 'AEMD', 'AHPI', 'ALGN', 'ALIM',
       'ALR', 'AMED', 'AMEH', 'ANGO', 'ANIK', 'ANIP', 'APDN', 'ATR',
       'ATRC', 'ATRI', 'AWH', 'AXDX', 'AZTA', 'BIIB', 'BIMI', 'BMY',
       'CAH', 'CEMI', 'CNC', 'CPSI', 'CVS', 'GILD', 'HSIC', 'HSTM',
       'HZNP', 'JNJ', 'LFMD', 'LFMDP', 'MCK', 'MDRX', 'MDVL', 'NRC',
       'NXGN', 'OMI', 'PETS', 'UNH']