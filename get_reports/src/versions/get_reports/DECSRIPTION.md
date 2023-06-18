# DataFrames
df_descriptive : ['id', 
    'symbol', 'longName', 
    'sector', 'industry', 'country','exchange'
       
    'longBusinessSummary', 'fullTimeEmployees', 
    'website', 'logo_url',
       ]


df_report_links : ['id', 
    'cik', 'ticker', 'title', 
    'date_added', 'date_publication',
    'quartal', 'url_report'
    ]

## GROUPED
#RAW:>> grouped_reports 

df_companies: ['symbol',"sector",'industry','country',"longName","longBusinessSummary",'fullTimeEmployees','unique_url']

##
worked_df
selected_first_5


###
test_group: 
    - ['ticker', 'date_publication', 'quartal', 'url_report', 'sector', 'industry']
    - ['A', 'ABC', 'ABEO', 'ABIO', 'ABT', 'ABVC', 'ACAD', 'ACER', 'ACHC',
       'ACOR', 'ACRX', 'ADMP', 'ADUS', 'AEMD', 'AHPI', 'ALGN', 'ALIM',
       'ALR', 'AMED', 'AMEH', 'ANGO', 'ANIK', 'ANIP', 'APDN', 'ATR',
       'ATRC', 'ATRI', 'AWH', 'AXDX', 'AZTA', 'BIIB', 'BIMI', 'BMY',
       'CAH', 'CEMI', 'CNC', 'CPSI', 'CVS', 'GILD', 'HSIC', 'HSTM',
       'HZNP', 'JNJ', 'LFMD', 'LFMDP', 'MCK', 'MDRX', 'MDVL', 'NRC',
       'NXGN', 'OMI', 'PETS', 'UNH']