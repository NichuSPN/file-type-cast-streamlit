# Streamlit File Type Cast Project

## Public URL
- Access the deployed application here - https://nichu-data-file-convert.streamlit.app/

## Overview
This project was created to experiment with features of Streamlit, including tabs, file uploaders, and download buttons. It provides a user-friendly interface for uploading files in various formats (CSV, JSON, XLSX), editing the data, and downloading the modified data in the selected format.

## Features
- **File Uploading**: Users can upload files in CSV, JSON, or XLSX formats.
- **Data Editing**: After uploading, users can edit the data using a built-in data editor.
- **Download Options**: Users can download the edited data in their preferred format (CSV or JSON).

## File Structure
- `main.py`: The main entry point of the application that sets up navigation between different pages.
- `singlepage.py`: A single-page application that allows file uploading, editing, and downloading without tabs.
- `tabs.py`: A multi-tab application that organizes the functionalities into separate tabs for better user experience.
- `utils.py`: Contains utility functions for file handling and data processing.

## Installation
To run this project, ensure you have Python and Streamlit installed. You can install Streamlit using pip:
```bash
pip install streamlit
```

## Running the Application
To start the application, run the following command in your terminal:
```bash
streamlit run main.py
```

## Usage
1. Choose a file to upload from your local system.
2. Edit the data as needed.
3. Select the desired format for downloading the edited data.
4. Click the download button to save the file.
