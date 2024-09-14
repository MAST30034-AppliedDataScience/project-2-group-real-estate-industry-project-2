import os
from urllib.request import urlretrieve
import time
from utils import create_dir, get_runtime, unzip

################################################################################
def download_external_data(url: str, file_name: str) -> None:
    """Downloads external data from the given url and file_name.
    """
    output_path = f"./data/landing/{file_name}"
    if not os.path.exists(output_path):
        print(f"Begin     {file_name}")
        urlretrieve(url, output_path)
        print(f"Completed {file_name}\n")
    else:
        print(f"File {output_path} already exists.\n")
    return

################################################################################
def main():
    start_time = time.time()

    create_dir('./data/landing/population/')
    create_dir('./data/landing/income/')
    create_dir('./data/landing/sa2/')

    #### ABS Population Data by SA2 2001-2023
    download_external_data(
        "https://www.abs.gov.au/statistics/people/population/regional-"\
            f"population/2022-23/32180DS0003_2001-23.xlsx",
        'population/population.xlsx'
    )

    #### ABS SA2 Data
    # Digital Boundary 2021-2026
    download_external_data(
        "https://www.abs.gov.au/statistics/standards/australian-statistical-"\
            f"geography-standard-asgs-edition-3/jul2021-jun2026/access-and-"\
            f"downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip",
        'sa2/sa2-shp.zip'
    )
    unzip("./data/landing/sa2", "sa2-21-shp", "sa2-shp.zip")


    #### school zone locations 
    download_external_data(
        f"https://www.education.vic.gov.au/Documents/about/research/datavic/"\
            f"dv371_DataVic_School_Zones_2024.zip",
        'school_zones.zip'
    )
    unzip("./data/landing", "school-zones", "school_zones.zip")

    #### Public Transport Victoria (PTV) GTFS data
    download_external_data(
        "https://data.ptv.vic.gov.au/downloads/gtfs.zip", 
        'gtfs.zip'
    )
    unzip("./data/landing", "ptv", "gtfs.zip")
    # Extract nested zip files in the PTV directory
    for i in range(1, 12):
        if i == 9:
            continue
        unzip(f"./data/landing/ptv/{i}", f'{i}', "google_transit.zip")

    #### Income data
    # 2012-2016
    download_external_data(
        f"https://www.abs.gov.au/statistics/labour/earnings-and-working-"\
            f"conditions/personal-income-australia/2011-12-2017-18/6524055002_"\
            f"DO001.xls",
        'income/income-2012-2016.xls'
    )
    # 2017-2021
    download_external_data(
        f"https://www.abs.gov.au/statistics/labour/earnings-and-working-"\
            f"conditions/personal-income-australia/2020-21-financial-year/"\
            f"Table%201%20-%20Total%20income%2C%20earners%20and%20summary%20"
            f"statistics%20by%20geography%2C%202016-17%20to%202020-21.xlsx",
        'income/income-2017-2021.xlsx'
    )

    print(get_runtime(start_time))

if __name__ == '__main__':
    main()
