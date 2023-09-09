import pandas as pd
import os


def clean_NHIS(path='raw_data/nhis/adult19.csv',
               outfile='artifacts/adult19_cleaned.csv'):
    if os.path.exists(outfile):
        return
    print('cleaning: ', path)
    df = pd.read_csv(path)
    # Cleaning code here
    # End cleaning code
    df.to_csv(outfile, index=False)


def clean_drug_utilization(path='raw_data/util/drug_utilization_2019.csv',
                           outfile='artifacts/drug_utilization_2019_cleaned.csv'):
    if os.path.exists(outfile):
        return
    print('cleaning: ', path)
    df = pd.read_csv(path)
    # eliminate rows where suppression is used
    df = df[~df['suppression_used']]
    # remove whitespace from product name
    df['product_name'] = df['product_name'].str.strip()
    df.to_csv(outfile, index=False)


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
        clean_drug_utilization()
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
