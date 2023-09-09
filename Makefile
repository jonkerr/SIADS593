all: artifacts/drug_utilization_2019_cleaned.csv

# acquire raw data
raw_data/drug_utilization_2019.csv:
	python get_data.py

# clean data file
artifacts/drug_utilization_2019_cleaned.csv: raw_data/drug_utilization_2019.csv
	python clean.py

# remove the generated artifacts from the filesystem
clean:
	rm artifacts/*.csv

# if for some reason we want to also clean the downloaded/source data, we can use the cleanraw target
# generally not recommended as these files are huge and we shouldn't plan on editing the source
cleanraw:
	rm raw_data/*.csv

# remove all data
cleanall: cleanraw clean
