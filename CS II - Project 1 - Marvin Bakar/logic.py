# Program functions - fixmes are additions
# FIXME: Clear lineEdit entries in pages right after submit button succeeds - not necessary, but adds clarity
# FIXME: Checks so if on last student entry (5th entry), to jump to Summary page after scores is retrieved
# FIXME: change page_Summary_SETUP setText call fonts

from PyQt6.QtWidgets import *
from gui import *
from page_change_functions import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.student_name: str = "-" # Initializes student name
        self.num_of_students: int = 0 # Initializes number of students (1-5)

        self.score1: int = 0  # Initializes score #1 (0-100)
        self.score2: int or str = 0  # Initializes score #2 (0-100)
        self.score2_alt: str = "-"  # Initializes score #2 alternative
        self.score3: int or str = 0  # Initializes score #3 (0-100)
        self.score3_alt: str = "-"  # Initializes score #3 alternative
        self.score4: int or str = 0  # Initializes score #4 (0-100)
        self.score4_alt: str = "-"  # Initializes score #4 alternative
        self.score5: int or str = 0  # Initializes score #5 (0-100)
        self.score5_alt: str = "-"  # Initializes score #5 alternative
        # "self.score1_alt" doesn't exist because there will always be at least one score

        self.num_of_attempts: int = 0  # Initializes number of attempts (for average calc) (1-5)
        self.lowest_score: int = 0  # Initializes lowest score (0-100)
        self.highest_score: int = 0  # Initializes highest score (0-100)
        self.average_score: float = 0.00  # Initializes average score (0.00-100.0)
        self.final_grade: int = 0  # Initializes final grade (highest grade) (0-100)

        self.student_names_scores_entries_current = 0 # Initializes the current amount of student names/scores entries
        self.student_names_scores_entries_max = 5 # Initializes the max amount of student names/scores entries

        self.csv_header: int = 0 # Initializes if csv header was already written (max = 1)
        self.csv_written_for_current_student: bool = False # Has the current students stats been written yet
        self.stud_name_headtext: str = "Student Name" # Student Name CSV header text
        self.score1_headtext: str = "Score #1" # Score #1 CSV header text
        self.score2_headtext: str = "Score #2" # Score #2 CSV header text
        self.score3_headtext: str = "Score #3" # Score #3 CSV header text
        self.score4_headtext: str = "Score #4" # Score #4 CSV header text
        self.score5_headtext: str = "Score #5" # Score #5 CSV header text
        self.num_of_attempts_headtext: str = "# of Attempts" # Num of Attempts CSV header text
        self.lowest_score_headtext: str = "Lowest Grade" # Lowest Grade CSV header text
        self.highest_score_headtext: str = "Highest Grade" # Highest Grade CSV header text
        self.average_score_headtext: str = "Average Grade" # Average Grade CSV header text
        self.final_grade_headtext: str = "Final Grade" # Final Grade CSV header text



        # Start Program
        self.page_Home_SETUP()

        # Page "More_Students" buttons' behaviors placed here to avoid student_names_scores_entries_current increment stacking
        self.pushButton_More_Students_yes_1.clicked.connect(self.on_button_More_Students_1)
        self.pushButton_More_Students_no_1.clicked.connect(self.on_button_More_Students_2)


