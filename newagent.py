from openpyxl import load_workbook

print("I am your Excel working agent!")

filename = input("Enter your file name (e.g., my_data.xlsx): ")

try:
    workbook = load_workbook(filename)
    page = workbook.active
    
    print("\nI am ready, Type 'done' to save and exit.")
    
    # This loop will run until the user types 'done'
    while True:
        user_action = input("What kind of data settlement do you want? (double/increase/add/done): ").lower()

        if user_action == "done":
            print("\nSaving changes and exiting.")
            break  # This keyword exits the loop

        elif user_action == "double":
            print("Processing double values...")
            for row_index, row in enumerate(page.iter_rows(min_row=2), start=2):
                pieces_left_cell = row[1]
                if isinstance(pieces_left_cell.value, (int, float)):
                    if pieces_left_cell.value < 100:
                        pieces_left_cell.value *= 2
                        print(f"Row {row_index} doubled to {pieces_left_cell.value}.")
                    else:
                        print(f"Row {row_index}:")
                else:
                    print(f"Row {row_index}: Skipping non-numeric value '{pieces_left_cell.value}'.")
        
        elif user_action == "increase":
            print("Processing data to increase values by 2...")
            for row_index, row in enumerate(page.iter_rows(min_row=2), start=2):
                pieces_left_cell = row[1]
                if isinstance(pieces_left_cell.value, (int, float)):
                    pieces_left_cell.value += 2
                    print(f"Row {row_index} value increased by 2. New value: {pieces_left_cell.value}.")
                else:
                    print(f"Row {row_index}: Skipping non-numeric value '{pieces_left_cell.value}'.")

        elif user_action == "add":
            print("Processing to add new data...")
            new_watch_data = ['Watch', 50, '8654321098']
            page.append(new_watch_data)
            print("New data for 'Watch' added successfully.")
            
        else:
            print("I don't understand that command. Please try again.")

    new_filename = 'updated_' + filename
    workbook.save(new_filename)
    print(f"\nDone! The updated data has been saved to '{new_filename}'.")

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found. Make sure it's in the same folder.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")