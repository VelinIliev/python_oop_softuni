from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)


# c = Category(1, "C")
# t = Topic(1, "T", "C:\\user")
# d = Document(1, 1, 1, "D")
# s = Storage()
#
# print(c.id, 1)
# print(c.name, "C")
#
# c.edit("new")
# print(c.name, "new")
# #
# print(str(c), "Category 1: C")
# #
# print(d.id, 1)
# print(d.category_id, 1)
# print(d.topic_id, 1)
# print(d.file_name, "D")
# print(d.tags, [])
#
# doc = Document.from_instances(1, c, t, "Doc")
# print(doc.id, 1)
# print(doc.category_id, 1)
# print(doc.topic_id, 1)
# print(doc.file_name, "Doc")
# print(doc.tags, [])
# #
# d.add_tag("tag")
# d.add_tag("tag")
# print(d.tags, ["tag"])
# #
# d.add_tag("tag")
# d.add_tag("tag")
# d.remove_tag("tag")
# print(d.tags, [])
# #
# d.edit("new")
# print(d.file_name, "new")
# #
# d.add_tag("tag")
# print(str(d), 'Document 1: D; category 1, topic 1, tags: tag')
# #
# print(t.id, 1)
# print(t.id, 1)
# print(t.storage_folder, "C:\\user")
# #
# t.edit("new topic", "new folder")
# print(t.topic, "new topic")
# print(t.storage_folder, "new folder")
#
# print(str(t), "Topic 1: T in C:\\user")
#
# print(s.categories, [])
# print(s.topics, [])
# print(s.documents, [])
#
# s.add_category(c)
# s.add_category(c)
# print(s.categories, [c])
#
# s.add_topic(t)
# s.add_topic(t)
# print(s.topics, [t])
#
# s.add_document(d)
# s.add_document(d)
# print(s.documents, [d])
#
# s.add_category(c)
# s.edit_category(1, "new")
# print(s.categories[0].name, "new")
#
# s.add_topic(t)
# s.edit_topic(1, "new", "new storage")
# print(s.topics[0].topic, "new")
# print(s.topics[0].storage_folder, "new storage")
#
# s.add_document(d)
# s.edit_document(1, "new")
# print(s.documents[0].file_name, "new")
#
# s.add_category(c)
# s.delete_category(1)
# print(s.categories, [])
#
# s.add_topic(t)
# s.delete_topic(1)
# print(s.topics, [])
#
# s.add_document(d)
# s.delete_document(1)
# print(s.documents, [])
#
# s.add_category(c)
# s.add_topic(t)
# s.add_document(d)
# expected = str(s).strip('\n')
# print(expected, "Document 1: D; category 1, topic 1, tags: ")
