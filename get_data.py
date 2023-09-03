import pandas as pd
import requests
from bs4 import BeautifulSoup
import os


def download_pricing(outfile='raw_data/insulin_pricing.csv'):
    # doesn't really do anything yet
    df = pd.DataFrame()
    df.to_csv(outfile)


def download_drug_utiliztion(outfile='raw_data/drug_utilization_2021.csv'):
    # don't download if this already exists
    if os.path.exists(outfile):
        return
    # get file
    url = 'https://data.medicaid.gov/api/1/datastore/query/eec7fbe6-c4c4-5915-b3d0-be5828ef4e9d/0/download'
    params = {'format': 'csv'}
    response = requests.get(url, params=params)
    with open(outfile, mode="wb") as file:
        file.write(response.content)


def download_all():
    download_drug_utiliztion()
    # download_pricing()


if __name__ == '__main__':
    download_all()
