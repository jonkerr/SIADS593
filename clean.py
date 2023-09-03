import pandas as pd


def clean_drug_utiliztion(path='raw_data/drug_utilization_2021.csv',
                          outfile='artifacts/drug_utilization_2021_cleaned.csv'):
    # import
    df = pd.read_csv(path)

    # remove whitespace from product name
    df['product_name'] = df['product_name'].str.strip()

    # write
    df.to_csv(outfile)


def clean_all():
    clean_drug_utiliztion()


if __name__ == '__main__':
    clean_all()
