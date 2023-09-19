import pandas as pd
import os

YEARS = [2014, 2015, 2016, 2017, 2018, 2019]

def clean_NHIS(path='raw_data/nhis/adult19.csv',
               outfile='artifacts/adult19_cleaned.csv'):
    if os.path.exists(outfile):
        return
    print('cleaning: ', path)
    df = pd.read_csv(path)
    # Cleaning code here
    # End cleaning code
    df.to_csv(outfile, index=False)


"""
Open each file, clean, and ultimately merge into a single file.
I had to add an intermediate step of saving each cleaned file as the process was being killed,
likely due to low memory.
"""
def combine_and_clean_drug_utilization(input_path='raw_data/util/',
                                       output_path='artifacts/util/', 
                           fileformat=r'drug_utilization_{}.csv'):

    # ensure output dir exists
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    # if combined file exists, no need to run again
    combined_output_file = f'{output_path}{fileformat}'.format('combined')
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

    outformat = f'{output_path}{fileformat}'.format('{}_cleaned')
    component_files = []
    print(outformat)
    for year in YEARS:
        input_file = f'{input_path}{fileformat}'.format(year)
        single_output_file = f'{output_path}{fileformat}'.format(f'{year}_cleaned')
        component_files.append(single_output_file)
        # have we already processed this file?
        if os.path.exists(single_output_file):
            return

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

#        dfs.append(df)

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
    df_combined = pd.concat(dfs, ignore_index=True, axis=0)
    print('save')
    df_combined.to_csv(combined_output_file, index=False)
    del(df_combined)



def clean_nadac_pricing(path='raw_data/nadac/nadac_pricing_2019.csv',
                       outfile='artifacts/nadac_pricing_2019_cleaned.csv'):
    if os.path.exists(outfile):
        return
    print('cleaning: ', path)
    df = pd.read_csv(path)
    # Cleaning code here
    # End cleaning code
    df.to_csv(outfile, index=False)


def process_clean(cleaning_option):
    if cleaning_option in ['util', 'all']:
        combine_and_clean_drug_utilization()
    if cleaning_option in ['nhis', 'all']:
        clean_NHIS()
    if cleaning_option in ['nadac', 'all']:
        clean_nadac_pricing()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # pass an arg using either "-co" or "--clean_option"
    parser.add_argument('-co', '--cleaning_option',
                        help='Which file to clean? [nhis|util|nadac|all] Default is all',
                        default="all",
                        required=False)
    args = parser.parse_args()
    process_clean(args.cleaning_option)
