from .abstract_cli_worker import AbstractCliWorker
from typing import List


class HelpCliWorker(AbstractCliWorker):

    def __init__(self, worker_name: str, commands: List[str], command_help: str, workers: List[AbstractCliWorker]):
        super().__init__(worker_name, commands, command_help)
        self.__workers_data = []
        self.__map_workers_help_to_props(workers)

    def work(self, input_val: str):
        if input_val is None or input_val == "":
            self.__print_all_helps()
        else:
            self.__print_single_worker_help(input_val)

    def __map_workers_help_to_props(self, workers: List[AbstractCliWorker]):
        for worker in workers:
            self.__workers_data.append({
                "name": worker.name,
                "commands": " ,".join(command for command in worker.commands),
                "help": worker.command_help
            })

    def __print_single_worker_help(self, worker_name):
        for worker_data in self.__workers_data:
            if worker_name == worker_data["name"]:
                print(
                    "{} commands: {} help: {}".format(worker_data["name"], worker_data["commands"], worker_data["help"])
                )

    def __print_all_helps(self):
        for worker_data in self.__workers_data:
            print("{} commands: {} help: {}".format(worker_data["name"], worker_data["commands"], worker_data["help"]))
