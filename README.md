# Generic Real Estate Consulting Project

## Overview
This project aims to provide insights and analysis for the real estate market using data scraping, preprocessing, machine learning, and visualization techniques. The repository is structured to facilitate data collection, processing, modelling, and analysis through various scripts and notebooks.

## Directory Structure

- **/summary**: Contains raw, curated, and landing data.
- **data/**: Contains raw, curated, and landing data.
  - **curated/**: Processed and cleaned data.
  - **landing/**: Raw data collected from various sources.
  - **raw/**: uncleaned data.
- **meetings/**: Documentation of meeting notes and planning.
- **notebooks/**: Jupyter notebooks for data scraping, preprocessing, modelling, and analysis.
  - **1.\<num\>\_scrape_\<name\>.ipynb**: Scraping of property datasets (from oldlistings).
  - **2.\<num\>\_preprocessing_\<name\>.ipynb**: Combining buy and sell data.
  - **3.\<num\>\_\<name\>.ipynb**: feature engineering containing proximity calculation using locally installed ORS server
  - **4.\<num\>\_model_\<name\>.ipynb**: modelling on curated data. Compute Predictions, and analysis of results.
  - **5.\<num\>\_visualization_\<name\>.ipynb**: Geosptial and some other visualization
  - **6.1_liveability_main.ipynb**: liveability and affordability ranking calculations.
  
  
- **plots/**: Placeholder for generated plots and visualizations.
- **scripts/**:. Contains scripts for data scraping and other utilities.
  - **scrape.py**: Script to start scraping data.
- **SummaryNotebookRelated/**: Placeholder for summary notebooks and related files.

## Getting Started
1. **Clone the repository**:
    ```sh
    git clone https://github.com/MAST30034-AppliedDataScience/project-2-group-real-estate-industry-project-2.git
    cd project-2-group-real-estate-industry-project-2
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```


## Usage
- **Data Scraping**: Run all notebooks labelled [notebooks/1.\*\_scrape_*.ipynb](notebooks/) to collect data.
Note: this requires api keys to run.
- **Data Preprocessing**: Refer to the notebooks in the [notebooks/2.*_preprocessing\_\*.ipynb](notebooks/) directory for data preprocessing steps.
- **Analysis and Visualization**: Use the notebooks and scripts to analyze and visualize the data.


## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please open an issue or contact the project maintainers.