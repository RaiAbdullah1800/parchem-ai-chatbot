from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_order_email(sender: str, recipient: str, order_details: dict) -> MIMEMultipart:
    """Create professional order email"""
    formatted_text = f"""
    CHEMICAL ORDER DETAILS
    ------------------------
    Product: {order_details['product']}
    Quantity: {order_details['quantity']} {order_details['unit']}
    Packaging: {order_details['packaging']}
    Delivery Date: {order_details['delivery_date']}
    
    COMPANY INFORMATION
    -------------------
    Name: {order_details['company_name']}
    Email: {order_details['email']}
    Phone: {order_details['phone']}
    Address: {order_details['address']}
    Website: {order_details.get('website', 'N/A')}
    Country: {order_details['country']}
    Occupation: {order_details['occupation']}
    
    SPECIAL INSTRUCTIONS
    --------------------
    {order_details.get('special_instructions', 'None')}
    """

    html_content = f"""
    <html>
      <head>
        <style>
          .order-card {{ 
              border: 1px solid #e0e0e0;
              border-radius: 10px;
              padding: 25px;
              margin: 20px 0;
              font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
          }}
          .section-title {{
              color: #2c3e50;
              border-bottom: 2px solid #3498db;
              padding-bottom: 8px;
              margin: 20px 0 15px;
              font-size: 1.2em;
          }}
          .detail-row {{ margin: 12px 0; }}
          .detail-label {{
              font-weight: 600;
              color: #3498db;
              min-width: 140px;
              display: inline-block;
          }}
        </style>
      </head>
      <body>
        <div class="order-card">
          <h2 style="color: #2c3e50; margin-top: 0;">New Chemical Order</h2>
          
          <div class="section-title">Order Details</div>
          <div class="detail-row">
            <span class="detail-label">Product:</span> {order_details['product']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Quantity:</span> {order_details['quantity']} {order_details['unit']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Packaging:</span> {order_details['packaging']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Delivery Date:</span> {order_details['delivery_date']}
          </div>
          
          <div class="section-title">Company Information</div>
          <div class="detail-row">
            <span class="detail-label">Name:</span> {order_details['company_name']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Email:</span> {order_details['email']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Phone:</span> {order_details['phone']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Address:</span> {order_details['address']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Website:</span> {order_details.get('website', 'N/A')}
          </div>
          <div class="detail-row">
            <span class="detail-label">Country:</span> {order_details['country']}
          </div>
          <div class="detail-row">
            <span class="detail-label">Occupation:</span> {order_details['occupation']}
          </div>
          
          <div class="section-title">Special Instructions</div>
          <div class="detail-row">
            {order_details.get('special_instructions', 'None')}
          </div>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"🔬 Chemical Order - {order_details['company_name']}"
    msg['From'] = f"Parchem Orders <{sender}>"
    msg['To'] = recipient
    
    part1 = MIMEText(formatted_text, 'plain')
    part2 = MIMEText(html_content, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    return msg
