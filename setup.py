from setuptools import setup, find_packages

setup(
    name='OdooXMLRPCLibrary',
    version='0.3.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        # 'xmlrpc.client',  # Corrected import for xmlrpc.client
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'create_contact = OdooXMLRPCLibrary.create_contact:main',
            'create_sale_order = OdooXMLRPCLibrary.saleOrderModel:main',
        ],
    },
    author='Aditya Irri',
    author_email='adityairri@gmail.com',
    description='OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using XML-RPC API. With modules like create_sales_order and create_contact, it provides an easy-to-use interface for managing rental orders and contacts in the Odoo platform. Whether youre integrating Odoo functionality into your application or automating business processes, OdooXMLRPCLibrary streamlines the communication process, making it efficient and developer-friendly.',
    long_description_content_type='text/markdown',
    long_description='''
    # OdooXMLRPCLibrary

OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using the XML-RPC API. It provides modules for creating contacts, Creating Sales Order in the Odoo platform.

## Features

- Add and Manage contacts in the Odoo platform.

## Installation

To install the library, you can use pip:

```bash
pip install OdooXMLRPCLibrary
```

## How To Use?

**Importing**
```python
from odoo_library.create_contact import CreateContactLibrary
from odoo_library.saleOrderModel import SaleOrderModel

# Create instances of the libraries
create_contact_instance = CreateContactLibrary()
create_sale_order_instance = SaleOrderModel()

# Run the Flask apps
create_contact_instance.run()
create_sale_order_instance.run()
```

**Code Usage**
```python
# Example code to create a Contact
data = {
    "odoo_server_url": "https://exampledb.odoo.com/",   # Your Odoo server URL here (with http or https)
    "database_name": "exampledb",                       # The database name on your Odoo Server 
    "odoo_username": "DB Username",                     # The username for your Odoo Database
    "odoo_password": "DB Password",                     # The password for your Odoo Database user
    "contact_name": "",                                 # Name of the contact
    "company_name": "",                                 # Company name of the contact
    "company_type": "company",                          # Type of company ("company" or "person")
    "address_type": "invoice",                          # Address type ("delivery" or "invoice")
    "street1": "Test Street 1",                         # First line of address
    "street2": "Test Street 2",                         # Second line of address (optional)
    "city": "Hyderabad",                                # City
    "state": "Telangana",                               # State
    "country": "India",                                 # Country
    "zip": "500032",                                    # Zip Code
    "gst_treatment": "",                                # GST Treatment if any ("registered" or "unregistered
    "vat": "",                                          # VAT number (if any)
    "job_position": "",                                 # Job Position (If applicable)
    "phone": "9988776655",                              # Phone Number
    "mobile": "",                                       # Mobile Number (Optional)
    "email": "Email@example.com",                       # Email ID
    "website": "https://example.com",                   # Website URL (Optional)
    "title": "",                                        # Title (Optional)
    "tags": ""                                          # Tags (Comma separated list, Optional)
}

response = create_contact_instance.create_contact(data)
return (response)







# Example code to create a Sale Order
data = {
    "odoo_server_url": "https://aquaexchange-20240123-umsh.odoo.com/",   # Replace with your Odoo Server URL
    "database_name": "aquaexchange-20240123-umsh",                       # Replace with your Database Name
    "odoo_username": "pavan@aquaexchange.com",                           # Replace with your Odoo Username
    "odoo_password": "AXOdoo@456",                                       # Replace with your Odoo Password
    "name": "",                                                          # Leave it blank as we will generate automatically
    "customerNumber": "6309528941",                                      # Customer's phone number / customer id in your system
    "customerId": "",                                                    # Customer Id from Contacts API
    "resellerNumber": "6309528941",                                      # Reseller Number (Only required if you are creating an OpenERP account)
    "resellerId": "",                                                    # Reseller Id from Accounts API
    "gst_treatment": "",                                                 # GST Treatment if any ("registered" or "unregister
    "expirationDate": "",                                                # Expiry Date in YYYY-MM-DD format
    "quotationDate": "",                                                 # Quotation Date in format YYYY-MM-DD
    "pricelist": "Public Pricelist (INR)",                               # Price List Name
    "orderLine_productNames": ["Vannastar 2P","Vannastar 2P"],           # Product Names for which you want to raise order lines
    "orderLine_productId": [],                                           # Product Id's for which you want to raise an order
    "orderLine_description": [],                                         # Array of order lines description
    "orderLine_quantity":[3],                                            # Quantity for each product in orderline[] 
    "orderLine_unitPrice":[],                                            # Unit price for each product in orderline[] format
    "orderLine_taxes": [],                                               # Taxes for each order Line
    "orderLine_discount": []                                             # Discounts for each order Line
}

response = create_sale_order_instance.create_sale_order(data)
return (response)
```


Feel free to paste this directly into your README.md file and customize it further if needed.
''',
    url='https://github.com/aditya-infiplus/odooXMLRPCLibrary.git',
    license='MIT',
)