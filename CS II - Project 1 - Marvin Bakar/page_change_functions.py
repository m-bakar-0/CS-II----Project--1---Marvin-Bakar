# Page Change Functions

def page_change_Home(self) -> None:
    '''
    Changes current page to page named "Home".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(0)

def page_change_Attempts(self) -> None:
    '''
    Changes current page to page named "Attempts".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(1)

def page_change_Scores_Entry_1(self) -> None:
    '''
    Changes current page to page named "Scores_Entry_1".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(2)

def page_change_Scores_Entry_2(self) -> None:
    '''
    Changes current page to page named "Scores_Entry_2".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(3)

def page_change_Scores_Entry_3(self) -> None:
    '''
    Changes current page to page named "Scores_Entry_3".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(4)

def page_change_Scores_Entry_4(self) -> None:
    '''
    Changes current page to page named "Scores_Entry_4".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(5)

def page_change_Scores_Entry_5(self) -> None:
    '''
    Changes current page to page named "Scores_Entry_5".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(6)

def page_change_More_Students(self) -> None:
    '''
    Changes current page to page named "More_Students".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(7)

def page_change_Home_No_Welcome(self) -> None:
    '''
    Changes current page to page named "Home_No_Welcome".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(8)

def page_change_Summary(self) -> None:
    '''
    Changes current page to page named "Summary".
    :return: None
    '''
    self.stackedWidget.setCurrentIndex(9)

def which_Scores_Entries_page(self) -> None:
    '''
    Changes to a Score Entries page according to value of num_of_attempts
    :return: None
    '''
    if self.num_of_attempts == 1:
        page_change_Scores_Entry_1(self)
    elif self.num_of_attempts == 2:
        page_change_Scores_Entry_2(self)
    elif self.num_of_attempts == 3:
        page_change_Scores_Entry_3(self)
    elif self.num_of_attempts == 4:
        page_change_Scores_Entry_4(self)
    elif self.num_of_attempts == 5:
        page_change_Scores_Entry_5(self)