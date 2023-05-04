from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print("The dynamically typed languages are: ")
languages = [python, ruby, visual_basic]
for computer_language in languages:
    if computer_language.is_dynamic():
        print(computer_language.language)
