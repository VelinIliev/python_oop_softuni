class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        name = name
        language = language
        skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == language:
            skills += skills_earned
            return f'{name} watched {course_name}'
        else:
            return f'{name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if new_language != language and skills >= skills_needed:
            old_language = language
            language = new_language
            return f'{name} switched from {old_language} to {language}'
        elif new_language == language and skills >= skills_needed:
            return f'{name} already knows {new_language}'
        else:
            needed_skills = skills_needed - skills
            return f'{name} needs {needed_skills} more skills'


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
