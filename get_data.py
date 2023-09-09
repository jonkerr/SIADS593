import pandas as pd
import requests
import os
# from bs4 import BeautifulSoup

# stuff for processing zip file
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


def download_pricing(outfile='raw_data/insulin_pricing.csv'):
    # doesn't really do anything yet
    df = pd.DataFrame()
    df.to_csv(outfile)


def download_drug_utiliztion(outfile='raw_data/drug_utilization_2019.csv'):
    # don't download if this already exists
    if os.path.exists(outfile):
        return
    # get file
    print('downloading ', outfile)
    #url = 'https://data.medicaid.gov/api/1/datastore/query/eec7fbe6-c4c4-5915-b3d0-be5828ef4e9d/0/download'
    url = 'https://data.medicaid.gov/api/1/datastore/query/daba7980-e219-5996-9bec-90358fd156f1/0/download'    
    params = {'format': 'csv'}
    response = requests.get(url, params=params)
    with open(outfile, mode="wb") as file:
        file.write(response.content)


def download_NHIS(outpath='raw_data/'):
    # don't download if this already exists
    if os.path.exists(outpath + "adult19.csv"):
        return
    print('downloading ', outpath + "adult19.csv")

    # cool unzipping approach found at:
    # https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/
    zipurl = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2019/adult19csv.zip"
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(outpath)


def process_downloads(download_option):
    if download_option in ['nhis', 'all']:
        download_NHIS()
    if download_option in ['util', 'all']:
        download_drug_utiliztion()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # pass an arg using either "-do" or "--download_option"
    parser.add_argument('-do', '--download_option',
                        help='Which file to download? [nhis|util|all] Default is all',
                        default="all",
                        required=False)
    args = parser.parse_args()
    process_downloads(args.download_option)
