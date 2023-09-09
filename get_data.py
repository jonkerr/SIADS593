import pandas as pd
import requests
import os
from bs4 import BeautifulSoup

# stuff for processing zip file
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

"""
download_from_medicaid() and download_zip() are generalized methods for downloading information.
"""


def download_from_medicaid(dataset_id, outfile):
    # don't download if this already exists
    if os.path.exists(outfile):
        return
    # get file
    print('downloading ', outfile)
    url = f'https://data.medicaid.gov/api/1/datastore/query/{dataset_id}/0/download'
    params = {'format': 'csv'}
    response = requests.get(url, params=params)
    with open(outfile, mode="wb") as file:
        file.write(response.content)


def download_zip(zipurl, outpath, filename):
    # don't download if this already exists
    if os.path.exists(outpath + filename):
        return
    print('downloading ', outpath + filename)
    # cool unzipping approach found at:
    # https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(outpath)


"""
The following methods are for acquiring specific data sets
"""


def download_NHIS(outpath='raw_data/'):
    zipurl = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2019/adult19csv.zip"
    download_zip(zipurl, outpath, "adult19.csv")


def download_drug_utiliztion(outfile='raw_data/drug_utilization_2019.csv'):
    dataset_id = 'daba7980-e219-5996-9bec-90358fd156f1'
    download_from_medicaid(dataset_id, outfile)


def download_ndac_pricing(outfile='raw_data/ndac_pricing_2019.csv'):
    dataset_id = '76a1984a-6d69-5e4d-86c8-65eb31f0506d'
    download_from_medicaid(dataset_id, outfile)


"""
Select targets for download
"""


def process_download_target(download_option):
    if download_option in ['nhis', 'all']:
        download_NHIS()
    if download_option in ['util', 'all']:
        download_drug_utiliztion()
    if download_option in ['ndac', 'all']:
        download_ndac_pricing()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # pass an arg using either "-do" or "--download_option"
    parser.add_argument('-do', '--download_option',
                        help='Which file to download? [nhis|util|ndac|all] Default is all',
                        default="all",
                        required=False)
    args = parser.parse_args()
    process_download_target(args.download_option)
