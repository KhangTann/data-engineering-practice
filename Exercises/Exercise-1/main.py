import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    os.makedirs("downloads", exist_ok=True)

    for url in download_uris:
        filename = url.split("/")[-1]
        zip_path = os.path.join("downloads", filename)

        try:
            print(f"Downloading {filename}...")
            response = requests.get(url)

            if response.status_code == 200:
                with open(zip_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")

                # Giải nén và giữ lại chỉ file .csv
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        extracted_files = zip_ref.namelist()
                        zip_ref.extractall("downloads")
                        print(f"Extracted: {filename}")

                        # Xóa tất cả file không phải .csv
                        for file in extracted_files:
                            extracted_path = os.path.join("downloads", file)
                            if not file.endswith('.csv'):
                                if os.path.isfile(extracted_path):
                                    os.remove(extracted_path)
                                    print(f"Removed non-csv file: {file}")
                    # Xóa file zip sau khi giải nén
                    os.remove(zip_path)
                    print(f"Deleted zip: {filename}")

                except zipfile.BadZipFile:
                    print(f" Invalid zip file: {filename}")
                    os.remove(zip_path)

            else:
                print(f"Failed to download {filename} - Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    main()
