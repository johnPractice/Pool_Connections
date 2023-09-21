import logging
from interfaces.connection import Connection
from interfaces.connection import Connection
from interfaces.singleton import Singleton


class PoolConnection(metaclass=Singleton):
    """`_summary_`\n"""

    def __init__(
        self, connection: Connection, pool_count: int, pool_threshold: int = 2
    ) -> None:
        self.connection = connection
        self.__pool_count = pool_count
        self.__pool_threshold = pool_threshold
        self.__pool_connections: list[connection] = list()
        self.__create_pool_connections()

    def get_connection(self):
        return next(self.__get_connection())

    def __get_connection(self):
        print(self.__pool_connections)
        try:
            yield self.__pool_connections.pop()
        except IndentationError:
            yield self.connection.create_new_connection()
        except Exception as e:
            logging.error(e)
            yield
        finally:
            pooled_connection_count = len(self.__pool_connections)
            if pooled_connection_count < self.__pool_threshold:
                self.__fill_pool()

    def __fill_pool(self):
        """`_summary_`\n
        Fill pool `self.__pool_connections`.
        """
        for _ in range(self.__pool_count - len(self.__pool_connections)):
            self.__pool_connections.insert(0, self.connection.create_new_connection())

    def __create_pool_connections(
        self,
    ):
        for _ in range(self.__pool_count):
            self.__pool_connections.append(self.connection.create_new_connection())
