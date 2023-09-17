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
def download_diabetes_ndc_codes(outfile='raw_data/NDC11_Diabetes_Drug.xlsx'):
    if os.path.exists(outfile):
        return
    print('download NDC codes')
    url = 'https://figshare.com/ndownloader/files/20202789'
    response = requests.get(url)
    with open(outfile, mode="wb") as file:
        file.write(response.content)


def download_NHIS(outpath='raw_data/nhis/'):
    zipurl = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2019/adult19csv.zip"
    download_zip(zipurl, outpath + '2019/', "adult19.csv")
    zipurl ='https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2018/samadultcsv.zip'
    download_zip(zipurl, outpath + '2018/', "samadult.csv")
    zipurl = 'https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2017/samadultcsv.zip'
    download_zip(zipurl, outpath + '2017/', "samadult.csv")
    zipurl = 'https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2016/samadultcsv.zip'
    download_zip(zipurl, outpath + '2016/', "samadult.csv")
    zipurl = 'https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2015/samadult.zip'
    download_zip(zipurl, outpath + '2015/', "samadult.csv")
    zipurl = 'https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2014/samadult.zip'
    download_zip(zipurl, outpath + '2014/', "samadult.dat")
    

def bulk_download_medicaid(year_ids, outpath, outfile):
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    for year in year_ids.keys():
        dataset_id = year_ids[year]
        download_from_medicaid(dataset_id, outpath+outfile.format(year))


def download_drug_utiliztion(outpath='raw_data/util/', outfile=r'drug_utilization_{}.csv'):
    year_ids = {
        2014: 'a9cfe5e9-d7d8-5b87-a7db-b45a7daf84fc',
        2015: '2fed5758-5fd6-5dbb-8f92-34b3a0c3c8dd',
        2016: '53cf9f05-97e3-5bd6-a237-bc971e3642d9',
        2017: '776a3880-a62d-5990-8b40-4406e6861dbb',
        2018: 'a1f3598e-fc71-51aa-8560-78e7e1a61b09',
        2019: 'daba7980-e219-5996-9bec-90358fd156f1'
    }
    bulk_download_medicaid(year_ids, outpath, outfile)


def download_nadac_pricing(outpath='raw_data/nadac/', outfile=r'nadac_pricing_{}.csv'):
    year_ids = {
        2014: 'ba0c3734-8012-549a-8f50-2ff389d0e0ef',
        2015: '4d7af295-2132-55a8-b40c-d6630061f3e8',
        2016: '7656fc17-f1b4-566b-9a2d-c4a4f2ac7ae1',
        2017: '1c5d0fc9-693a-534a-8240-4627d9362b0d',
        2018: '8de1b213-73c5-552b-b84e-ac795f34d056',
        2019: '76a1984a-6d69-5e4d-86c8-65eb31f0506d'
    }
    bulk_download_medicaid(year_ids, outpath, outfile)


"""
Select targets for download
"""


def process_download_target(download_option):
    if download_option in ['nhis', 'all']:
        download_NHIS()
    if download_option in ['util', 'all']:
        download_drug_utiliztion()
    if download_option in ['nadac', 'all']:
        download_nadac_pricing()
    if download_option in ['ndc', 'all']:
        download_diabetes_ndc_codes()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    # pass an arg using either "-do" or "--download_option"
    parser.add_argument('-do', '--download_option',
                        help='Which file to download? [nhis|util|nadac|ndc|all] Default is all',
                        default="all",
                        required=False)
    args = parser.parse_args()
    process_download_target(args.download_option)
