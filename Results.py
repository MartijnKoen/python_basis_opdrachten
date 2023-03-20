# Dit Script vereist de volgende setup:
    # 1+ windows desktop met dit script, PyCharm en file sharing enabled
        # Pycharm geinstalleerd op het Public User account
        # Installatie van pip 23.0.1 voor python 3.11  voor de matplotlib functie
    # 1 windows desktop met de benaming "DATABASEPC" en file sharing enabled
        # Op windows desktop "DATABASEPC", het bestand Stem.txt onder de de file path C:\Users\public\Database
            # Stem.txt | Lijst met uitgebrachte stemmen


# --------------------------------------------------------------------------------

import sys
sys.path.append(r"C:\Users\Public\PycharmProjects\pythonProject\venv\Lib\site-packages")

import matplotlib.pyplot as plt

# Set the network path to the text file
file_path = r"\\DATABASEPC\Users\Public\Database\Stem.txt"

# Read the file and split it into lines
with open(file_path, "r") as f:
    lines = f.read().splitlines()

# Extract the names and values from the lines
names, values = zip(*(line.split(":") for line in lines))

# Convert the values to integers
values = [int(value) for value in values]

# Calculate the percentages
total = sum(values)
percentages = [(value/total)*100 for value in values]

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(percentages, labels=names, autopct="%1.1f%%")
ax.set_title("Resultaten")

# Show the pie chart
plt.show()
