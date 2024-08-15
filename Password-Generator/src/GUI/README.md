# Password Generator Dashboard

## Overview
This directory contains a Streamlit-based dashboard that allows users to generate different types of passwords interactively. Users can choose between generating a random password, a pincode, or a memorable password with various customization options.

## Features
- **Random Password Generator**: Allows users to specify the length, and optionally include numbers and symbols.
- **Pincode Generator**: Generates numeric PIN codes with a customizable length.
- **Memorable Password Generator**: Creates passwords composed of multiple words, with options for capitalization and custom separators.

## Installation

To run this dashboard, ensure you have Python installed and the required packages by running:

```
pip install -r requirements.txt
```

## Dependencies
The dashboard relies on the following Python packages:
* streamlit
* src.password_generator (Located in the main repository's src directory)

  ## Usage
To start the dashboard, run the following command in your terminal:
```
streamlit run dashboard.py
```
This will start a local web server and open the dashboard in your browser.

## Repository structure 
```
GUI/
│
├── images/        
        └── banner.jpeg     # Banner image for the dashboard
├── README.md
├── dashboard.py            # Main Streamlit dashboard script
└── password-generator      # Script of different password generators imported in dashboard
```

## License
This project is licensed under the MIT License.
