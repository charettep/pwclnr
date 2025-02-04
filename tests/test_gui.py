import unittest
import tkinter as tk
import threading

def start_gui():
    try:
        from gui import gui  # assuming gui.py contains a function to start the GUI or just runs when imported
    except Exception as e:
        raise e

class TestGUI(unittest.TestCase):
    def test_gui_initialization(self):
        # Run the GUI in a separate thread and close it immediately to test init.
        def run():
            root = tk.Tk()
            root.title("Test GUI")
            # ...existing GUI logic...
            root.after(500, root.destroy)
            root.mainloop()
        thread = threading.Thread(target=run)
        thread.start()
        thread.join(timeout=2)
        self.assertFalse(thread.is_alive())

if __name__ == '__main__':
    unittest.main()
