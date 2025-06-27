"""
Script to download the metabolomics dataset ST000915 from the Metabolomics Workbench.
This script fetches the ZIP archive for study ST000915 from the official download link 
and saves it locally as 'ST000915.zip'.

Source: https://www.metabolomicsworkbench.org/

Author: Tomasz Lasota
Version: 1.0
Date: 2025-06-27
"""


import requests

url = "https://www.metabolomicsworkbench.org/studydownload/ST000915.zip"
filename = "ST000915.zip"

try:
    r = requests.get(url)
    r.raise_for_status()

    with open(filename, "wb") as f:
        f.write(r.content)
    
    print(f"Download complete: {filename}")

except requests.exceptions.RequestException as e:
    print(f"Download failed: {e}")