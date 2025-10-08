import os
import shutil
import string
import random

#688 541

#region Create junk files

def create_garbage():
    """
    Warning: TEST FUNCTION.
    WILL CREATE 1000 JUNK FILES ON YOUR DESKTOP!
    -------
    You can change the number of files in the
    NUM_FILES constant
    
    ps. just use sortDesktop() function to clean up :)
    """
    NUM_FILES = 100
    EXTENSIONS = ['.docx', '.mp3', '.pdf', '.pptx', '.xlsx', '.png', '.mp4']

    if os.name == 'nt':
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

    def random_filename(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # Create dummy files
    for _ in range(NUM_FILES):
        ext = random.choice(EXTENSIONS)
        name = random_filename() + ext
        file_path = desktop + f'\\{name}'
        
        with open(file_path, 'wb') as f:
            if ext in ['.mp3', '.png', '.pdf']:
                f.write(os.urandom(1024))  # random binary data (1 KB)
            else:
                f.write(b"This is a dummy file for testing.\n")

#endregion Create junk files
# create_garbage()

#region Move files to dirs
def sortDesktop():
    """Dummy function.\n
    Creates seven folders for different file types,
    then moves them from desktop to the corresponding folders.\n
    Supported file extensions in development."""

    # path to desktop in string
    if os.name == 'nt':
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

    # create folders (if they don't exist, otherwise do nothing)

    os.makedirs(desktop + '\\docs', exist_ok=True)
    os.makedirs(desktop + '\\pdfs', exist_ok=True)
    os.makedirs(desktop + '\\presentations', exist_ok=True)
    os.makedirs(desktop + '\\tables', exist_ok=True)
    os.makedirs(desktop + '\\images', exist_ok=True)
    os.makedirs(desktop + '\\videos', exist_ok=True)
    os.makedirs(desktop + '\\audios', exist_ok=True)
    # move files to the folders
    for i in os.listdir(desktop):   # list of all filenames in desktop
        if '.lnk' in i: # ignores links
            pass
        elif os.path.splitext(i)[1] == '.png': # checks extension (only the end point e.g. {filename.docx.pptx will go to presentations})
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\images') # forming of a destination string

        elif os.path.splitext(i)[1] == '.docx':
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\docs')
        elif os.path.splitext(i)[1] == '.pptx':
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\presentations')
        elif os.path.splitext(i)[1] == '.xlsx':
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\tables')
        elif os.path.splitext(i)[1] == '.mp3':
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\audios')
        elif os.path.splitext(i)[1] == '.mp4' :
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\videos')
        elif os.path.splitext(i)[1] == '.pdf':
            shutil.move(src=desktop + f'\\{i}', dst=desktop + '\\pdfs')
    print('Moving complete!')
#endregion Move files to dirs

# sortDesktop()
# groups = [{'name': 'ext_eq_png', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\1',
#             'criteria': [{'field': 'Extension', 'operator': 'equals', 'value': '.docx'}]}]

groups = [{'name': 'ext_eq_png', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\1', 
            'criteria': [{'field': 'Extension', 'operator': 'equals', 'value': '.png'}]},
            {'name': 'name_eq_bebra', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\3', 
            'criteria': [{'field': 'Name', 'operator': 'contains', 'value': 'ebr'}]},
            # {'name': 'size_>_than', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\4', 
            # 'criteria': [{'field': 'Size', 'operator': '>', 'value': '10'}]},
            {'name': 'ext_eq_doc', 'destination': 'C:/Users/Dream/Desktop/shutil_test\\2', 
             'criteria': [{'field': 'Extension', 'operator': 'equals', 'value': '.docx'}]}]
# print(groups)
source_folder = 'C:/Users/Dream/Desktop/shutil_test'

#destination folder
print(list(groups[0].items())[1][1])

# if os.name == 'nt':
#         desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
# for i in os.listdir(desktop):
#     stats = os.stat(desktop + f'/{i}')
#     sizeBytes = stats.st_size
#     sizeMBytes = sizeBytes / 1024
#     print(f'{sizeMBytes:.2f}')
#     print(os.path.splitext(i)[0]) - splits filename into name [0], and extension [1]























#region Sorting Function

count_criteria = 0
criteria = list(groups[0].items())[2][1][0] # dictionary 'criteria'
operator = list(dict(criteria).items())[1][1] # operator = equals in criteria
value = list(dict(criteria).items())[2][1] # value = .png in criteria
print(criteria)
print(operator) 
print(value)

def moveFiles(j):
    shutil.move(src=os.path.join(source_folder, j), dst=os.path.join(destination_folder, j))

for group in groups:
    print(list(group.items())[2][1][0])
    destination_folder = group['destination']
    criteria = group['criteria'][0]
    field = criteria['field']
    operator = criteria['operator']
    value = criteria['value']
    for j in os.listdir('C:/Users/Dream/Desktop/shutil_test'):
        if field == 'Extension':
            file_extension = os.path.splitext(j)[1]
            if operator == 'equals':
                if file_extension.lower() == value.lower():
                    count_criteria += 1
                    moveFiles(j)
        elif field == 'Name':
            filename = os.path.splitext(j)[0]
            if operator == 'equals':
                if filename == value:
                    moveFiles(j)
            if operator == 'contains':
                if value in filename:
                    moveFiles(j)
        # elif field == 'Path':
        elif field == 'Size':
            stats = os.stat(source_folder + f'//{j}')
            sizeBytes = stats.st_size
            sizeKBytes = sizeBytes / 1024
            if operator == '>':
                if sizeKBytes > float(value):
                    moveFiles(j)
            if operator == '<':
                if sizeKBytes < float(value):
                    moveFiles(j)
print(count_criteria)




    
# print(os.listdir('C:/Users/Dream/Desktop/shutil_test'))