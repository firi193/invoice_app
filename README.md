# Invoice Data Pipeline

## Overview

This project is an invoice data processing pipeline that loads, transforms, and validates invoice and line item data from CSV files. It includes containerization and deployment to a cloud service (Render) for easy access and querying.

## Features

* **Data Ingestion**: Loads invoice and line item data from CSV files.
* **Data Transformation**: Cleans the data, classifies line items, and adds line item totals.
* **Data Validation**: Validates data completeness, uniqueness, and referential integrity.
* **Mismatch Reporting**: Reports mismatches between invoice totals and line item totals.
* **API Endpoints**: Exposes endpoints to query the processed data.

## Cloud Deployment

This project is deployed on **Render** and is accessible via the following public API endpoints:

### API Endpoints

* **Invoice Count**

  * **Endpoint**: `https://invoice-app-1oh2.onrender.com/report/invoice-count`
  * **Description**: Returns the total number of invoices in the database.
 
<img width="851" alt="image" src="https://github.com/user-attachments/assets/5d40e699-582c-407f-bd45-34888fb0c85b" />



* **Unmatched Invoice Totals**

  * **Endpoint**: `https://invoice-app-1oh2.onrender.com/report/unmatched-totals`
  * **Description**: Returns a list of invoices with mismatched totals between the invoice and line items.
 
  <img width="904" alt="image" src="https://github.com/user-attachments/assets/3fd0d229-c395-4872-8f7c-57ba6de477c5" />



* **Line Items by Category**

  * **Endpoint**: `https://invoice-app-1oh2.onrender.com/report/line-items-category`
  * **Description**: Returns the count of line items by their category.
  
<img width="919" alt="image" src="https://github.com/user-attachments/assets/e808b812-3dd4-42c8-b554-127269313801" />



* **Revenue by Category**

  * **Endpoint**: `https://invoice-app-1oh2.onrender.com/report/revenue-category`
  * **Description**: Returns the total revenue by category.
 
<img width="845" alt="image" src="https://github.com/user-attachments/assets/fa6609d2-04a4-44da-a166-389e60d80724" />



 

## Database

The application uses **PostgreSQL** to store and query the invoice and line item data. You can interact with the database via the exposed API endpoints.



