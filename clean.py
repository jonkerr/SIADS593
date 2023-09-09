import pandas as pd


def clean_NHIS():
    pass


def clean_drug_utiliztion(path='raw_data/drug_utilization_2019.csv',
                          outfile='artifacts/drug_utilization_2019_cleaned.csv'):
    # import
    df = pd.read_csv(path)

    # remove whitespace from product name
    df['product_name'] = df['product_name'].str.strip()
    # eliminate rows where suppression is used
    df = df[~df['suppression_used']]

    # write
    df.to_csv(outfile)


def process_clean(cleaning_option):
    if cleaning_option in ['nhis', 'all']:
        clean_NHIS()
    if cleaning_option in ['util', 'all']:
        clean_drug_utiliztion()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # pass an arg using either "-co" or "--clean_option"
    parser.add_argument('-co', '--cleaning_option',
                        help='Which file to clean? [nhis|util|all] Default is all',
                        default="all",
                        required=False)
    args = parser.parse_args()
    process_clean(args.cleaning_option)
