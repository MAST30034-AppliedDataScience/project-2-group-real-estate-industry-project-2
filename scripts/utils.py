import matplotlib.pyplot as plt
import time
import os


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