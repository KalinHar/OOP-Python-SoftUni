class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for cat in self.categories:
            if category_id == cat.id:
                cat.family_name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for top in self.topics:
            if topic_id == top.id:
                top.topic = new_topic
                top.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        doc = self.get_document(document_id)
        doc.file_name = new_file_name

    def delete_document(self, document_id):
        doc = self.get_document(document_id)
        self.documents.remove(doc)

    def delete_category(self, category_id):
        for cat in self.categories:
            if category_id == cat.id:
                self.categories.remove(cat)

    def delete_topic(self, topic_id):
        for top in self.topics:
            if topic_id == top.id:
                self.topics.remove(top)

    def get_document(self, document_id):
        for doc in self.documents:
            if document_id == doc.id:
                return doc

    def __repr__(self):
        result = [repr(doc) for doc in self.documents]
        return "\n".join(result)
