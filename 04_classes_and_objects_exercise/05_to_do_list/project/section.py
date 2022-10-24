from project.task import Task


class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        tasks_list = []
        for x in self.tasks:
            tasks_list.append(x.name)
        if new_task.name in tasks_list:
            return f'Task is already in the section {self.name}'
        else:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        count = 0
        tasks_to_remove = []
        for i, task in enumerate(self.tasks):
            if task.completed:
                tasks_to_remove.append(i)
        while tasks_to_remove:
            self.tasks.pop(tasks_to_remove.pop())
            count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        return_string = ""
        return_string += f'Section {self.name}:\n'
        for task in self.tasks:
            return_string += f'{task.details()}\n'
        return return_string

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())


