import os
import zipfile

# Specify the directory to zip and maximum zip file size in bytes
directory = r"E:\Projects\Deep-Learning-A-Z"
max_size = 90 * 1024 * 1024  # 90 MB in bytes

# Define the output directory where zip files will be saved
output_dir = r"E:\Projects\Created-Zip"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Initialize variables
current_zip_size = 0
zip_index = 1
zip_file = None


def start_new_zip():
    """Start a new zip file."""
    global zip_index, current_zip_size, zip_file
    zip_file_path = os.path.join(output_dir, f"Deep_Learning_AZ_Part_{zip_index}.zip")
    zip_file = zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED)
    print(f"Created new zip file: {zip_file_path}")
    zip_index += 1
    current_zip_size = 0
    return zip_file_path


# Start the first zip file
current_zip_path = start_new_zip()

# Iterate through all files in the directory
for root, _, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)

        # Check if adding this file would exceed max size, if so start a new zip
        if current_zip_size + file_size > max_size:
            zip_file.close()
            print(
                f"Zipped file saved at: {current_zip_path}"
            )  # Print the path of the completed zip file
            current_zip_path = start_new_zip()

        # Add the file to the current zip and update the size
        zip_file.write(file_path, os.path.relpath(file_path, directory))
        current_zip_size += file_size
        print(
            f"Added {file_path} to zip, current zip size: {current_zip_size / (1024 * 1024):.2f} MB"
        )

# Close the last zip file and print its path
zip_file.close()
print(f"Zipped file saved at: {current_zip_path}")
print("Zipping complete.")
