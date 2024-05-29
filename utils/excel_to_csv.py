import pandas as pd
import os

filename = 'PCT Data - Clean and Reduced.xlsx'
dataset = pd.read_excel('../datasets/' + filename)

namemap = {
    'QAR#': 'QAR',
    'Supplier/Grower': 'supplier_grower',
    'District Abb.': 'district',
    'Ward Abb.': 'ward',
    'Village': 'village',
    'Field Assistant': 'field_assistant',
    'Buying Agent': 'buying_agent',
    'BAGS': 'bags',
    'NET, KG': 'weight_net',
    'Comments': 'comment',
    'kgs, A.I.': 'weight_assay',
    'MC, w%': 'moisture_pct',
    'Dry Flower Py %': 'dry_pct'

}

dataset.rename(columns=namemap, inplace=True)
dataset.to_csv('../datasets/stats-data.csv', index=False)