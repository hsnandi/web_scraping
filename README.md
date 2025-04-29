# Automated Order Extraction from Flipkart

## Project Overview
This project aims to automate the process of logging into a Flipkart account, navigating to the "Orders" page, and extracting various details about the orders. The extracted data includes the order ID, product name, price, quantity, delivery status, payment method, and more. The script handles login automation, pagination of the orders, and data extraction in a structured format (CSV/JSON).

## Objective
- Log in to Flipkart using either mobile number/OTP or email/password.
- Extract order details from the "Orders" page on Flipkart.
- Export extracted information in CSV and JSON formats.

## Technologies Used
- **Python**: The core programming language for the script.
- **Playwright**: Used for automating the web browser to interact with Flipkart.
- **CSV & JSON**: For data export and persistence.

## Project Progress
Due to a limitation with OTP (One-Time Password) requests (maximum attempts reached), the current implementation includes login functionality up until OTP entry. The code demonstrates the login process using the mobile number and OTP, as well as navigating through the Flipkart profile to the Orders page.

### Login Automation (Incomplete due to OTP issue)
- The script accepts a phone number as input.
- Sends OTP to the provided number.
- The user manually inputs the OTP into the script.
- After successful login, the script navigates to the "Orders" section by clicking the profile and dropdown buttons.

### Data Scraping Demonstration
For demonstration purposes, a different website (`https://quotes.toscrape.com/login`) was used to showcase the scraping and data export capabilities. The process involves:
- Logging into the website with a provided username and password.
- Scraping the quotes, authors, and tags from all pages of the website.
- Exporting the data to both CSV and JSON files.


## Installation & Requirements
1. Clone the repository to your local machine.
2. Install required dependencies:
   ```bash
   pip install playwright
   playwright install

## Usage
1. To run the Flipkart login automation and order extraction:

- Provide your phone number when prompted.

- Enter the OTP you receive.

2. To run the quotes scraping demo:

- Provide any values for the username and password fields on the https://quotes.toscrape.com website.

- The quotes will be saved in both CSV and JSON formats.