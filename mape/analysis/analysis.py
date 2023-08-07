from abc import ABC, abstractmethod


class Analysis(ABC):

    planners = []

    @abstractmethod
    def violates_upwards(self):
        pass

    @abstractmethod
    def violates_downwards(self):
        pass

    def add_planner(self, planner):
        self.planners.append(planner)

    def notify_planners(self):
        for planner in self.planners:
            if self.violates_upwards():
                planner.scale_up()
            elif self.violates_downwards():
                planner.scale_down()
