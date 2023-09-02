import pandas as pd
from bs4 import BeautifulSoup

def download_pricing(outfile='raw_data/insulin_pricing.csv'):
    # doesn't really do anything yet
    df = pd.DataFrame()
    df.to_csv(outfile)


if __name__ == '__main__':
    download_pricing()
