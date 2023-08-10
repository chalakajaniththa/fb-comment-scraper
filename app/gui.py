import tkinter as tk
#from app.facebook_api import get_comments
#Sfrom app.database import insert_comment

class AppGUI:
    def __init__(self, root):
        # GUI setup here

        self.root = root
        self.root.title("Facebook Comments Collector")

        self.input_label = tk.Label(self.root, text="Enter Post ID:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.collect_button = tk.Button(self.root, text="Collect Comments", command=self.collect_button_clicked)
        self.collect_button.pack()

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()
        pass

    def collect_button_clicked(self):
        post_id = self.input_entry.get()
        # comments = get_comments(post_id)  # Uncomment and replace with actual function
        # for comment in comments:
        #     insert_comment(comment)        # Uncomment and replace with actual function
        self.status_label.config(text="Comments collected and stored.")  # Update status label

        # Update GUI elements as needed

def main():
    root = tk.Tk()
    app = AppGUI(root)

    # Set the default window size
    root.geometry("1000x800")  # Width: 400, Height: 300

    root.mainloop()

if __name__ == "__main__":
    main()