# -----------------------------------------------------------------------------------------------------------------
    # Page SETUP Functions

    def page_Home_SETUP(self) -> None:
        '''
        Sets up page named "Home" (Page #1 - Index #0)
        and starts program

        :return: None
        '''
        self.setFocus()  # Makes so that the line input isn't automatically focused
        self.label_Home_error_message_1.hide()  # Hides error message label
        self.pushButton_Home_submit_1.clicked.connect(lambda: self.on_button_Home_1()) # When 'Submit' is clicked


    def page_Attempts_SETUP(self) -> None:
        '''
        Sets up page named "Attempts" (Page #2 - Index #1)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        self.label_Attempts_name_change_1.hide() # Hides "Name Change:" label
        self.lineEdit_Attempts_name_change_1.hide() # Hides name change line edit
        self.pushButton_Attempts_submit_1.hide()  # Hides name change submit button
        self.label_Attempts_error_message_1.hide()  # Hides error message label 1
        self.label_Attempts_error_message_2.hide()  # Hides error message label 2
        self.label_Attempts_stud_name_var_1.setText(f"[{self.student_name}]") # Changes '[STUDENT NAME]' to '[student_name]'
        self.pushButton_Attempts_change_1.clicked.connect(lambda: self.on_button_Attempts_1()) # When 'Click to Change' is clicked
        self.pushButton_Attempts_submit_2.clicked.connect(lambda: self.on_button_Attempts_3()) # When main 'Submit' is clicked


    def page_Scores_Entry_1_SETUP(self):
        '''
        Sets up page named "Scores_Entry_1" (Page #3 - Index #2)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        self.label_Scores_Entry_1_attempts_change_2.hide()  # Hides "Attempts Change:" label
        self.lineEdit_Scores_Entry_1_attempts_change_1.hide()  # Hides attempts change line edit
        self.pushButton_Scores_Entry_1_submit_1.hide()  # Hides attempts change submit button
        self.label_Scores_Entry_1_error_message_1.hide()  # Hides error message label 1
        self.label_Scores_Entry_1_error_message_2.hide()  # Hides error message label 2
        self.label_Scores_Entry_1_attempts_var_1.setText(f"[{self.num_of_attempts}]") # Changes '[ATTEMPTS]' to '[num_of_attempts]'
        self.label_Scores_Entry_1_ent_stud_name_1.setText(f"Enter [{self.student_name}]'s") # Changes "Enter [STUDENT NAME]'s" to "Enter [student_name]'s"
        self.pushButton_Scores_Entry_1_change_1.clicked.connect(lambda: self.on_button_Scores_Entry_1_1()) # When 'Click to Change' is clicked
        self.pushButton_Scores_Entry_1_submit_2.clicked.connect(lambda: self.on_button_Scores_Entry_1_3()) # When 'Submit' is clicked


    def page_Scores_Entry_2_SETUP(self):
        '''
        Sets up page named "Scores_Entry_2" (Page #4 - Index #3)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        self.label_Scores_Entry_2_attempts_change_2.hide()  # Hides "Attempts Change:" label
        self.lineEdit_Scores_Entry_2_attempts_change_1.hide()  # Hides attempts change line edit
        self.pushButton_Scores_Entry_2_submit_1.hide()  # Hides attempts change submit button
        self.label_Scores_Entry_2_error_message_1.hide()  # Hides error message label 1
        self.label_Scores_Entry_2_error_message_2.hide()  # Hides error message label 2
        self.label_Scores_Entry_2_attempts_var_1.setText(f"[{self.num_of_attempts}]") # Changes '[ATTEMPTS]' to '[num_of_attempts]'
        self.label_Scores_Entry_2_ent_stud_name_1.setText(f"Enter [{self.student_name}]'s") # Changes "Enter [STUDENT NAME]'s" to "Enter [student_name]'s"
        self.pushButton_Scores_Entry_2_change_1.clicked.connect(lambda: self.on_button_Scores_Entry_2_1()) # When 'Click to Change' is clicked
        self.pushButton_Scores_Entry_2_submit_2.clicked.connect(lambda: self.on_button_Scores_Entry_2_3()) # When 'Submit' is clicked


    def page_Scores_Entry_3_SETUP(self):
        '''
        Sets up page named "Scores_Entry_3" (Page #5 - Index #4)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        self.label_Scores_Entry_3_attempts_change_2.hide()  # Hides "Attempts Change:" label
        self.lineEdit_Scores_Entry_3_attempts_change_1.hide()  # Hides attempts change line edit
        self.pushButton_Scores_Entry_3_submit_1.hide()  # Hides attempts change submit button
        self.label_Scores_Entry_3_error_message_1.hide()  # Hides error message label 1
        self.label_Scores_Entry_3_error_message_2.hide()  # Hides error message label 2
        self.label_Scores_Entry_3_attempts_var_1.setText(f"[{self.num_of_attempts}]") # Changes '[ATTEMPTS]' to '[num_of_attempts]'
        self.label_Scores_Entry_3_ent_stud_name_1.setText(f"Enter [{self.student_name}]'s") # Changes "Enter [STUDENT NAME]'s" to "Enter [student_name]'s"
        self.pushButton_Scores_Entry_3_change_1.clicked.connect(lambda: self.on_button_Scores_Entry_3_1()) # When 'Click to Change' is clicked
        self.pushButton_Scores_Entry_3_submit_2.clicked.connect(lambda: self.on_button_Scores_Entry_3_3()) # When 'Submit' is clicked


    def page_Scores_Entry_4_SETUP(self):
        '''
        Sets up page named "Scores_Entry_4" (Page #6 - Index #5)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        self.label_Scores_Entry_4_attempts_change_2.hide()  # Hides "Attempts Change:" label
        self.lineEdit_Scores_Entry_4_attempts_change_1.hide()  # Hides attempts change line edit
        self.pushButton_Scores_Entry_4_submit_1.hide()  # Hides attempts change submit button
        self.label_Scores_Entry_4_error_message_1.hide()  # Hides error message label 1
        self.label_Scores_Entry_4_error_message_2.hide()  # Hides error message label 2
        self.label_Scores_Entry_4_attempts_var_1.setText(f"[{self.num_of_attempts}]") # Changes '[ATTEMPTS]' to '[num_of_attempts]'
        self.label_Scores_Entry_4_ent_stud_name_1.setText(f"Enter [{self.student_name}]'s") # Changes "Enter [STUDENT NAME]'s" to "Enter [student_name]'s"
        self.pushButton_Scores_Entry_4_change_1.clicked.connect(lambda: self.on_button_Scores_Entry_4_1()) # When 'Click to Change' is clicked
        self.pushButton_Scores_Entry_4_submit_2.clicked.connect(lambda: self.on_button_Scores_Entry_4_3()) # When 'Submit' is clicked


    def page_Scores_Entry_5_SETUP(self):
        '''
        Sets up page named "Scores_Entry_5" (Page #7 - Index #6)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        self.label_Scores_Entry_5_attempts_change_2.hide()  # Hides "Attempts Change:" label
        self.lineEdit_Scores_Entry_5_attempts_change_1.hide()  # Hides attempts change line edit
        self.pushButton_Scores_Entry_5_submit_1.hide()  # Hides attempts change submit button
        self.label_Scores_Entry_5_error_message_1.hide()  # Hides error message label 1
        self.label_Scores_Entry_5_error_message_2.hide()  # Hides error message label 2
        self.label_Scores_Entry_5_attempts_var_1.setText(f"[{self.num_of_attempts}]") # Changes '[ATTEMPTS]' to '[num_of_attempts]'
        self.label_Scores_Entry_5_ent_stud_name_1.setText(f"Enter [{self.student_name}]'s") # Changes "Enter [STUDENT NAME]'s" to "Enter [student_name]'s"
        self.pushButton_Scores_Entry_5_change_1.clicked.connect(lambda: self.on_button_Scores_Entry_5_1()) # When 'Click to Change' is clicked
        self.pushButton_Scores_Entry_5_submit_2.clicked.connect(lambda: self.on_button_Scores_Entry_5_3()) # When 'Submit' is clicked


    def page_More_Students_SETUP(self):
        '''
        Sets up page named "More_Students" (Page #8 - Index #7)

        :return: None
        '''
        self.setFocus()  # Makes so that the line inputs aren't automatically focused
        # Page "More_Students" buttons' behaviors moved to __init__

        # Writes to CSV File
        self.which_csv_write()


    def page_Home_No_Welcome_SETUP(self):
        '''
        Sets up page named "Home_No_Welcome" (Page #9 - Index #8)

        :return: None
        '''
        self.setFocus()  # Makes so that the line input isn't automatically focused
        self.label_Home_No_Welcome_error_message_1.hide()  # Hides error message label
        self.pushButton_Home_No_Welcome_submit_1.clicked.connect(lambda: self.on_button_Home_No_Welcome_1()) # When 'Submit' is clicked


    def page_Summary_SETUP(self):
        '''
        Sets up page named "Summary" (Page #10 - Index #9)

        :return: None
        '''
        if self.student_names_scores_entries_current == 1:
            self.label_Summary_studA_var_1.setText(f"[{self.student_name}]")
            self.textBrowser_Summary_studA_sum_box_1.setText(f"Lowest = [{self.lowest_score}], "
                                                             f"Highest = [{self.highest_score}], "
                                                             f"Average = [{self.average_score}]\n"
                                                             f"Final Grade = [{self.final_grade}]")
        elif self.student_names_scores_entries_current == 2:
            self.label_Summary_studB_var_1.setText(f"[{self.student_name}]")
            self.textBrowser_Summary_studB_sum_box_1.setText(f"Lowest = [{self.lowest_score}], "
                                                             f"Highest = [{self.highest_score}], "
                                                             f"Average = [{self.average_score}]\n"
                                                             f"Final Grade = [{self.final_grade}]")
        elif self.student_names_scores_entries_current == 3:
            self.label_Summary_studC_var_1.setText(f"[{self.student_name}]")
            self.textBrowser_Summary_studC_sum_box_1.setText(f"Lowest = [{self.lowest_score}], "
                                                             f"Highest = [{self.highest_score}], "
                                                             f"Average = [{self.average_score}]\n"
                                                             f"Final Grade = [{self.final_grade}]")
        elif self.student_names_scores_entries_current == 4:
            self.label_Summary_studD_var_1.setText(f"[{self.student_name}]")
            self.textBrowser_Summary_studD_sum_box_1.setText(f"Lowest = [{self.lowest_score}], "
                                                             f"Highest = [{self.highest_score}], "
                                                             f"Average = [{self.average_score}]\n"
                                                             f"Final Grade = [{self.final_grade}]")
        elif self.student_names_scores_entries_current == 5:
            self.label_Summary_studE_var_1.setText(f"[{self.student_name}]")
            self.textBrowser_Summary_studE_sum_box_1.setText(f"Lowest = [{self.lowest_score}], "
                                                             f"Highest = [{self.highest_score}], "
                                                             f"Average = [{self.average_score}]\n"
                                                             f"Final Grade = [{self.final_grade}]")
# -----------------------------------------------------------------------------------------------------------------

    # Order of operations

    def on_button_Home_1(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Home"
        Goes through student_name_check1()
        If succeeds, hides error message
        If succeeds, saves text_input to self.student_name
        If succeeds, goes through page_change_Attempts()
        If succeeds, goes through page_Attempts_SETUP()
        If fails, shows error message

        :return: None
        '''
        text_input: str = self.lineEdit_Home_stud_name_input_1.text().strip()
        try:
            self.student_name_check_1(text_input)
            self.label_Home_error_message_1.hide()
            self.student_name = text_input
            page_change_Attempts(self)
            self.page_Attempts_SETUP()

        except ValueError:
            self.label_Home_error_message_1.show()


    def student_name_check_1(self, text_input: str) -> None:
        '''
        Checks to see if user's student name input is
        valid (no blanks entries, no numbers, must be a
        string, must be less than or equal to 25 characters)

        :return: None
        '''
        max_length = 25

        if not text_input: # If text_input is empty
            self.label_Home_error_message_1.setText(f"Name box can't be empty!")
            raise ValueError
        if len(text_input) > max_length: # If text_input is larger than 25 characters
            self.label_Home_error_message_1.setText(f"Name is too long, please abbreviate!")
            raise ValueError()
        for char in text_input: # If text_input is numbers/has a number(s)
            if char.isdigit():
                self.label_Home_error_message_1.setText(f"Wrong datatype! Enter a name")
                raise ValueError


    def on_button_Attempts_1(self) -> None:
        '''
        Behavior of 'Click to change' button for page named "Attempts"
        Goes through on_button_click3()
        :return: None
        '''
        self.label_Attempts_name_change_1.show()  # Shows "Name Change:" label
        self.lineEdit_Attempts_name_change_1.show()  # Shows name change line edit
        self.pushButton_Attempts_submit_1.show()  # Shows name change submit button
        self.pushButton_Attempts_submit_1.clicked.connect(lambda: self.on_button_Attempts_2()) # When 'Submit' regarding name change is clicked


    def on_button_Attempts_2(self) -> None:
        '''
        Behavior of 'Submit' button regarding name change for page named "Attempts"
        Goes through student_name_check2()
        If succeeds, hides error message
        If succeeds, saves text_input to name_change to self.student_name
        If succeeds, updates GUI with self.student_name
        If fails, shows error message
        :return: None
        '''
        name_change: str = "-"
        text_input: str = self.lineEdit_Attempts_name_change_1.text().strip()
        try:
            self.student_name_check_2(text_input)
            self.label_Attempts_error_message_2.hide()
            name_change = text_input
            self.student_name = name_change
            self.label_Attempts_stud_name_var_1.setText(f"[{self.student_name}]") # Changes '[STUDENT NAME]' to new '[student_name]'

        except ValueError:
            self.label_Attempts_error_message_2.show()  # Shows error message label for name change


    def student_name_check_2(self, text_input: str) -> None:
        '''
        Checks to see if user's student name input is
        valid (no blanks entries, no numbers, must be a
        string, must be equal or less than 60 characters)
        Different from student_name_check_1 due to error messages

        :return: None
        '''
        max_length = 25

        if not text_input: # If text_input is empty
            self.label_Attempts_error_message_2.setText(f"Name box can't be empty!")
            raise ValueError
        if len(text_input) > max_length: # If text_input is larger than 25 characters
            self.label_Attempts_error_message_2.setText(f"Name is too long, please abbreviate!")
            raise ValueError()
        for char in text_input: # If text_input is numbers/has a number(s)
            if char.isdigit():
                self.label_Attempts_error_message_2.setText(f"Wrong datatype! Enter a name")
                raise ValueError


    def on_button_Attempts_3(self) -> None:
        '''
        Behavior of main 'Submit' button for page named "Attempts"
        Goes through attempts_check_1()
        If succeeds, saves text_input to num_of_attempts
        If succeeds, hides error message
        If succeeds, goes through which_Scores_Entries_page()
        If succeeds, goes through which_Scores_Entries_SETUP()
        If fails, shows error message

        :return: None
        '''
        text_input = self.lineEdit_Attempts_num_of_attempts_1.text().strip()
        try:
            self.num_of_attempts = self.attempts_check_1(text_input)
            self.label_Attempts_error_message_1.hide()
            which_Scores_Entries_page(self)
            self.which_Scores_Entries_SETUP()

        except ValueError:
            self.label_Attempts_error_message_1.show()


    def attempts_check_1(self, text_input: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 1-5)

        :param text_input: The text_input variable
        :return: int
        '''
        valid_attempts_list = [1, 2, 3, 4, 5]

        if not text_input.isdigit():
            self.label_Attempts_error_message_1.setText("Wrong datatype! Enter a number (1-5)")
            raise ValueError

        converted_attempts = int(text_input)

        if converted_attempts not in valid_attempts_list:
            self.label_Attempts_error_message_1.setText("Enter a number (1-5)")
            raise ValueError

        return converted_attempts


    def which_Scores_Entries_SETUP(self) -> None:
        '''
        Chooses a Score Entries SETUP function according to value of num_of_attempts

        :return: None
        '''
        if self.num_of_attempts == 1:
            self.page_Scores_Entry_1_SETUP()
        elif self.num_of_attempts == 2:
            self.page_Scores_Entry_2_SETUP()
        elif self.num_of_attempts == 3:
            self.page_Scores_Entry_3_SETUP()
        elif self.num_of_attempts == 4:
            self.page_Scores_Entry_4_SETUP()
        elif self.num_of_attempts == 5:
            self.page_Scores_Entry_5_SETUP()


    def on_button_Scores_Entry_1_1(self) -> None:
        '''
        Behavior of 'Click to change' button for page named "Scores_Entry_1"
        Goes through on_button_Scores_Entry_1_2()

        :return: None
        '''
        self.label_Scores_Entry_1_attempts_change_2.show()  # Shows "Attempts Change:" label
        self.lineEdit_Scores_Entry_1_attempts_change_1.show()  # Shows attempts change line edit
        self.pushButton_Scores_Entry_1_submit_1.show()  # Shows attempts change submit button
        self.pushButton_Scores_Entry_1_submit_1.clicked.connect(lambda: self.on_button_Scores_Entry_1_2()) # When 'Submit' regarding attempts change is clicked



    def on_button_Scores_Entry_1_2(self) -> None:
        '''
        Behavior of 'Submit' button regarding attempts change for page named "Scores_Entry_1"
        Goes through attempts_check_2()
        If succeeds, sees if new_num_of_attempts isn't equal to num_of_attempts
        If succeeds, self.num_of_attempts gets new_num_of_attempts value
        If succeeds, updates GUI with self.student_name
        If fails, shows error message

        :return: None
        '''
        new_num_of_attempts: int = 0
        text_input = self.lineEdit_Scores_Entry_1_attempts_change_1.text().strip()
        try:
            new_num_of_attempts = self.attempts_check_2(text_input)
            if new_num_of_attempts != self.num_of_attempts:
                self.num_of_attempts = new_num_of_attempts
                self.label_Scores_Entry_1_error_message_2.hide()
                which_Scores_Entries_page(self)
                self.which_Scores_Entries_SETUP()
            else:
                self.label_Scores_Entry_1_error_message_2.setText(f"Attempts is already {new_num_of_attempts}")
                raise ValueError

        except ValueError:
            self.label_Scores_Entry_1_error_message_2.show()


    def attempts_check_2(self, text_input: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 1-5)
        Different from attempts_check_1 due to error messages

        :param text_input: The text_input variable
        :return: int
        '''
        valid_attempts_list = [1, 2, 3, 4, 5]

        if not text_input.isdigit():
            self.label_Scores_Entry_1_error_message_2.setText("Wrong datatype! Enter a number (1-5)")
            raise ValueError

        converted_attempts = int(text_input)

        if converted_attempts not in valid_attempts_list:
            self.label_Scores_Entry_1_error_message_2.setText("Enter a number (1-5)")
            raise ValueError

        return converted_attempts


    def on_button_Scores_Entry_2_1(self) -> None:
        '''
        Behavior of 'Click to change' button for page named "Scores_Entry_2"
        Goes through on_button_Scores_Entry_2_2()

        :return: None
        '''
        self.label_Scores_Entry_2_attempts_change_2.show()  # Shows "Attempts Change:" label
        self.lineEdit_Scores_Entry_2_attempts_change_1.show()  # Shows attempts change line edit
        self.pushButton_Scores_Entry_2_submit_1.show()  # Shows attempts change submit button
        self.pushButton_Scores_Entry_2_submit_1.clicked.connect(lambda: self.on_button_Scores_Entry_2_2()) # When 'Submit' regarding attempts change is clicked


    def on_button_Scores_Entry_2_2(self) -> None:
        '''
        Behavior of 'Submit' button regarding attempts change for page named "Scores_Entry_2"
        Goes through attempts_check_3()
        If succeeds, sees if new_num_of_attempts isn't equal to num_of_attempts
        If succeeds, self.num_of_attempts gets new_num_of_attempts value
        If succeeds, updates GUI with self.student_name
        If fails, shows error message

        :return: None
        '''
        new_num_of_attempts: int = 0
        text_input = self.lineEdit_Scores_Entry_2_attempts_change_1.text().strip()
        try:
            new_num_of_attempts = self.attempts_check_3(text_input)
            if new_num_of_attempts != self.num_of_attempts:
                self.num_of_attempts = new_num_of_attempts
                self.label_Scores_Entry_1_error_message_2.hide()
                which_Scores_Entries_page(self)
                self.which_Scores_Entries_SETUP()
            else:
                self.label_Scores_Entry_2_error_message_2.setText(f"Attempts is already {new_num_of_attempts}")
                raise ValueError

        except ValueError:
            self.label_Scores_Entry_2_error_message_2.show()


    def attempts_check_3(self, text_input: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 1-5)
        Different from previous attempts_checks due to error messages

        :param text_input: The text_input variable
        :return: int
        '''
        valid_attempts_list = [1, 2, 3, 4, 5]

        if not text_input.isdigit():
            self.label_Scores_Entry_2_error_message_2.setText("Wrong datatype! Enter a number (1-5)")
            raise ValueError

        converted_attempts = int(text_input)

        if converted_attempts not in valid_attempts_list:
            self.label_Scores_Entry_2_error_message_2.setText("Enter a number (1-5)")
            raise ValueError

        return converted_attempts


    def on_button_Scores_Entry_3_1(self) -> None:
        '''
        Behavior of 'Click to change' button for page named "Scores_Entry_3"
        Goes through on_button_Scores_Entry_3_2()

        :return: None
        '''
        self.label_Scores_Entry_3_attempts_change_2.show()  # Shows "Attempts Change:" label
        self.lineEdit_Scores_Entry_3_attempts_change_1.show()  # Shows attempts change line edit
        self.pushButton_Scores_Entry_3_submit_1.show()  # Shows attempts change submit button
        self.pushButton_Scores_Entry_3_submit_1.clicked.connect(lambda: self.on_button_Scores_Entry_3_2()) # When 'Submit' regarding attempts change is clicked


    def on_button_Scores_Entry_3_2(self) -> None:
        '''
        Behavior of 'Submit' button regarding attempts change for page named "Scores_Entry_3"
        Goes through attempts_check_4()
        If succeeds, sees if new_num_of_attempts isn't equal to num_of_attempts
        If succeeds, self.num_of_attempts gets new_num_of_attempts value
        If succeeds, updates GUI with self.student_name
        If fails, shows error message

        :return: None
        '''
        new_num_of_attempts: int = 0
        text_input = self.lineEdit_Scores_Entry_3_attempts_change_1.text().strip()
        try:
            new_num_of_attempts = self.attempts_check_4(text_input)
            if new_num_of_attempts != self.num_of_attempts:
                self.num_of_attempts = new_num_of_attempts
                self.label_Scores_Entry_3_error_message_2.hide()
                which_Scores_Entries_page(self)
                self.which_Scores_Entries_SETUP()
            else:
                self.label_Scores_Entry_3_error_message_2.setText(f"Attempts is already {new_num_of_attempts}")
                raise ValueError

        except ValueError:
            self.label_Scores_Entry_3_error_message_2.show()


    def attempts_check_4(self, text_input: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 1-5)
        Different from previous attempts_checks due to error messages

        :param text_input: The text_input variable
        :return: int
        '''
        valid_attempts_list = [1, 2, 3, 4, 5]

        if not text_input.isdigit():
            self.label_Scores_Entry_3_error_message_2.setText("Wrong datatype! Enter a number (1-5)")
            raise ValueError

        converted_attempts = int(text_input)

        if converted_attempts not in valid_attempts_list:
            self.label_Scores_Entry_3_error_message_2.setText("Enter a number (1-5)")
            raise ValueError

        return converted_attempts


    def on_button_Scores_Entry_4_1(self) -> None:
        '''
        Behavior of 'Click to change' button for page named "Scores_Entry_4"
        Goes through on_button_Scores_Entry_4_2()

        :return: None
        '''
        self.label_Scores_Entry_4_attempts_change_2.show()  # Shows "Attempts Change:" label
        self.lineEdit_Scores_Entry_4_attempts_change_1.show()  # Shows attempts change line edit
        self.pushButton_Scores_Entry_4_submit_1.show()  # Shows attempts change submit button
        self.pushButton_Scores_Entry_4_submit_1.clicked.connect(lambda: self.on_button_Scores_Entry_4_2()) # When 'Submit' regarding attempts change is clicked


    def on_button_Scores_Entry_4_2(self) -> None:
        '''
        Behavior of 'Submit' button regarding attempts change for page named "Scores_Entry_4"
        Goes through attempts_check_5()
        If succeeds, sees if new_num_of_attempts isn't equal to num_of_attempts
        If succeeds, self.num_of_attempts gets new_num_of_attempts value
        If succeeds, updates GUI with self.student_name
        If fails, shows error message

        :return: None
        '''
        new_num_of_attempts: int = 0
        text_input = self.lineEdit_Scores_Entry_4_attempts_change_1.text().strip()
        try:
            new_num_of_attempts = self.attempts_check_5(text_input)
            if new_num_of_attempts != self.num_of_attempts:
                self.num_of_attempts = new_num_of_attempts
                self.label_Scores_Entry_4_error_message_2.hide()
                which_Scores_Entries_page(self)
                self.which_Scores_Entries_SETUP()
            else:
                self.label_Scores_Entry_4_error_message_2.setText(f"Attempts is already {new_num_of_attempts}")
                raise ValueError

        except ValueError:
            self.label_Scores_Entry_4_error_message_2.show()


    def attempts_check_5(self, text_input: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 1-5)
        Different from previous attempts_checks due to error messages

        :param text_input: The text_input variable
        :return: int
        '''
        valid_attempts_list = [1, 2, 3, 4, 5]

        if not text_input.isdigit():
            self.label_Scores_Entry_4_error_message_2.setText("Wrong datatype! Enter a number (1-5)")
            raise ValueError

        converted_attempts = int(text_input)

        if converted_attempts not in valid_attempts_list:
            self.label_Scores_Entry_4_error_message_2.setText("Enter a number (1-5)")
            raise ValueError

        return converted_attempts


    def on_button_Scores_Entry_5_1(self) -> None:
        '''
        Behavior of 'Click to change' button for page named "Scores_Entry_5"
        Goes through on_button_Scores_Entry_5_2()

        :return: None
        '''
        self.label_Scores_Entry_5_attempts_change_2.show()  # Shows "Attempts Change:" label
        self.lineEdit_Scores_Entry_5_attempts_change_1.show()  # Shows attempts change line edit
        self.pushButton_Scores_Entry_5_submit_1.show()  # Shows attempts change submit button
        self.pushButton_Scores_Entry_5_submit_1.clicked.connect(lambda: self.on_button_Scores_Entry_5_2()) # When 'Submit' regarding attempts change is clicked


    def on_button_Scores_Entry_5_2(self) -> None:
        '''
        Behavior of 'Submit' button regarding attempts change for page named "Scores_Entry_5"
        Goes through attempts_check_6()
        If succeeds, sees if new_num_of_attempts isn't equal to num_of_attempts
        If succeeds, self.num_of_attempts gets new_num_of_attempts value
        If succeeds, updates GUI with self.student_name
        If fails, shows error message

        :return: None
        '''
        new_num_of_attempts: int = 0
        text_input = self.lineEdit_Scores_Entry_5_attempts_change_1.text().strip()
        try:
            new_num_of_attempts = self.attempts_check_6(text_input)
            if new_num_of_attempts != self.num_of_attempts:
                self.num_of_attempts = new_num_of_attempts
                self.label_Scores_Entry_5_error_message_2.hide()
                which_Scores_Entries_page(self)
                self.which_Scores_Entries_SETUP()
            else:
                self.label_Scores_Entry_5_error_message_2.setText(f"Attempts is already {new_num_of_attempts}")
                raise ValueError

        except ValueError:
            self.label_Scores_Entry_5_error_message_2.show()


    def attempts_check_6(self, text_input: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 1-5)
        Different from previous attempts_checks due to error messages

        :param text_input: The text_input variable
        :return: int
        '''
        valid_attempts_list = [1, 2, 3, 4, 5]

        if not text_input.isdigit():
            self.label_Scores_Entry_5_error_message_2.setText("Wrong datatype! Enter a number (1-5)")
            raise ValueError

        converted_attempts = int(text_input)

        if converted_attempts not in valid_attempts_list:
            self.label_Scores_Entry_5_error_message_2.setText("Enter a number (1-5)")
            raise ValueError

        return converted_attempts


    def on_button_Scores_Entry_1_3(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Scores_Entry_1"
        Goes through scores_check_1()
        If succeeds, hides error message
        If succeeds, saves converted score(s) to corresponding score var(s) for csv prep
        If succeeds, goes through page_change_More_Students()
        If succeeds, goes through page_More_Students_SETUP()
        If fails, shows error message

        :return: None
        '''
        t_i_1 = self.lineEdit_Scores_Entry_1_score_one_1.text().strip()
        try:
            self.score1 = self.scores_check_1(t_i_1)
            self.score2 = self.score2_alt
            self.score3 = self.score3_alt
            self.score4 = self.score4_alt
            self.score5 = self.score5_alt
            self.label_Scores_Entry_1_error_message_1.hide()
            self.compute_stats()
            page_change_More_Students(self)
            self.page_More_Students_SETUP()

        except ValueError:
            self.label_Scores_Entry_1_error_message_1.show()


    def scores_check_1(self, t_i_1: str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 0-100)
        Different from previous attempts_checks due to error messages

        :param t_i_1: The user text inputs
        :return: int
        '''
        if t_i_1 == "":
            self.label_Scores_Entry_1_error_message_1.setText("Entry cannot be blank!")
            raise ValueError
        if not t_i_1.isdigit():
            self.label_Scores_Entry_1_error_message_1.setText("Wrong datatype! Enter a number (0-100)")
            raise ValueError

        converted_score1 = int(t_i_1)

        if converted_score1 < 0 or converted_score1 > 100:
            self.label_Scores_Entry_1_error_message_1.setText("Enter a number between 0 and 100")
            raise ValueError

        return converted_score1


    def on_button_Scores_Entry_2_3(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Scores_Entry_2"
        Goes through scores_check_2()
        If succeeds, hides error message
        If succeeds, saves converted score(s) to corresponding score var(s) for csv prep
        If succeeds, goes through page_change_More_Students()
        If succeeds, goes through page_More_Students_SETUP()
        If fails, shows error message

        :return: None
        '''
        t_i_1 = self.lineEdit_Scores_Entry_2_score_one_1.text().strip()
        t_i_2 = self.lineEdit_Scores_Entry_2_score_two_1.text().strip()
        try:
            self.score1, self.score2 = self.scores_check_2(t_i_1, t_i_2)
            self.score3 = self.score3_alt
            self.score4 = self.score4_alt
            self.score5 = self.score5_alt
            self.label_Scores_Entry_1_error_message_1.hide()
            self.compute_stats()
            page_change_More_Students(self)
            self.page_More_Students_SETUP()

        except ValueError:
            self.label_Scores_Entry_2_error_message_1.show()


    def scores_check_2(self, t_i_1:str, t_i_2:str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 0-100)
        Different from previous attempts_checks due to error messages

        :param t_i_1: The user text input
        :param t_i_2: The user text input
        :return: int
        '''
        for i in [t_i_1, t_i_2]:
            if i == "":
                self.label_Scores_Entry_2_error_message_1.setText("Entry cannot be blank")
                raise ValueError
            if not i.isdigit():
                self.label_Scores_Entry_2_error_message_1.setText("Wrong datatype! Enter numbers (0-100)")
                raise ValueError
            if not (0 <= int(i) <= 100):
                self.label_Scores_Entry_2_error_message_1.setText("Enter a number between 0 and 100")
                raise ValueError

        return int(t_i_1), int(t_i_2)


    def on_button_Scores_Entry_3_3(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Scores_Entry_3"
        Goes through scores_check_3()
        If succeeds, hides error message
        If succeeds, saves converted score(s) to corresponding score var(s) for csv prep
        If succeeds, goes through page_change_More_Students()
        If succeeds, goes through page_More_Students_SETUP()
        If fails, shows error message

        :return: None
        '''
        t_i_1 = self.lineEdit_Scores_Entry_3_score_one_1.text().strip()
        t_i_2 = self.lineEdit_Scores_Entry_3_score_two_1.text().strip()
        t_i_3 = self.lineEdit_Scores_Entry_3_score_three_1.text().strip()
        try:
            self.score1, self.score2, self.score3 = self.scores_check_3(t_i_1, t_i_2, t_i_3)
            self.score4 = self.score4_alt
            self.score5 = self.score5_alt
            self.label_Scores_Entry_3_error_message_1.hide()
            self.compute_stats()
            page_change_More_Students(self)
            self.page_More_Students_SETUP()

        except ValueError:
            self.label_Scores_Entry_3_error_message_1.show()


    def scores_check_3(self, t_i_1:str, t_i_2:str, t_i_3:str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 0-100)
        Different from previous attempts_checks due to error messages

        :param t_i_1: The user text input
        :param t_i_2: The user text input
        :param t_i_3: The user text input
        :return: int
        '''
        for i in [t_i_1, t_i_2, t_i_3]:
            if i == "":
                self.label_Scores_Entry_3_error_message_1.setText("Entry cannot be blank")
                raise ValueError
            if not i.isdigit():
                self.label_Scores_Entry_3_error_message_1.setText("Wrong datatype! Enter numbers (0-100)")
                raise ValueError
            if not (0 <= int(i) <= 100):
                self.label_Scores_Entry_3_error_message_1.setText("Enter a number between 0 and 100")
                raise ValueError

        return int(t_i_1), int(t_i_2), int(t_i_3)


    def on_button_Scores_Entry_4_3(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Scores_Entry_4"
        Goes through scores_check_4()
        If succeeds, hides error message
        If succeeds, saves converted score(s) to corresponding score var(s) for csv prep
        If succeeds, goes through page_change_More_Students()
        If succeeds, goes through page_More_Students_SETUP()
        If fails, shows error message

        :return: None
        '''
        t_i_1 = self.lineEdit_Scores_Entry_4_score_one_1.text().strip()
        t_i_2 = self.lineEdit_Scores_Entry_4_score_two_1.text().strip()
        t_i_3 = self.lineEdit_Scores_Entry_4_score_three_1.text().strip()
        t_i_4 = self.lineEdit_Scores_Entry_4_score_four_1.text().strip()
        try:
            self.score1, self.score2, self.score3, self.score4 = self.scores_check_4(t_i_1, t_i_2, t_i_3, t_i_4)
            self.score5 = self.score5_alt
            self.label_Scores_Entry_4_error_message_1.hide()
            self.compute_stats()
            page_change_More_Students(self)
            self.page_More_Students_SETUP()

        except ValueError:
            self.label_Scores_Entry_4_error_message_1.show()


    def scores_check_4(self, t_i_1:str, t_i_2:str, t_i_3:str, t_i_4:str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 0-100)
        Different from previous attempts_checks due to error messages

        :param t_i_1: The user text input
        :param t_i_2: The user text input
        :param t_i_3: The user text input
        :param t_i_4: The user text input
        :return: int
        '''
        for i in [t_i_1, t_i_2, t_i_3, t_i_4]:
            if i == "":
                self.label_Scores_Entry_4_error_message_1.setText("Entry cannot be blank")
                raise ValueError
            if not i.isdigit():
                self.label_Scores_Entry_4_error_message_1.setText("Wrong datatype! Enter numbers (0-100)")
                raise ValueError
            if not (0 <= int(i) <= 100):
                self.label_Scores_Entry_4_error_message_1.setText("Enter a number between 0 and 100")
                raise ValueError

        return int(t_i_1), int(t_i_2), int(t_i_3), int(t_i_4)


    def on_button_Scores_Entry_5_3(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Scores_Entry_5"
        Goes through scores_check_5()
        If succeeds, hides error message
        If succeeds, saves converted score(s) to corresponding score var(s) for csv prep
        If succeeds, goes through page_change_More_Students()
        If succeeds, goes through page_More_Students_SETUP()
        If fails, shows error message

        :return: None
        '''
        t_i_1 = self.lineEdit_Scores_Entry_5_score_one_1.text().strip()
        t_i_2 = self.lineEdit_Scores_Entry_5_score_two_1.text().strip()
        t_i_3 = self.lineEdit_Scores_Entry_5_score_three_1.text().strip()
        t_i_4 = self.lineEdit_Scores_Entry_5_score_four_1.text().strip()
        t_i_5 = self.lineEdit_Scores_Entry_5_score_five_1.text().strip()
        try:
            self.score1, self.score2, self.score3, self.score4, self.score5 = self.scores_check_5(t_i_1, t_i_2, t_i_3, t_i_4, t_i_5)
            self.label_Scores_Entry_5_error_message_1.hide()
            self.compute_stats()
            page_change_More_Students(self)
            self.page_More_Students_SETUP()

        except ValueError:
            self.label_Scores_Entry_5_error_message_1.show()


    def scores_check_5(self, t_i_1:str, t_i_2:str, t_i_3:str, t_i_4:str, t_i_5:str) -> int:
        '''
        Checks to see if user's number of attempts input is
        valid (must be a number 0-100)
        Different from previous attempts_checks due to error messages

        :param t_i_1: The user text input
        :param t_i_2: The user text input
        :param t_i_3: The user text input
        :param t_i_4: The user text input
        :param t_i_5: The user text input
        :return: int
        '''
        for i in [t_i_1, t_i_2, t_i_3, t_i_4, t_i_5]:
            if i == "":
                self.label_Scores_Entry_5_error_message_1.setText("Entry cannot be blank")
                raise ValueError
            if not i.isdigit():
                self.label_Scores_Entry_5_error_message_1.setText("Wrong datatype! Enter numbers (0-100)")
                raise ValueError
            if not (0 <= int(i) <= 100):
                self.label_Scores_Entry_5_error_message_1.setText("Enter a number between 0 and 100")
                raise ValueError

        return int(t_i_1), int(t_i_2), int(t_i_3), int(t_i_4), int(t_i_5)


    def on_button_More_Students_1(self) -> None:
        '''
        Behavior of 'Yes' button for page named "More_Students"

        :return: None
        '''
        self.student_names_scores_entries_current += 1
        self.page_Summary_SETUP()
        self.csv_written_for_current_student = False

        if self.student_names_scores_entries_current >= self.student_names_scores_entries_max:
            page_change_Summary(self)
        else:

            # Re-Initializations
            self.student_name: str = "-"  # Re-Initializes student name
            self.score1: int = 0  # Re-Initializes score #1 (0-100)
            self.score2: int or str = 0  # Re-Initializes score #2 (0-100)
            self.score3: int or str = 0  # Re-Initializes score #3 (0-100)
            self.score4: int or str = 0  # Re-Initializes score #4 (0-100)
            self.score5: int or str = 0  # Re-Initializes score #5 (0-100)
            self.lowest_score: int = 0  # Re-Initializes lowest score (0-100)
            self.highest_score: int = 0  # Re-Initializes highest score (0-100)
            self.average_score: float = 0.00  # Re-Initializes average score (0.00-100.0)
            self.final_grade: int = 0  # Re-Initializes final grade (highest grade) (0-100)

            self.page_Home_No_Welcome_SETUP()
            page_change_Home_No_Welcome(self)


    def on_button_More_Students_2(self) -> None:
        '''
        Behavior of 'No' button for page named "More_Students"

        :return: None
        '''
        self.which_csv_write()
        self.student_names_scores_entries_current += 1
        self.page_Summary_SETUP()
        page_change_Summary(self)


    def on_button_Home_No_Welcome_1(self) -> None:
        '''
        Behavior of 'Submit' button for page named "Home_No_Welcome"
        Goes through student_name_check3()
        If succeeds, hides error message
        If succeeds, saves text_input to self.student_name
        If succeeds, goes through page_change_Attempts()
        If succeeds, goes through page_Attempts_SETUP()
        If fails, shows error message

        :return: None
        '''
        text_input: str = self.lineEdit_Home_No_Welcome_stud_name_input_1.text().strip()
        try:
            self.student_name_check_3(text_input)
            self.label_Home_No_Welcome_error_message_1.hide()
            self.student_name = text_input
            page_change_Attempts(self)
            self.page_Attempts_SETUP()

        except ValueError:
            self.label_Home_No_Welcome_error_message_1.show()


    def student_name_check_3(self, text_input: str) -> None:
        '''
        Checks to see if user's student name input is
        valid (no blanks entries, no numbers, must be a
        string, must be equal or less than 60 characters)
        Different from previous student_name_checks due to error messages

        :return: None
        '''
        max_length = 25

        if not text_input:  # If text_input is empty
            self.label_Home_No_Welcome_error_message_1.setText(f"Name box can't be empty!")
            raise ValueError
        if len(text_input) > max_length:  # If text_input is larger than 25 characters
            self.label_Home_No_Welcome_error_message_1.setText(f"Name is too long, please abbreviate!")
            raise ValueError()
        for char in text_input:  # If text_input is numbers/has a number(s)
            if char.isdigit():
                self.label_Home_No_Welcome_error_message_1.setText(f"Wrong datatype! Enter a name")
                raise ValueError


    def compute_stats(self) -> None:
        '''
        Computes stats (lowest score, highest score,
        average score, and final grade) in respect to the number
        of attempts

        :return: None
        '''
        scores = [self.score1]
        if self.num_of_attempts >= 2:
            scores.append(self.score2)
        if self.num_of_attempts >= 3:
            scores.append(self.score3)
        if self.num_of_attempts >= 4:
            scores.append(self.score4)
        if self.num_of_attempts >= 5:
            scores.append(self.score5)

        self.lowest_score = min(scores)
        self.highest_score = max(scores)
        self.average_score = round(sum(scores) / len(scores), 2)
        self.final_grade = self.highest_score


    def which_csv_write(self) -> None:
        '''
        Chooses which csv writing function to use
        depending on conditions

        :return: None
        '''
        if self.csv_written_for_current_student:
            return

        if self.csv_header == 0:
            self.write_csv_header()

        self.write_csv_entries()
        self.csv_written_for_current_student = True

    def write_csv_header(self) -> None:
        '''
        Writes header and blank row to csv file

        :return: None
        '''
        with open('results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.stud_name_headtext, "-", self.score1_headtext,
                             self.score2_headtext, self.score3_headtext,
                             self.score4_headtext, self.score5_headtext, "-",
                             self.num_of_attempts_headtext, self.lowest_score_headtext,
                             self.highest_score_headtext, self.average_score_headtext,
                             self.final_grade_headtext])
            writer.writerow([])
        self.csv_header = 1


    def write_csv_entries(self) -> None:
        '''
        Writes entries to csv file

        :return: None
        '''
        with open('results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.student_name, "", self.score1,
                             self.score2, self.score3,
                             self.score4, self.score5, "",
                             self.num_of_attempts, self.lowest_score,
                             self.highest_score, self.average_score,
                             self.final_grade])
