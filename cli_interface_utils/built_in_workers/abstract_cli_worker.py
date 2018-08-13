from abc import ABC, abstractmethod
from typing import List


class AbstractCliWorker(ABC):

    def __init__(self, worker_name: str, commands: List[str], command_help: str):
        self.commands = []
        [self.commands.append(command.lower()) for command in commands]
        self.command_help = command_help
        self.name = worker_name

    @abstractmethod
    def work(self, input_val: str):
        pass
