all: raw_data/insulin_pricing.csv

raw_data/insulin_pricing.csv:
	python get_data.py

