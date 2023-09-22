import pandas as pd
import os

"""
Clean, transform, merge downloaded data.
"""

YEARS = [2014, 2015, 2016, 2017, 2018, 2019]

def clean_NHIS(path='raw_data/nhis',
               outfile='artifacts/nhis_cleaned.csv'):
    if os.path.exists(outfile):
        return
    print('cleaning: ', path)
    # Cleaning code here

    nhis19 = pd.read_csv('raw_data/nhis/2019/adult19.csv')
    nhis18 = pd.read_csv('raw_data/nhis/2018/samadult.csv')
    nhis17 = pd.read_csv('raw_data/nhis/2017/samadult.csv')
    nhis16 = pd.read_csv('raw_data/nhis/2016/samadult.csv')
    nhis15 = pd.read_csv('raw_data/nhis/2015/samadult.csv')

    year = 2019
    nhis19['Year'] = year
    year = 2018
    nhis18['Year'] = year
    year = 2017
    nhis17['Year'] = year
    year = 2016
    nhis16['Year'] = year
    year = 2015
    nhis15['Year'] = year

    nhis19updated = nhis19[['REGION','AGEP_A','SEX_A','RACEALLP_A','DIBEV_A','DIBAGETC_A','DIBPILL_A','DIBINS_A',
    'HYPEV_A','HYPDIF_A','HYPMED_A','CHLEV_A','CHLMED_A',
    'CHDEV_A','ANGEV_A','MIEV_A','STREV_A','BLADDCAN_A','BLADDAGETC_A','BLOODCAN_A','BLOODAGETC_A',
    'COLONCAN_A','COLONAGETC_A','GALLBCAN_A','GALLBAGETC_A','LIVERCAN_A','LIVERAGETC_A','LUNGCAN_A','LUNGAGETC_A',
    'LYMPHCAN_A','LYMPHAGETC_A','PANCRCAN_A','PANCRAGETC_A','RECTUCAN_A','RECTUAGETC_A','STOMACAN_A',
    'STOMAAGETC_A','THYROCAN_A','THYROAGETC_A','RXDL12M_A','RXSK12M_A','RXDG12M_A','Year']]

    nhis19updated = nhis19updated.rename(columns={"AGEP_A": "AGE_P", "SEX_A": "SEX","RACEALLP_A":"RACERPI2","DIBEV_A":"DIBEV1","DIBAGETC_A":"DIBAGE1",
    "DIBPILL_A":"DIBPILL1","DIBINS_A":"INSLN1","HYPEV_A":"HYPEV","HYPDIF_A":"HYPDIFV","HYPMED_A":"HYPMED2","CHLEV_A":"CHLEV",
    "CHLMED_A":"CHLMDNW2","CHDEV_A":"CHDEV","ANGEV_A":"ANGEV","MIEV_A":"MIEV","STREV_A":"STREV","BLADDCAN_A":"CNKIND1",
    "BLOODAGETC_A":"CANAGE2","COLONCAN_A ":"CNKIND7","COLONAGETC_A":"CANAGE7","GALLBCAN_A":"CNKIND9","GALLBAGETC_A":"CANAGE9",
    "LIVERCAN_A":"CNKIND13","LIVERAGETC_A":"CANAGE13","LUNGCAN_A":"CNKIND14","LUNGAGETC_A":"CANAGE14","LYMPHCAN_A":"CNKIND15",
    "LYMPHAGETC_A":"CANAGE15","PANCRCAN_A":"CNKIND19","PANCRAGETC_A":"CANAGE19","RECTUAGETC_A":"CANAGE21","STOMACAN_A":"CNKIND25",
    "STOMAAGETC_A":"CANAGE25","THYROCAN_A":"CNKIND28","THYROAGETC_A":"CANAGE28","RXDL12M_A":"ARX12_3","RXSK12M_A":"ARX12_1","RXDG12M_A":"AHCAFYR1","BLADDAGETC_A":"CANAGE1","BLOODCAN_A":"CNKIND2","COLONCAN_A":"CNKIND7","RECTUCAN_A":"CNKIND21"})

    nhis18updated = nhis18[['REGION','AGE_P','SEX','RACERPI2','DIBEV1','DIBAGE1',
    'DIBPILL1','INSLN1','HYPEV','HYPDIFV','HYPMED2','CHLEV','CHLMDNW2','CHDEV',
    'ANGEV','MIEV','STREV','CNKIND1','CANAGE1','CNKIND2','CANAGE2','CNKIND7','CANAGE7',
    'CNKIND9','CANAGE9','CNKIND13','CANAGE13','CNKIND14','CANAGE14','CNKIND15','CANAGE15',
    'CNKIND19','CANAGE19','CNKIND21','CANAGE21','CNKIND25','CANAGE25','CNKIND28','CANAGE28','ARX12_3','ARX12_1','AHCAFYR1','Year']]

    nhis17updated = nhis17[['REGION','AGE_P','SEX','RACERPI2','DIBEV1','DIBAGE1',
    'DIBPILL1','INSLN1','HYPEV','HYPDIFV','HYPMED2','CHLEV','CHLMDNW2','CHDEV',
    'ANGEV','MIEV','STREV','CNKIND1','CANAGE1','CNKIND2','CANAGE2','CNKIND7','CANAGE7',
    'CNKIND9','CANAGE9','CNKIND13','CANAGE13','CNKIND14','CANAGE14','CNKIND15','CANAGE15',
    'CNKIND19','CANAGE19','CNKIND21','CANAGE21','CNKIND25','CANAGE25','CNKIND28','CANAGE28','ARX12_3','ARX12_1','AHCAFYR1','Year']]

    nhis16updated = nhis16[['REGION','AGE_P','SEX','RACERPI2','DIBEV1','DIBAGE1',
    'DIBPILL1','INSLN1','HYPEV','HYPDIFV','HYPMED2','CHLEV','CHLMDNW2','CHDEV',
    'ANGEV','MIEV','STREV','CNKIND1','CANAGE1','CNKIND2','CANAGE2','CNKIND7','CANAGE7',
    'CNKIND9','CANAGE9','CNKIND13','CANAGE13','CNKIND14','CANAGE14','CNKIND15','CANAGE15',
    'CNKIND19','CANAGE19','CNKIND21','CANAGE21','CNKIND25','CANAGE25','CNKIND28','CANAGE28','ARX12_3','ARX12_1','AHCAFYR1','Year']]

    nhis15updated = nhis15[['REGION','AGE_P','SEX','RACERPI2','DIBEV','DIBAGE',
    'DIBPILL','INSLN','HYPEV','HYPDIFV','HYPMED2','CHLEV','CHLMDNW2','CHDEV',
    'ANGEV','MIEV','STREV','CNKIND1','CANAGE1','CNKIND2','CANAGE2','CNKIND7','CANAGE7',
    'CNKIND9','CANAGE9','CNKIND13','CANAGE13','CNKIND14','CANAGE14','CNKIND15','CANAGE15',
    'CNKIND19','CANAGE19','CNKIND21','CANAGE21','CNKIND25','CANAGE25','CNKIND28','CANAGE28','ARX12_3','ARX12_1','AHCAFYR1','Year']]

    nhis15updated = nhis15updated.rename(columns={"DIBEV":"DIBEV1","DIBAGE":"DIBAGE1","DIBPILL":"DIBPILL1","INSLN":"INSLN1"})

    varmap = [{'REGION': { 'index': 33, 'length': 1}},
    {'AGE_P': { 'index': 48, 'length': 2}},
    {'SEX': { 'index': 39, 'length': 1}},
    {'RACERPI2': { 'index': 42, 'length': 2}},
    {'DIBEV1': { 'index': 246, 'length': 1}},
    {'DIBAGE1': { 'index': 248, 'length': 2}},
    {'DIBPILL1': { 'index': 253, 'length': 1}},
    {'INSLN1': { 'index': 252, 'length': 1}},
    {'HYPEV': { 'index': 79, 'length': 1}},
    {'HYPDIFV': { 'index': 80, 'length': 1}},
    {'HYPMED2': { 'index': 87, 'length': 1}},
    {'CHLEV': { 'index': 88, 'length': 1}},
    {'CHLMDNW2': { 'index': 94, 'length': 1}},
    {'CHDEV': { 'index': 95, 'length': 1}},
    {'ANGEV': { 'index': 96, 'length': 1}},
    {'MIEV': { 'index': 97, 'length': 1}},
    {'STREV': { 'index': 99, 'length': 1}},
    {'CNKIND1': { 'index': 125, 'length': 1}},
    {'CANAGE1': { 'index': 156, 'length': 3}},
    {'CNKIND2': { 'index': 126, 'length': 1}},
    {'CANAGE2': { 'index': 159, 'length': 3}},
    {'CNKIND7': { 'index': 131, 'length': 1}},
    {'CANAGE7': { 'index': 174, 'length': 3}},
    {'CNKIND9': { 'index': 133, 'length': 1}},
    {'CANAGE9': { 'index': 180, 'length': 3}},
    {'CNKIND13': { 'index': 137, 'length': 1}},
    {'CANAGE13': { 'index': 192, 'length': 3}},
    {'CNKIND14': { 'index': 138, 'length': 1}},
    {'CANAGE14': { 'index': 195, 'length': 3}},
    {'CNKIND15': { 'index': 139, 'length': 1}},
    {'CANAGE15': { 'index': 198, 'length': 3}},
    {'CNKIND19': { 'index': 143, 'length': 1}},
    {'CANAGE19': { 'index': 210, 'length': 3}},
    {'CNKIND21': { 'index': 145, 'length': 1}},
    {'CANAGE21': { 'index': 216, 'length': 3}},
    {'CNKIND25': { 'index': 149, 'length': 1}},
    {'CANAGE25': { 'index': 228, 'length': 3}},
    {'CNKIND28': { 'index': 152, 'length': 1}},
    {'CANAGE28': { 'index': 237, 'length': 3}},
    {'ARX12_3': { 'index': 869, 'length': 1}},
    {'ARX12_1': { 'index': 867, 'length': 1}},
    {'AHCAFYR1': { 'index': 858, 'length': 1}}]


    file = open('raw_data/nhis/2014/samadult.dat','r')
    # Get keys and make an empty dataframe

    columnList = []
    for var in varmap:
        columnList.append(list(var.keys())[0])


    dataValues = []
    for i in file.readlines():
        rowval = []
        for v in varmap:
            varKey = list(v.keys())[0]
            index = v[varKey]['index']
            length = v[varKey]['length']
            rowval.append(i[index-1:index-1+length])
        dataValues.append(rowval)

    valuesDF = pd.DataFrame(dataValues, columns=columnList)
    
    nhis2014updated = valuesDF
    nhis2014updated['Year'] = 2014

    

    frames = [nhis2014updated,nhis15updated,nhis16updated,nhis17updated,nhis18updated,nhis19updated]
    combined_nhis = pd.concat(frames)

    # End cleaning code
    combined_nhis.to_csv(outfile, index=False)


