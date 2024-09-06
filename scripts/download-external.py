import os
from urllib.request import urlretrieve
import time
import zipfile
from utils import create_dir, get_runtime

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
def unzip(file_dir_path: str, extract_dir, file_name: str) -> None:
    """Unzips the file_name in the file_dir_path to extract_dir.
    """
    # Check if the extracted directory already exists
    if not os.path.exists(f'{file_dir_path}/{extract_dir}'):
        with zipfile.ZipFile(f'{file_dir_path}/{file_name}', 'r') as zip_ref:
            zip_ref.extractall(f'{file_dir_path}/{extract_dir}')

        # Remove the zip file after extraction
        os.remove(f'{file_dir_path}/{file_name}')
        print(f"Extracted {file_name} to {file_dir_path}/{extract_dir}\n")
    else:
        print(f"Directory {file_dir_path}/{file_name} already extracted"\
              f"at {file_dir_path}/{file_name}.\n")
        os.remove(f'{file_dir_path}/{file_name}')
    return


def main():
    start_time = time.time()

    create_dir('./data/landing/population/')
    create_dir('./data/landing/income/')

    ######### ABS Population Data by SA2 2001-2023
    download_external_data(
        "https://www.abs.gov.au/statistics/people/population/regional-population/2022-23/32180DS0003_2001-23.xlsx",
        'population/population.xlsx'
    )

    ######### ABS SA2 Digital Boundary data as of 2021
    download_external_data(
        "https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip",
        'SA2.zip'
    )
    unzip("./data/landing", "SA2-shapefile", "SA2.zip")

    ########################################   school locations  ########################################
    download_external_data(
        "https://www.education.vic.gov.au/Documents/about/research/datavic/dv371_DataVic_School_Zones_2024.zip",
        'school_zones.zip'
    )
    unzip("./data/landing", "school-zones", "school_zones.zip")

    ######### Public Transport Victoria (PTV) GTFS data
    # TODO: PAUL - Please try and download the PTV data and extract it. Looks like we can get google tranzit data from here
    # ptv_url = "http://data.ptv.vic.gov.au/downloads/gtfs.zip"
    # download_file(ptv_url, '../data/raw/gtfs.zip')
    # create_directory("../data/raw/ptv")
    # extract_zip("../data/raw/gtfs.zip", "../data/raw/ptv")
    # # Extract nested zip files in the PTV directory
    # for i in range(2, 5):
    #     nested_zip_path = f"../data/raw/ptv/{i}/google_transit.zip"
    #     extract_zip(nested_zip_path, f"../data/raw/ptv/{i}")

    #######################################   income locations  ########################################
    # TODO: Confirm usecase for income location data
    download_external_data(
        "https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&14100do0004_2014-19.xlsx&1410.0&Data%20Cubes&63757E101C2DA1A1CA2586290010B831&0&2014-19&24.11.2020&Latest",
        'income/income.xlsx'
    )

    print(get_runtime(start_time))

if __name__ == '__main__':
    main()
