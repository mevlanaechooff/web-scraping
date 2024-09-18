import tkinter as tk
from tkinter import filedialog
from src.scraper import fetch_data, parse_titles, save_to_csv
from src.utils import handle_exception

def scrape():
    url = url_entry.get()
    try:
        soup = fetch_data(url)
        if not soup:
            return
        titles = parse_titles(soup)
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            save_to_csv(titles, file_path)
            result_label.config(text="Veri başarıyla kaydedildi!")
    except Exception as e:
        handle_exception(e)
        result_label.config(text="Bir hata oluştu.")


root = tk.Tk()
root.title("Web Scraper")

url_label = tk.Label(root, text="URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

scrape_button = tk.Button(root, text="Veriyi Çek", command=scrape)
scrape_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