def clean_drug_utilization(input_path='raw_data/util/',
                           output_path='artifacts/', 
                           fileformat=r'drug_utilization_{}.csv'):

    """
    Open each file, clean, and ultimately merge into a single file.
    I had to add an intermediate step of saving each cleaned file as the process was being killed,
    likely due to low memory.
    """
    
    # if combined file exists, no need to run again
    combined_output_file = f'{output_path}{fileformat}'.format('cleaned')
    if os.path.exists(combined_output_file):
        return
    
    # Trying to determine column types during import is very memory intensive
    # Can reduce burden by specifying column types up front
    dtypes = {
        'utilization_type':'object',
        'state': 'object',
        'ndc': 'object', #'int64',
        'labeler_code': 'int64',
        'product_code': 'int64',
        'package_size': 'object', #'float64',
        'year': 'int64',
        'quarter': 'int64',
        'suppression_used': 'bool',
        'product_name': 'object',
        'units_reimbursed': 'float64',
        'number_of_prescriptions': 'float64',
        'total_amount_reimbursed': 'float64',
        'medicaid_amount_reimbursed': 'float64',
        'non_medicaid_amount_reimbursed': 'float64',
    }

    component_files = []
    output_temp_path = f'{output_path}temp/'
    # ensure output dir exists
    if not os.path.exists(output_temp_path):
        os.mkdir(output_temp_path)

    for year in YEARS:
        input_file = f'{input_path}{fileformat}'.format(year)
        single_output_file = f'{output_temp_path}{fileformat}'.format(f'{year}_cleaned')
        component_files.append(single_output_file)
        # have we already processed this file?
        if os.path.exists(single_output_file):
            continue

        print('cleaning: ', input_file)
        df = pd.read_csv(input_file, dtype=dtypes) 
        # eliminate rows where suppression is used.  This will reduce file size by 50%
        df = df[~df['suppression_used']]
        # remove whitespace from product name
        df['product_name'] = df['product_name'].str.strip()
        # remove dashes from ndc and package_size columns
        df['ndc'] = df['ndc'].str.replace('-','').str.strip()
        df['package_size'] = df['package_size'].str.replace('-','').str.strip()
        df = df.astype({'ndc':'int64', 'package_size':'int64'})

        print('saving: ', single_output_file)
        df.to_csv(single_output_file, index=False)
        # free up memory
        del(df)

    dtypes_proper = {
        'utilization_type':'object',
        'state': 'object',
        'ndc': 'int64',
        'labeler_code': 'int64',
        'product_code': 'int64',
        'package_size': 'int64',
        'year': 'int64',
        'quarter': 'int64',
        'suppression_used': 'bool',
        'product_name': 'object',
        'units_reimbursed': 'float64',
        'number_of_prescriptions': 'float64',
        'total_amount_reimbursed': 'float64',
        'medicaid_amount_reimbursed': 'float64',
        'non_medicaid_amount_reimbursed': 'float64',
    }

    dfs = []
    for file in component_files:
        print(f'reading {file} for merge')
        df = pd.read_csv(file, dtype=dtypes_proper) 
        dfs.append(df)


    print('concat')
    try:
        df_combined = pd.concat(dfs, ignore_index=True, axis=0)
    except Exception as e:
        print(f'caught {type(e)}: e')

    print('save')
    df_combined.to_csv(combined_output_file, index=False)
    del(df_combined)


