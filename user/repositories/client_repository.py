from ..models.client import Client

class ClientRepository:
  def register(self, client):
    return Client.save(client)