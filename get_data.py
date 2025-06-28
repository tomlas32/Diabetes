"""
Script to download the metabolomics dataset ST001906_1 from the Metabolomics Workbench.
This script fetches the ZIP archive for study ST001906_1 from the official download link 
and saves it locally as 'ST001906_1.txt'.

Source: https://www.metabolomicsworkbench.org/

Author: Tomasz Lasota
Version: 1.0
Date: 2025-06-27
"""


import requests

url = "https://www.metabolomicsworkbench.org/data/showfile_t.php?RA=86.186.80.144&DF=MSdata_ST001906_1.txt"
filename = "ST001906_1.txt"

try:
    r = requests.get(url)
    r.raise_for_status()

    with open(filename, "wb") as f:
        f.write(r.content)
    
    print(f"Download complete: {filename}")

except requests.exceptions.RequestException as e:
    print(f"Download failed: {e}")