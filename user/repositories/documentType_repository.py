from user.models import DocumentType

class DocumentTypeRepository:
  def get(self, id):
    return DocumentType.objects.get(id=id)