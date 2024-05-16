# Programming for Data Science Project

## Introduction
This project is part of the Programming for Data Science course at the University of Bern in spring semester 2024.

## Project Description
This project aims to develop a comprehensive reporting tool for analyzing Fitbit data. 
The tool is designed to merge data from multiple CSV files containing Fitbit data for 30 users into a single DataFrame. 
This DataFrame allows users to access health parameters such as sleep, steps, and calories burned at 
different temporal resolutions (minute, hour, or day).

Users can interact with the tool to select specific subjects and time periods of interest, 
enabling them to generate summary statistics for health measures based on their criteria. 
Furthermore, the tool provides visualizations of health measures over time, 
facilitating comparisons between subjects and time periods. 
Users can adjust the resolution of data displayed in visualizations according to their preferences.

Key considerations include data cleaning to handle missing values and outliers, 
designing an intuitive user interface for ease of interaction, and providing comprehensive documentation for user guidance. 
The tool prioritizes scalability to accommodate large datasets and potential future expansions.


## Setup
### Python
To run this project you need to have installed python on your machine. 
You can download python from the [official website](https://www.python.org/downloads/).
As alternative, you can also install conda from by following the instructions on the [official website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Dependencies
You can create a virtual environment with conda (or alternatively with pip) and install the required packages 
by running the following commands on the command line. You need to do only one of the following options.

Conda:
```bash
conda create --name <<YourEnvName>>
conda activate <<YourEnvName>>
```

Pip:
```bash
pip install -r requirements.txt
```

If you add a new package to the project, please update also the requirements.txt file manually.

## Data
The data used in this project originate from [kaggle](https://www.kaggle.com/datasets/supriya3024/fitbit-fitness-tracker). The dataset is also contained
in the data folder of this project. The data is stored in multiple csv files.

### Preprocessing
To preprocess the data please run the file `src\MergeMinutes.py`. This will take some time (~2min), 
as it merges all the data into one file. Afterward you will find a `minutes.csv` in the `preprocessed_data` folder.
```bash
python src/MergeMinutes.py
```

## Usage
This project contains a dashboard which visualize the preprocessed data. 
To run the dashboard, please run the file `src\dashboard.py` and then open `http://127.0.0.1:8050/` 
(or any other url which is shown in the console) in your browser. Now you can interact with the dashboard by 
selecting different subjects, chart types, time ranges and resolutions.

```bash
python src/dashboard.py
```

## Further Information
There are other modules in the `src` folder which can be used to analyze the data. 

The `data_cleaning.py` file contains logic to handle missing data. 
But this is currently not used in the data process and can be ignored.

The `SummaryStatistics.py` file contains logic to calculate summary statistics. This is currently not used 
in since many views can already be configured in the dashboard and we did not yet add more statistic features.

The `DataSelection.py` file contains logic to select data based on user input over the command line. 
This is currently not used in the dashboard but can be used as standalone solution.