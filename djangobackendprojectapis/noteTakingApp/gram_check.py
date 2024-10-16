import language_tool_python

# Initialize the LanguageTool object
tool = language_tool_python.LanguageTool('en-US')

# The text to be checked

# Check the text for grammar issues
def check_grammer(note):
    matches = tool.check(note)

    # Determine if the note is grammatically correct
    if len(matches) == 0:
        print("The note is grammatically correct.")
        return True
    else:
        print("The note is not grammatically correct.")
        return False