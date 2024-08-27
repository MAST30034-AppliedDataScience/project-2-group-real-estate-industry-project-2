import os
import requests
import zipfile

def download_file(url, output_path):
    """Downloads a file from the given URL to the specified output path."""
    resp = requests.get(url)
    with open(output_path, 'wb') as output:
        output.write(resp.content)

def extract_zip(zip_path, extract_to):
    """Extracts a zip file to the specified directory and deletes the zip file."""
    with zipfile.ZipFile(zip_path, mode="r") as archive:
        archive.extractall(extract_to)
    os.remove(zip_path)

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

######### ABS Population Data by SA2 2001-2023
population_url = "https://www.abs.gov.au/statistics/people/population/regional-population/2022-23/32180DS0003_2001-23.xlsx"
download_file(population_url, '../data/raw/population.xlsx')

######### ABS SA2 Digital Boundary data as of 2021
sa2_url = "https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip"
download_file(sa2_url, '../data/raw/SA2.zip')
create_directory("../data/raw/SA2")
extract_zip("../data/raw/SA2.zip", "../data/raw/SA2")

######### Public Transport Victoria (PTV) GTFS data
# TODO: Confirm which PTV datasets are needed
# ptv_url = "http://data.ptv.vic.gov.au/downloads/gtfs.zip"
# download_file(ptv_url, '../data/raw/gtfs.zip')
# create_directory("../data/raw/ptv")
# extract_zip("../data/raw/gtfs.zip", "../data/raw/ptv")
# # Extract nested zip files in the PTV directory
# for i in range(2, 5):
#     nested_zip_path = f"../data/raw/ptv/{i}/google_transit.zip"
#     extract_zip(nested_zip_path, f"../data/raw/ptv/{i}")

########################################   school locations  ########################################
school_url = "https://www.education.vic.gov.au/Documents/about/research/datavic/dv371_DataVic_School_Zones_2024.zip"
download_file(school_url, '../data/raw/school_zones.zip')
create_directory("../data/raw/school_zones")
extract_zip("../data/raw/school_zones.zip", "../data/raw/school_zones")

########################################   hospital locations  ########################################
# TODO: Confirm usecase for hospital data
# hospital_url = "https://data.humdata.org/dataset/a5221b34-8ed4-4e19-88c9-b195c13502b6/resource/6df0921e-d676-4c36-8229-c65cea510217/download/australia.csv"
# download_file(hospital_url, '../data/raw/hospital2021.csv')

########################################   income locations  ########################################
# TODO: Confirm usecase for income location data
# income_url = "https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&14100do0004_2014-19.xlsx&1410.0&Data%20Cubes&63757E101C2DA1A1CA2586290010B831&0&2014-19&24.11.2020&Latest"
# download_file(income_url, '../data/raw/income.xlsx')
