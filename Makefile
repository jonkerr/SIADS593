all: artifacts/diabetes_meds_prices.csv

# acquire raw data
raw_data/util/drug_utilization_2019.csv:
	python get_data.py

# clean data file
artifacts/diabetes_meds_prices.csv: raw_data/util/drug_utilization_2019.csv
	python clean.py

# remove the generated artifacts from the filesystem
clean:
	rm artifacts/*.csv
	rm -fr artifacts/temp

# if for some reason we want to also clean the downloaded/source data, we can use the cleanraw target
# generally not recommended as these files are huge and we shouldn't plan on editing the source
cleanraw:
	rm -fr raw_data/fda_NDC_all
	rm -fr raw_data/nadac
	rm -fr raw_data/nhis
	rm -fr raw_data/util

# remove all data
cleanall: cleanraw clean
