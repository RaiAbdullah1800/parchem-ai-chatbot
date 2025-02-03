# Configuration constants file code
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
DEFAULT_RECIPIENT = "adigitalcare@gmail.com"
PACKAGING_OPTIONS = [
    "BULK / RAILCAR / BARGE",
    "FCL / TL / ISO TANK",
    "PALLET / SKID / TOTE",
    "DRUM / BAG",
    "R&D / PILOT"
]
UNIT_OPTIONS = [
    "Metric tons",
    "Kilogram",
    "Pound",
    "Gallon",
    "Gram",
    "Liter",
    "MOQ"
]
ORDER_FIELDS = {
    'product': "Enter product name:",
    'unit': "Select unit for quantity:",
    'quantity': "Enter quantity:",
    'packaging': "Select packaging type:",
    'delivery_date': "Select delivery date:",
    'company_name': "Enter company name:",
    'country':"Enter your country name",
    'email': "Enter business email:",
    'phone': "Enter contact number:",
    'address': "Enter delivery address:",
    'website': "Company website (optional):",
    'occupation': "Enter your occupation:",
    'special_instructions': "Special instructions (optional):"
}