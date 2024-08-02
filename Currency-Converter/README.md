# Currency Converter
![app image](./images/currency-converter.png)
This Python project allows users to convert currencies using real-time exchange rates from the ExchangeRate-API. It includes a command-line interface (CLI) and a graphical user interface (GUI) built with Streamlit.

## Features
* Fetches up-to-date exchange rates from ExchangeRate-API
* Caches exchange rates for 3 hours to reduce API calls
* Supports conversion between any two currencies available in the API
* Provides both CLI and GUI options for user interaction

  ## Requirements
* Python 3.x
* `requests` library
* `cachetools` library
* `streamlit` library

  ## Installation
  1. Clone this repository or download the script
  2. Install required libraries
     
     ```pip install requests cachetools streamlit```

## Usage
### Command-Line Interface (CLI)
Run the script and follow the prompts: `python currency-converter.py`
1. Enter the base currency code (e.g., USD, EUR, GBP)
2. Enter the target currency code
3. Enter the amount to convert
The script will display the converted amount.

### Graphical User Interface (GUI)
Run the Streamlit app: `streamlit run app.py`
Follow the instructions on the web interface to enter the base currency, target currency, and amount to convert. The converted amount will be displayed on the page.

## Note
This project uses a free API which may have rate limits. The caching mechanism helps to reduce API calls, but be mindful of usage limits.







