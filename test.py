import os
from datetime import date, timedelta

today = date.today()
sunday = today + timedelta((6-today.weekday())%7)
test_date = sunday

if test_date != sunday:
    print("It's Not Sunday")
else:
    print("It's Sunday. Cleaning Files")
    file_count = 0
    print("Starting File Count: {}".format(file_count))
    path = "./support_files"
    print("Removing Files From: {}".format(path))

    for file in os.walk(path):
        print(f"Removing File: {file}")
        os.remove(str(file))
        print(f"File Removed: {file}")
        file_count += 1
        print(f"Updated File Count: {file_count}")
    
    print(f"Ending File Count: {file_count}")
