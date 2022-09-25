Feature: Basic Window

    Open the tk.Tk window sub-class Windows.Basic() 

    Scenario: Open by file
        Given the virtual environment target/venv is activated
        And the Windows library is imported
        When the Basic class is called
        Then a window should pop up