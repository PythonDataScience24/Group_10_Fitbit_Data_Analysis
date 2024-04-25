# Programming for Data Science Project

## Introduction
This project is part of the Programming for Data Science course at the University of Bern in spring semester 2024.

## Project Description
This project aims to develop a comprehensive reporting tool for analyzing Fitbit data. The tool is designed to merge data from multiple CSV files containing Fitbit data for 30 users into a single DataFrame. This DataFrame allows users to access health parameters such as sleep, steps, and calories burned at different temporal resolutions (minute, hour, or day).

Users can interact with the tool to select specific subjects and time periods of interest, enabling them to generate summary statistics for health measures based on their criteria. Furthermore, the tool provides visualizations of health measures over time, facilitating comparisons between subjects and time periods. Users can adjust the resolution of data displayed in visualizations according to their preferences.

Key considerations include data cleaning to handle missing values and outliers, designing an intuitive user interface for ease of interaction, and providing comprehensive documentation for user guidance. The tool prioritizes scalability to accommodate large datasets and potential future expansions.


## Setup
You can create a virtual environment with conda (or alternatively with pip) and install the required packages 
by running the following commands on the command line:
```bash
conda create --name <<YourEnvName>>
conda activate <<YourEnvName>>

pip install -r requirements.txt
```

If you add a new package to the project, please update also the requirements.txt file manually.
