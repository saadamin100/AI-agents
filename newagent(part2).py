from openpyxl import Workbook

# Create a new workbook object. Think of this as an empty Excel file in memory.
workbook = Workbook()

# Get the active worksheet, which is the first sheet by default.
sheet = workbook.active

# Give the sheet a name.
sheet.title = "Sales Data"

# Add column headers to the first row.
sheet['A1'] = 'Product'
sheet['B1'] = 'Pieces'
sheet['C1'] = 'Barcodes'

# Add some sample data to the rows below the headers.
data = [
    ('Trousers', 150, '12454564'),
    ('Shirts', 80, '55449433'),
    ('Pants', 220, '384878322'),
    ('Shoes', 95, '7565444'),
    ('T-shirts', 180, '94858929')
]

for row in data:
    sheet.append(row)

# This will create a new Excel file named "Inventory.xlsx".
workbook.save("Inventory.xlsx")

print("The Excel file 'Inventory.xlsx' has been created successfully!")