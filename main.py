import tkinter as tk
import random
import threading
import time


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("500x400")

        # create the text boxes
        self.textboxes = []
        colors = [
            "light steel blue",
            "misty rose",
            "seashell4",
            "lightsalmon2",
            "light goldenrod",
            "lavender",
        ]
        for i in range(6):
            textbox = tk.Label(
                self.root,
                text="0",
                font=("Arial", 24),
                bg=colors[i],
                width=10,
                height=5,
            )
            textbox.grid(row=(i // 3), column=(i % 3), padx=10, pady=10)
            self.textboxes.append(textbox)

        # create the threads for updating the text boxes
        self.threads = []
        self.threads.append(
            threading.Thread(target=self.update_textbox, args=(0, 10, 20, 1))
        )
        self.threads.append(
            threading.Thread(target=self.update_textbox, args=(1, -10, 10, 2))
        )
        self.threads.append(
            threading.Thread(target=self.update_textbox, args=(2, -100, 0, 5))
        )
        self.threads.append(
            threading.Thread(target=self.update_textbox, args=(3, 0, 20, 3))
        )
        self.threads.append(
            threading.Thread(target=self.update_textbox, args=(4, -40, 40, 6))
        )
        self.threads.append(
            threading.Thread(target=self.update_textbox, args=(5, 100, 200, 4))
        )

        # start the threads
        for thread in self.threads:
            thread.start()

    def update_textbox(self, index, min, max, increment):
        while True:
            # generate a random number in the specified range
            number = random.randint(min, max)

            # update the text box
            self.textboxes[index].config(text=str(number))

            # sleep for the specified time
            time.sleep(increment)


root = tk.Tk()
dashboard = Dashboard(root)
root.mainloop()
