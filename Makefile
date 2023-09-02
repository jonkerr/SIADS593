all: raw_data/insulin_pricing.csv

raw_data/insulin_pricing.csv:
	python get_data.py

# clean the generated artificats
clean:
	rm artifacts/*.csv

# if for some reason we want to also clean the downloaded/source data, we can use the cleanraw target
# generally not recommended as these files are huge and we shouldn't plan on editing the source
cleanraw:
	rm raw_data/*.csv

# remove all data
cleanall: cleanraw clean
