"""
This file is the entry point of the application. When run directly, it launches the GUI.
"""

from gui import launch_gui  # Import the function that initializes and runs our GUI

# If this file is executed (rather than imported), run the launch_gui() function
if __name__ == "__main__":
    # Call the GUI's launch function, which starts the Tkinter loop
    launch_gui()
