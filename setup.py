from setuptools import setup, find_packages

setup(
    name='OdooXMLRPCLibrary',
    version='0.3.12',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        # 'xmlrpc.client',  # Corrected import for xmlrpc.client
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            #--------------- ↓ ResPartnerModel ↓ ------------------------
            'create_contact = OdooXMLRPCLibrary.ResPartnerModel:create_contact',
            'get_contact_data = OdooXMLRPCLibrary.ResPartnerModel:get_contact_data',
            #--------------- ↓ SaleOrderModel ↓ ------------------------
            'create_sale_order = OdooXMLRPCLibrary.SaleOrderModel:create_sale_order',
            'get_sale_order_data = OdooXMLRPCLibrary.SaleOrderModel:get_sale_order_data',
            'confirm_sale_order = OdooXMLRPCLibrary.SaleOrderModel:confirm_sale_order',
        ],
    },
    author='Aditya Irri',
    author_email='adityairri@gmail.com',
    description='OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using XML-RPC API. With modules like create_sales_order and create_contact, it provides an easy-to-use interface for managing rental orders and contacts in the Odoo platform. Whether youre integrating Odoo functionality into your application or automating business processes, OdooXMLRPCLibrary streamlines the communication process, making it efficient and developer-friendly.',
    long_description_content_type='text/markdown',
    long_description='''
    # OdooXMLRPCLibrary

OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using the XML-RPC API. It provides modules for Creating contacts, Creating Sales Order in the Odoo platform.

## Features

*res.partner* Model
- Add a new contact in the Odoo platform.
- Get Contact Details by Phone Number or Name.

*sale.order* Model
- Add Sales Order in the Odoo platform.
- Get Sales Order Data by Order ID.
- Confirm a Sales Order.

*More Modules and Features Coming Soon*

## Installation

To install the library, you can use pip:

```bash
pip install OdooXMLRPCLibrary
```

## How To Use?

**Importing**
```python
from odoo_library.res_partner import ResPartnerModel
from odoo_library.sale_order import SaleOrderModel
```

**Code Usage**
```python
# -------------------------- Example code to create a Contact --------------------------

# Create instances of the libraries
res_partner_model_instance = ResPartnerModel()

# Run the Instance
res_partner_model_instance.run()

# Prepare Data
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

# Send data to the function
response = res_partner_model_instance.create_contact(data)

#Get Response
return (response)




# -------------------------- Example code to Get Contact Data --------------------------

# Create instances of the libraries
res_partner_model_instance = ResPartnerModel()

# Run the Instance
res_partner_model_instance.run()

# Prepare Data
# Can use either 'name' or 'phone' to get the contact details 
data = {
    "odoo_server_url": "https://exampledb.odoo.com/",   # Your Odoo server URL here (with http or https)
    "database_name": "exampledb",                       # The database name on your Odoo Server 
    "odoo_username": "DB Username",                     # The username for your Odoo Database
    "odoo_password": "DB Password",                     # The password for your Odoo Database user
    "name": "",                                         # Name of contact person (Optional)
    "phone": ""                                         # Phone number of contact person (Optional)
}

# Send data to the function
response = res_partner_model_instance.get_contact_data(data)

#Get Response
return (response)







# -------------------------- Example code to create a Sale Order  --------------------------

# Create instances of the libraries
sale_order_model_instance = SaleOrderModel()

# Run the Instance
sale_order_model_instance.run()

# Prepare Data
data = {
    "odoo_server_url": "https://exampledb.odoo.com/",   # Your Odoo server URL here (with http or https)
    "database_name": "exampledb",                       # The database name on your Odoo Server 
    "odoo_username": "DB Username",                     # The username for your Odoo Database
    "odoo_password": "DB Password",                     # The password for your Odoo Database user
    "name": "",                                         # Leave it blank as we will generate automatically
    "customerNumber": "",                               # Customer's phone number / customer id in your system
    "customerId": "",                                   # Customer Id from Contacts API
    "resellerNumber": "",                               # Reseller Number (Only required if you are creating an OpenERP account)
    "resellerId": "",                                   # Reseller Id from Accounts API
    "gst_treatment": "",                                # GST Treatment if any ("registered" or "unregister
    "expirationDate": "",                               # Expiry Date in YYYY-MM-DD format
    "quotationDate": "",                                # Quotation Date in format YYYY-MM-DD
    "pricelist": "",                                    # Price List Name
    "orderLine_productNames": ["",""],                  # Product Names for which you want to raise order lines (array of string)
    "orderLine_productId": [],                          # Product Id's for which you want to raise an order (array of numbers)
    "orderLine_description": [],                        # Array of order lines description (array of string)
    "orderLine_quantity":[],                            # Quantity for each product in orderline[] (array of float)
    "orderLine_unitPrice":[],                           # Unit price for each product in orderline[] format (array of float)
    "orderLine_taxes": [],                              # Taxes for each order Line (array of float)
    "orderLine_discount": []                            # Discounts for each order Line (array of float)
}

# Send data to the function
response = sale_order_model_instance.create_sale_order(data)

#Get Response
return (response)




# -------------------------- Example code to get Sales Order Data --------------------------

# Create instances of the libraries
sale_order_model_instance = SaleOrderModel()

# Run the Instance
sale_order_model_instance.run()

# Prepare Data
data = {
    "odoo_server_url": "https://exampledb.odoo.com/",   # Your Odoo server URL here (with http or https)
    "database_name": "exampledb",                       # The database name on your Odoo Server 
    "odoo_username": "DB Username",                     # The username for your Odoo Database
    "odoo_password": "DB Password",                     # The password for your Odoo Database user
    "orderID": "",                                      # The sales order ID (String) / Odoo Database ID (Int) you want to retrieve data for
}

# Send data to the function
response = sale_order_model_instance.get_sale_order_data(data)

#Get Response
return (response)





# -------------------------- Example code to Confirm Sales Order Data --------------------------

# Create instances of the libraries
sale_order_model_instance = SaleOrderModel()

# Run the Instance
sale_order_model_instance.run()

# Prepare Data
data = {
    "odoo_server_url": "https://exampledb.odoo.com/",   # Your Odoo server URL here (with http or https)
    "database_name": "exampledb",                       # The database name on your Odoo Server 
    "odoo_username": "DB Username",                     # The username for your Odoo Database
    "odoo_password": "DB Password",                     # The password for your Odoo Database user
    "orderID": "",                                      # The sales order ID you want to Confirm Order
}

# Send data to the function
response = sale_order_model_instance.confirm_sale_order(data)

#Get Response
return (response)
```


Feel free to paste this directly into your README.md file and customize it further if needed.
''',
    url='https://github.com/aditya-infiplus/odooXMLRPCLibrary.git',
    license='MIT',
)