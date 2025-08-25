import tkinter as tk
from tkinter import messagebox
from scraper import scrape_community

def start_scraping():
    community_url = url_entry.get()
    if not community_url:
        messagebox.showerror("Error", "Please enter a Roblox community URL.")
        return
    results = scrape_community(community_url)
    for result in results:
        output_text.insert(tk.END, str(result) + "\n")

# Set up the GUI
root = tk.Tk()
root.title("Roblox Community Scraper")

url_label = tk.Label(root, text="Enter Roblox Community URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
start_button.pack()

output_text = tk.Text(root, height=20, width=80)
output_text.pack()

root.mainloop()
