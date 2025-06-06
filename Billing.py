from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Header row
DATA = [["Order ID", "Item Name", "Quantity", "Price (Rs.)", "Total (Rs.)"]]

# User inputs
order_id = input("Enter Order ID: ")
order_date = input("Enter Order Date (DD/MM/YYYY): ")
customer_name = input("Enter Customer Name: ")

num_items = int(input("How many items in the order? "))
grand_total = 0

# Loop for collecting item data
for i in range(num_items):
    print(f"\nItem {i+1} details:")
    item_name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item (Rs.): "))
    total = quantity * price
    grand_total += total
    DATA.append([order_id, item_name, str(quantity), f"{price:,.2f}", f"{total:,.2f}"])

# Add delivery charge
delivery_charge = float(input("\nEnter delivery charge (Rs.): "))
grand_total += delivery_charge

# Add rows for delivery and final total
DATA.append(["", "", "", "Delivery Charges", f"{delivery_charge:,.2f}"])
DATA.append(["", "", "", "Grand Total", f"{grand_total:,.2f}"])

# Create PDF
pdf = SimpleDocTemplate("online_order_invoice.pdf", pagesize=A4)
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1

title = Paragraph("Online Order Invoice", title_style)

# Optional subheading
subheading_style = styles["Normal"]
subheading = Paragraph(f"<b>Customer:</b> {customer_name}<br/><b>Order Date:</b> {order_date}", subheading_style)

# Table styling
style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -3), colors.beige),
    ("BACKGROUND", (0, -2), (-1, -1), colors.lightgrey),
])

table = Table(DATA, style=style)

# Build PDF
pdf.build([title, subheading, table])

print("\n✅ Invoice generated successfully: 'online_order_invoice.pdf'")


