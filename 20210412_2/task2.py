"""
Homework application task2.py.

- Functions and classes have few parameters
"""

from logic import Application


class App(Application):
	"""Main application class."""

    def create_widgets(self):
    	"""Create all widgets of this application."""
        super().create_widgets()


def show_handler(self):
	"""
        Show button handler.
    """

    self.S.set(self.SforE.get())


def main():
	"""Call main application ."""
    app = App(title="task2.py")
    app.mainloop()


if __name__ == "__main__":
    main()
