from tkinter import *
from functools import partial # To prevent unwanted windows

# import all_constants as c


class StartGame():
    """
    Temperature conversion tool (℃ to ℉ or ℉ to ℃)
    """

    def __init__(self):
        """
        Game Start GUI
        """

        self.game_frame = Frame(padx=10, pady=10, bg="#DAE8FC")
        self.game_frame.grid()

        self.temp_heading = Label(self.game_frame,
                                  text="Colour Quest",
                                  font=("Arial", "16", "bold"),
                                  bg="#DAE8FC",
                                  )
        self.temp_heading.grid(row=0)

        instructions = "In each round you will be invited to choose a colour. " \
                       "Your goal is to beat the target score and win the round " \
                       "(and keep your points). \n\n" \
                       "To begin, please choose how many rounds you'd like to play."

        self.colour_instructions = Label(self.game_frame,
                                         text=instructions,
                                         wraplength=250, width=40,
                                         justify="left", bg="#DAE8FC")
        self.colour_instructions.grid(row=1)

        error = "Please enter a number"
        self.answer_error = Label(self.game_frame, text=error, fg="#004C99", bg="#DAE8FC", font=("Arial", "10", "bold"))
        self.answer_error.grid(row=2)

        self.round_entry = Entry(self.game_frame,
                                 font=("Arial", "20"),
                                 bg="#FFFFFF"
                                 )
        self.round_entry.grid(row=3, padx=10, pady=10)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.game_frame, bg="#DAE8FC")
        self.button_frame.grid(row=4)

        self.play_button = Button(self.button_frame,
                                  text="Play!", bg="#0057D8",
                                  fg="#ffffff", font=("Arial", "12", "bold"),
                                  width=12)
        self.play_button.grid(row=0, padx=5, pady=5)

        self.check_int()

    def check_rounds(self):
        """
        Checks temperature is valid and either invokes calculation function or shows a custom error
        """
        # Retrieve temperature to be converted
        to_check = self.round_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99")
        self.round_entry.config(bg="#FFFFFF")

        # Checks that amount to be converted is a number above absolute zero
        try:
            to_check = int(to_check)
            if to_check <= 0:
                error = ""

            else:
                error = "Too Low!"

        except ValueError:
            error = "Oops - Please choose a whole number more than zero!"

        # Display the error if frequency
        if error != "":
            self.answer_error.config(text=error, fg="#990000")
            self.round_entry.config(bg="#F4CCCC")
            self.round_entry.delete(0, END)

        else:
            self.answer_error.config(text="OK!")
            self.round_entry.delete(0, END)


# Main Routine 
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Converter()
    root.mainloop()
