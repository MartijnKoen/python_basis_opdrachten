# Dit Script vereist de volgende setup:
    # 1+ windows desktop met dit script en file sharing enabled
    # 1 windows desktop met de benaming "DATABASEPC" en file sharing enabled
        # Op windows desktop "DATABASEPC", de bestanden Kandidaat.txt | StudentReg.txt | Stem.txt onder de de file path C:\Users\public\Database
            # Kandidaat.txt | Lijst met de deelnemende kandidaten
            # StudentReg.txt | Lijst met personen die gestemd hebben
            # Stem.txt | Lijst met uitgebrachte stemmen

# Toetscombinatie Alt+ f4 om het stemvenster te sluiten
#--------------------------------------------------------------------------------


import tkinter as tk
from tkinter import messagebox

# Import candidates from Kandidaat.txt file
candidates = []
with open(r"\\DATABASEPC\Users\Public\Database\Kandidaat.txt", "r") as file:
    for line in file:
        candidates.append(line.strip())

# Define a function to handle the button click event
def submit_vote():
    selected_candidate = candidate_options.get()
    voter_id = voter_id_entry.get()

# Voter ID has to be exactly 9 digits & require candidate selection
    if len(voter_id) != 9:
        messagebox.showerror("Error", "Uw Deltion ID is niet herkend. Scan uw Deltion ID nogmaals.")
        # Clear the voter ID field
        voter_id_entry.delete(0, tk.END)
        # Autoselect voter ID field
        voter_id_entry.focus_set()
        return

    if selected_candidate == "":
        messagebox.showerror("Error", "U heeft geen kandidaat geselecteerd.")
        return

# Check Database StudentReg.txt for existing student ID
    with open(r"\\DATABASEPC\Users\Public\Database\StudentReg.txt", "r") as file:
        voter_ids = file.read().splitlines()
    if voter_id in voter_ids:
        messagebox.showerror("Error", "Uw stem is al geregistreerd. Meer dan 1 keer stemmen is niet mogelijk.")
        return

# Register submitted voter ID to the StudentReg database
    with open(r"\\DATABASEPC\Users\Public\Database\StudentReg.txt", "a") as file:
        file.write(voter_id + "\n")
    messagebox.showinfo("Vote Submitted", f"U heeft gestemd op {selected_candidate}. Uw stem wordt verwerkt. Hartelijk dank voor het deelnemen")

# Register the submitted vote from selected_candidate to the Stem.txt database
    with open(r"\\DATABASEPC\Users\Public\Database\Stem.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        candidate_votes = {candidate: 0 for candidate in candidates}
        for line in lines:
            candidate, votes = line.strip().split(":")
            candidate_votes[candidate] = int(votes)
        candidate_votes[selected_candidate] += 1
        for candidate in candidates:
            file.write(f"{candidate}:{candidate_votes[candidate]}\n")

# Reset UI after submission
    candidate_options.set("")
    voter_id_entry.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Voting System")

# Maximize window
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Make a frame for all widgets and center it in the window
input_frame =tk.Frame(root)
input_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create Voter frame and Vote ID field
vote_frame =tk.Frame(input_frame)
vote_frame.pack(pady=20)
voter_id_label = tk.Label(vote_frame, text="Scan je Deltion ID", anchor="center")
voter_id_label.pack()
voter_id_entry = tk.Entry(vote_frame)
voter_id_entry.pack()
# Ensure voter ID field is active by default
voter_id_entry.focus_set()

# Create Dropdown menu
dropdown_frame =tk.Frame(input_frame)
dropdown_frame.pack(pady=20)
tk.Label(dropdown_frame, text="Selecteer een kandidaat").pack()
candidate_options = tk.StringVar(root, "")
candidate_menu = tk.OptionMenu(dropdown_frame, candidate_options, *candidates)
candidate_menu.pack()

# Create the submit button
submit_frame = tk.Frame(input_frame)
submit_frame.pack(pady=20)
submit_button = tk.Button(submit_frame, text="Stem indienen", command=submit_vote, anchor="center")
submit_button.pack()

# Start the GUI event loop
root.mainloop()

