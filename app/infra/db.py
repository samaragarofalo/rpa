import traceback
from rpa.app.infra.settings import collection


class MongoDBRepository:
    def __init__(self) -> None:
        pass

    def insert_data(self, data: list) -> None:
        try:
            if data:
                collection.insert_many(data)
                print("Dados inseridos com sucesso.")
            else:
                print("Nenhum dado para inserir.")
        except Exception as ex:
            print("Erro ao inserir dados:", ex)
            print(traceback.format_exc())
