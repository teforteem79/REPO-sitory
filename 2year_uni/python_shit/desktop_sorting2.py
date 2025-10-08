import os
import shutil # You'll need this if you uncomment the move line

groups = [{'name': 'ext_eq_png', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\1', 
           'criteria': [{'field': 'Extension', 'operator': 'equals', 'value': '.png'}]}, 
          {'name': 'ext_eq_doc', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\2', 
           'criteria': [{'field': 'Extension', 'operator': 'equals', 'value': '.docx'}]}]

source_folder = 'C:/Users/Dream/Desktop/shutil_test'
total_count_criteria = 0 # Renamed for clarity

# --- Removed your old static criteria logic here ---

for group in groups:
    # --- FIXED: Dynamically extract the criteria and destination for the current group ---
    
    # 1. Get the destination path for the current group
    destination_folder = group['destination'] 
    print(f"Destination: {destination_folder}")
    
    # Optional: Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    # 2. Extract the criteria dictionary (assuming one criteria per group)
    criteria = group['criteria'][0] 
    
    # 3. Extract the operator and value from the criteria dictionary
    # Note: Using dictionary keys is more robust than list(dict(criteria).items())[x]
    operator = criteria['operator'] # operator = equals
    value = criteria['value']       # value = .png or .docx
    
    print(f"Criteria: {criteria}")
    print(f"Operator: {operator}") 
    print(f"Value: {value}")
    
    # 4. Loop through the files in the source folder
    group_count = 0 # Counter for files matched in the current group
    for j in os.listdir(source_folder):
        # Skip directories
        if os.path.isdir(os.path.join(source_folder, j)):
            continue
            
        file_extension = os.path.splitext(j)[1] # e.g., '.png' or '.docx'

        if operator == 'equals':
            # Check if the file's extension exactly matches the value (case-insensitive check is safer)
            if file_extension.lower() == value.lower():
                group_count += 1
                
                # --- This is the line you uncomment to MOVE files ---
                # shutil.move(src=os.path.join(source_folder, j), dst=os.path.join(destination_folder, j)) 
                
    print(f"Files matched for {group['name']}: {group_count}")
    total_count_criteria += group_count
    
print(f"\nTotal files matched across all groups: {total_count_criteria}")