# Web Scraping - Product Information

This is a web scraping project created using Python. The goal of this project is to retrieve product information from a website using the following Python modules:

- **Requests**: Used to send HTTP requests and retrieve the HTML content of a web page.
- **Beautiful Soup**: Used for parsing the HTML content and extracting data from it.
- **Pandas**: Used to convert the extracted data into a CSV file..
- **Sys**: Used for accessing system-specific parameters and functions.

## Project Overview

The project follows these steps:

1. Import the necessary modules:
   ```python
   import requests
   from bs4 import BeautifulSoup
   import pandas as pd
   import sys
   
2. Send a request to the website using the requests.get() function to retrieve the HTML content.

3. Use Beautiful Soup to parse the HTML content and extract the desired information, such as product names, prices, and links.

4. Create a dictionary to store the extracted data:
   ```python
   data = {'Title': [], 'Price': [], 'Link': []}
5. Populate the data structure with the extracted information.

6. Convert the dictionary to a pandas DataFrame using:
   ```python
   pd.DataFrame.from_dict().

7. Save the DataFrame as a CSV file using the to_csv() method:
   ```python
   df.to_csv("data.csv", index=False)
   
## Requirements

To run this project, make sure you have the following packages installed:

- Requests: pip install requests
- Beautiful Soup: pip install beautifulsoup4
- Pandas: pip install pandas

## Usage
Clone the project repository.

1. Install the required packages.

2. Run the Python script to execute the web scraping and generate the CSV file.

3. The resulting CSV file, named "data.csv", will contain the product names, prices, and links.

Feel free to modify the code and adapt it to your specific use case. Happy web scraping!

Note: Please respect the terms of service and usage policies of the targeted website when performing web scraping.
