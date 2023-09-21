from abc import ABC, abstractmethod
import logging


class ObjectStorage(ABC):
    def __init__(self, buckets_name: list[str]) -> None:
        self._buckets_name = buckets_name

    def get_connection(self):
        pass

    def _get_connection(self):
        pass
        # try:
        #     yield pool.pop()

        # except IndexError:
        #     yield FAClient(
        #         FUSIONAUTH_API_KEY,
        #         FUSIONAUTH_HOST
        # )
        # finally:
        #     if len(pool) < CLIENT_POOL_REFILL_THRESHOLD:
        #         fill_pool()

    def __create_pool_connections(
        self,
    ):
        pass

    @abstractmethod
    def base_config(self, pre_config_functions_list: list[callable], **configs):
        for f in pre_config_functions_list:
            logging.info("💡run the function", f.__name__)
            try:
                logging.info("✅:", f.__name__)
            except Exception as e:
                logging.error("🚫:", e)

    def check_or_create_bucket(self):
        for bucket_name in self._buckets_name:
            check_bucket_exist = self._check_buckets_exist(bucket_name)
            if not check_bucket_exist:
                check_create_bucket = self.__create_bucket(bucket_name)
            if check_bucket_exist or check_create_bucket:
                logging.info()
                raise Exception("Check log for failer")

    def _check_buckets_exist(self, bucket_name: str) -> bool:
        # return True if client.bucket_exists(bucket_name) else False
        return True

    def __create_bucket(self, bucket_name: str) -> bool:
        try:
            # client.make_bucket(bucket_name)
            return True
        except Exception as e:
            logging.error("failed to create bucket", e)
            return False
