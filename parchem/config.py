# Configuration constants
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
DEFAULT_RECIPIENT = "naveed49478@gmail.com"
PACKAGING_OPTIONS = [
    "BULK / RAILCAR / BARGE",
    "FCL / TL / ISO TANK",
    "PALLET / SKID / TOTE",
    "DRUM / BAG",
    "R&D / PILOT"
]
ORDER_FIELDS = {
    'product': "Enter product name:",
    'quantity': "Enter quantity with unit (e.g., 100kg):",
    'packaging': "Select packaging type:",
    'delivery_date': "Select delivery date:",
    'company_name': "Enter company name:",
    'email': "Enter business email:",
    'phone': "Enter contact number:",
    'address': "Enter delivery address:",
    'website': "Company website (optional):",
    'special_instructions': "Special instructions (optional):"
}