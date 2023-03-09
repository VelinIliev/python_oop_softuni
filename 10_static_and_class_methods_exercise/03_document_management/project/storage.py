from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, new_category: Category):
        if new_category not in self.categories:
            self.categories.append(new_category)

    def add_topic(self, new_topic: Topic):
        if new_topic not in self.topics:
            self.topics.append(new_topic)

    def add_document(self, new_document: Document):

        if new_document not in self.documents:
            self.documents.append(new_document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = next(filter(lambda x: x.id == category_id , self.categories), None)
        current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = next(filter(lambda x: x.id == topic_id, self.topics), None)
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = next(filter(lambda x: x.id == document_id, self.documents), None)
        current_document.file_name = new_file_name

    def delete_category(self, category_id: int):
        current_category = next(filter(lambda x: x.id == category_id, self.categories), None)
        self.categories.remove(current_category)

    def delete_topic(self, topic_id: int):
        current_topic = next(filter(lambda x: x.id == topic_id, self.topics), None)
        self.topics.remove(current_topic)

    def delete_document(self, document_id: int):
        current_document = next(filter(lambda x: x.id == document_id, self.documents), None)
        self.documents.remove(current_document)

    def get_document(self, document_id):
        current_document = next(filter(lambda x: x.id == document_id, self.documents), None)
        return current_document

    def __repr__(self):
        output = []
        for document in self.documents:
            output.append(f'{document}')
        return "\n".join(output)
