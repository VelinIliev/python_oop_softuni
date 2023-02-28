from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        else:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        task = next(filter(lambda x: x.name == task_name, self.tasks), None)
        if task:
            task.completed = True
            return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        count = 0
        tasks_to_remove = [x for x in self.tasks if x.completed is True]
        for task in tasks_to_remove:
            self.tasks.remove(task)
            count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        output = [f'Section {self.name}:']
        for task in self.tasks:
            output.append(f'{task.details()}')
        return '\n'.join(output)

