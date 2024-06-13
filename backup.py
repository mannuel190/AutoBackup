import os  # Module for interacting with the operating system
import shutil  # Module for high-level file operations
import schedule  # Module for scheduling tasks
import datetime  # Module for working with dates and times
import time  # Module for time-related functions

# Define the source and destination directories and backup time.
source_dir = "E:/Projects/soucelol"
destination_dir = "E:/Projects/destinationlol"
backup_time = "00:16"

# Function to copy the folder to the destination directory with a timestamp
def copy_folder_to_directory(source, dest):
    # Get the name of the source folder
    folder_name = os.path.basename(source)
    # Get the current date and time formatted as 'YYYY-MM-DD_HH-MM-SS'
    today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Create the destination directory path with the source folder name and timestamp
    dest_dir = os.path.join(dest, f"{folder_name}_{today}")

    try:
        # Copy the entire source directory to the destination directory
        shutil.copytree(source, dest_dir)
        print(f"Folder has been backed up successfully to: {dest_dir}")
    except FileExistsError:
        # Handle the case where the destination directory already exists
        print(f"Folder already exists in : {dest}")

# Schedule the backup to run every day at 11:38 PM
schedule.every().day.at(backup_time).do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Print a message indicating the backup schedule has been set
print("Backup schedule set. Waiting for the scheduled time...")

# Infinite loop to keep the script running and checking the schedule
while True:
    # Run any pending scheduled tasks
    schedule.run_pending()
    # Sleep for 60 seconds before checking again
    time.sleep(60)
