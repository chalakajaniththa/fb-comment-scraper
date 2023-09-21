import tkinter as tk
from tkinter import ttk

def on_scroll(event):
    if event.num == 4 or event.delta == 120:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5 or event.delta == -120:
        canvas.yview_scroll(1, "units")

def create_scrollable_element():
    root = tk.Tk()
    root.title("Simple Scrollable Element")
    root.geometry("400x300")

    global canvas
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Bind mouse wheel and touchpad scroll events to the canvas
    canvas.bind_all("<MouseWheel>", on_scroll)
    canvas.bind_all("<Button-4>", on_scroll)
    canvas.bind_all("<Button-5>", on_scroll)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    content_label = ttk.Label(frame, text="This is some example content.\n" * 20)
    content_label.pack(padx=20, pady=20)

    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    root.mainloop()

if __name__ == "__main__":
    create_scrollable_element()
