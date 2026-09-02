import requests
import os

def download_data(url ,filename):
    filepath = os.path.join("../../data/raw", filename)
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print("Data downloaded and saved successfully.")
    else:
        print("Failed to download data.")

filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv'

download_data(filepath,'medical_insurance_dataset.csv')