def clean_nadac_pricing(input_path='raw_data/nadac/',
                           output_path='artifacts/', 
                           fileformat=r'nadac_pricing_{}.csv'):
    # ensure output dir exists
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # if combined file exists, no need to run again
    combined_output_file = f'{output_path}{fileformat}'.format('cleaned')
    if os.path.exists(combined_output_file):
        return
    
    df_combined = None
    for year in YEARS:
        input_file = f'{input_path}{fileformat}'.format(year)
        print('cleaning: ', input_file)
        df = pd.read_csv(input_file) 
        df_combined = df if df_combined is None else pd.concat([df_combined, df], ignore_index=True, axis=0)  

    print('saving combined: combined_output_file')
    df_combined.to_csv(combined_output_file, index=False)
    del(df_combined)


def clean_diabetes_products():
    # save to: artifacts/diabetes_products_cleaned.csv
    pass


def combine_all():
    fnames = [
        'diabetes_products_cleaned.csv', # this is what Zac will create
        'drug_utilization_cleaned.csv',
        'nadac_pricing_combined.csv',
        'nhis_cleaned.csv',
    ]
    # do merge

def process_clean(cleaning_option):
    if cleaning_option in ['util', 'all']:
        clean_drug_utilization()
    if cleaning_option in ['nhis', 'all']:
        clean_NHIS()
    if cleaning_option in ['nadac', 'all']:
        clean_nadac_pricing()
    if cleaning_option in ['diap', 'all']:
        clean_diabetes_products()
    if cleaning_option == 'all':
        combine_all()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # pass an arg using either "-co" or "--clean_option"
    parser.add_argument('-co', '--cleaning_option',
                        help='Which file to clean? [nhis|util|nadac|diap|all] Default is all',
                        default="all",
                        required=False)
    args = parser.parse_args()
    process_clean(args.cleaning_option)
