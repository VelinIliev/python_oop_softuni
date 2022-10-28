from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, new_category: Category):
        added = [x for x in self.categories if x.id == new_category.id]
        if not added:
            self.categories.append(new_category)

    def add_topic(self, new_topic: Topic):
        added = [x for x in self.topics if x.id == new_topic.id]
        if not added:
            self.topics.append(new_topic)

    def add_document(self, new_document: Document):
        added = [x for x in self.documents if x.id == new_document.id]
        if not added:
            self.documents.append(new_document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = [x for x in self.categories if x.id == category_id][0]
        current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = [x for x in self.topics if x.id == topic_id][0]
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = [x for x in self.documents if x.id == document_id][0]
        current_document.file_name = new_file_name

    def delete_category(self, category_id: int):
        for i, cat in enumerate(self.categories):
            if cat.id == category_id:
                self.categories.pop(i)
                break

    def delete_topic(self, topic_id: int):
        for i, topic in enumerate(self.topics):
            if topic.id == topic_id:
                self.topics.pop(i)
                break

    def delete_document(self, document_id: int):
        for i, document in enumerate(self.documents):
            if document.id == document_id:
                self.documents.pop(i)
                break

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return_string = ""
        for document in self.documents:
            return_string += f'{document}\n'
        return return_string
