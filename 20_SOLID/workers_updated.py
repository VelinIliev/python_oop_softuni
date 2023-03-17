from abc import ABC, abstractmethod
import time


class Work(ABC):
    @staticmethod
    @abstractmethod
    def work():
        ...


class Eat(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        ...


class Worker(Work, Eat):
    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(0)


class SuperWorker(Eat, Work):
    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(0)


class Robot(Work):
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class BaseManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Work), f"`worker` must be of type {Work}"

        self.worker = worker


class WorkManager(BaseManager):
    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
