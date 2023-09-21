from abc import ABC, abstractmethod
from .singleton import Singleton


class Connection(metaclass=Singleton):
    def __init__(self, config: dict[str, str], connection_adaptor_obj: object) -> None:
        self.config = config
        self._connection_adaptor_obj = connection_adaptor_obj

    def get_connection_adaptor_obj(self):
        """`_summary_` \n"""
        return self._connection_adaptor_obj

    def setup_config(self, **kwargs):
        """_summary_ \n
        setup_config methode you can use it for add extra logic to update `self.config`
        """
        pass

    def create_new_connection(
        self,
    ) -> object:
        """_summary_ \n
        Create new connection object and return it with config

        """
        return self._connection_adaptor_obj(**self.config)
