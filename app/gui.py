import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar


class AppGUI:
    def __init__(self, root):
        # GUI setup here

        self.root = root
        self.root.title("Facebook Comments Collector")

        # Using grid layout for frame1
        frame1 = tk.Frame(self.root)
        frame1.pack()

        self.input_label = tk.Label(frame1, text="Enter Post URL:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_entry = tk.Entry(frame1)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        self.collect_button = tk.Button(frame1, text="Collect Comments", command=self.collect_button_clicked)
        self.collect_button.grid(row=0, column=2, padx=10, pady=10)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

        # Using grid layout for frame2
        frame2 = tk.Frame(self.root)
        frame2.pack()

        self.save_button = tk.Button(frame2, text="Save Selected Comments", command=self.collect_button_clicked)
        self.save_button.grid(row=0, column=2, padx=10, pady=10)

        # Using grid layout for frame3
        frame3 = tk.Frame(self.root)
        frame3.pack()

        def on_scroll(event):
            if event.num == 4 or event.delta == 120:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5 or event.delta == -120:
                canvas.yview_scroll(1, "units")

        global canvas
        canvas = tk.Canvas(frame3)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind mouse wheel and touchpad scroll events to the canvas
        canvas.bind_all("<MouseWheel>", on_scroll)
        canvas.bind_all("<Button-4>", on_scroll)
        canvas.bind_all("<Button-5>", on_scroll)
        
        self.populate_scroll_area()

    def populate_scroll_area(self):
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

        for i in range(50):
            content_label = ttk.Label(scrollable_frame, text=f"{i} This is some example content.")
            content_label.pack(padx=20, pady=20)

        scrollable_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def collect_button_clicked(self):
        print("Done")

def main():
    root = tk.Tk()
    app = AppGUI(root)

    # Set the default window size and color
    root.geometry("1000x800")
    root.configure(bg="lightblue")
    
    root.mainloop()

if __name__ == "__main__":
    main()