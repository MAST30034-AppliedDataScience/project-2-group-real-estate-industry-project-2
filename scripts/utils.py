import matplotlib.pyplot as plt
import time
import os
import zipfile
import pandas as pd

################################################################################
def create_dir(relative_path: str) -> None:
    """Creates a directory from a given relative path if it doesn't exist.
    """
    if not os.path.exists(relative_path):
        os.makedirs(relative_path)
        print('Created directory:', relative_path)
    else:
        print('Directory already exists:', relative_path)
    print()

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

################################################################################
def get_runtime(start_time: float) -> str:
    """Calculates and returns the runtime from the given start time.
    """
    total_runtime_seconds = time.time() - start_time
    minutes = int(total_runtime_seconds // 60)
    seconds = int(total_runtime_seconds % 60)
    return f'Runtime: {minutes} minutes and {seconds} seconds'

################################################################################
def save_plot(plt: plt, file_name: str):
    """Saves a matplotlib plot with a given file_name.
    Parameters:
    - plt: The matplotlib plot object.
    - file_name (str): The name of the file to save the plot as.
    """
    plt.savefig(f"../plots/{file_name}.png", dpi=300, bbox_inches='tight')
