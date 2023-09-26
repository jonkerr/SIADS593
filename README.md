# SIADS593
Data processing for Milestone 1

## Overview
Explore the relationships of varied insulin prices in different regions and on diabetes patient outcomes in the same regions.

## Getting set up
Once you've cloned the repo, the following steps are recommended.
1. Create a virtual environment
```
python -m venv .venv
```

1a. Every time you want to use this venv, be sure to activate
```
source .venv/bin/activate 
```

2. Install all required dependencies
```
pip install -r requirements.txt
```

3. Install a kernel that can be used with Jupyter notebooks
```
python -m ipykernel install --user --name=mads-milestone1-team-08
```


## Data Pipeline Overview
To download and clean all data, issue the following commands
```
make cleanall all
```

To refresh the artifacts
```
make clean all
```


## Naming conventions
All notebooks for EDA will be prefixed "EDA_" so their purpose is clear.  For deeper analysis notebooks, the prefix is still to be determined.