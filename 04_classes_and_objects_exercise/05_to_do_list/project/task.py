class Task:
    def __init__(self, name: str, due_date: str):
        name = name
        due_date = due_date
        comments = []
        completed = False

    def change_name(self, new_name):
        if name != new_name:
            name = new_name
            return name
        else:
            return f'Name cannot be the same.'

    def change_due_date(self, new_date:str):
        if due_date != new_date:
            due_date = new_date
            return due_date
        else:
            return f'Date cannot be the same.'

    def add_comment(self, comment: str):
        comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number in range(0, len(comments)):
            comments[comment_number] = new_comment
            return f'{", ".join(x for x in comments)}'
        else:
            return f'Cannot find comment.'

    def details(self):
        return f'Name: {name} - Due Date: {due_date}'