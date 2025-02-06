# Configuration constants file code
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
DEFAULT_RECIPIENT = "adigitalcare@gmail.com"
"""PACKAGING_OPTIONS = [
    "BULK / RAILCAR / BARGE",
    "FCL / TL / ISO TANK",
    "PALLET / SKID / TOTE",
    "DRUM / BAG",
    "R&D / PILOT"
]"""
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
    'product': "Which product are you interested in?",
    'unit': "Select your preferred unit",
    'quantity': "How many units do you need?",
#    'packaging': "Select packaging type:",
    'delivery_date': "Select delivery date:",
#    'company_name': "What’s your company name?",
#    'country':"Which country are you in?",
    'email': "What’s your business email?",
#    'phone': "What’s your contact number?",
    'address': "Enter your location",
#    'website': "Do you have a website? (optional)",
#    'occupation': "what’s your occupation:",
#    'special_instructions': "Any special instructions? (optional)"
}