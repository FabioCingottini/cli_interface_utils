from .abstract_cli_worker import AbstractCliWorker
from typing import List


class ExitCliWorker(AbstractCliWorker):

    def __init__(self, worker_name: str, commands: List[str], command_help: str):
        super().__init__(worker_name, commands, command_help)

    def work(self, input_val: str):
        exit(0)

