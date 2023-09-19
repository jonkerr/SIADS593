import pandas as pd
import os


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

    frames = [nhis15updated,nhis16updated,nhis17updated,nhis18updated,nhis19updated]
    combined_nhis = pd.concat(frames)

    # End cleaning code
    combined_nhis.to_csv(outfile, index=False)


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
