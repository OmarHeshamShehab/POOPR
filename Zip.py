import os
import zipfile


def zip_folder(input_folder, output_folder, max_size_mb):
    max_size_bytes = max_size_mb * 1024 * 1024
    zip_counter = 1
    current_zip_size = 0
    zip_file = zipfile.ZipFile(
        f"{output_folder}/folder_part_{zip_counter}.zip", "w", zipfile.ZIP_DEFLATED
    )

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            # If adding this file would exceed the max size, close current zip and start a new one
            if current_zip_size + file_size > max_size_bytes:
                zip_file.close()
                zip_counter += 1
                current_zip_size = 0
                zip_file = zipfile.ZipFile(
                    f"{output_folder}/folder_part_{zip_counter}.zip",
                    "w",
                    zipfile.ZIP_DEFLATED,
                )

            # Add the file to the current zip and update the current zip size
            zip_file.write(file_path, arcname=file)
            current_zip_size += file_size

    zip_file.close()


# Updated input path with raw string notation
input_folder = r"C:\Users\omarh\Downloads\Deep-Learning-A-Z"
output_folder = r"C:\Users\omarh\Downloads\ZippedParts"
max_size_mb = 90

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

zip_folder(input_folder, output_folder, max_size_mb)
