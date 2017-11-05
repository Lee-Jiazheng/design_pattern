'''State
    it is used to solve the 'long method' problem.
    it is convinent to add a state and convert state in various of states.
'''
from abc import ABC, abstractmethod
class Work():
    def __init__(self):
        self.hour = 6
        self.task_finished = False
        self.state = ForenoonState()

    def setState(self, state):
        self.state = state 
    
    def WriteProgram(self):
        self.state.WriteProgram(self)

class State(ABC):
    @abstractmethod
    def WriteProgram(self, w):
        pass

class ForenoonState(State):
    def WriteProgram(self, w):
        if (w.hour < 12):
            print("Now is %s o'clock, forenoon working." % w.hour)
        else:
            w.setState(NoonState())
            w.WriteProgram()

class NoonState(State):
    def WriteProgram(self, w):
        if (w.hour < 13):
            print("Now is %s o'clock, noon working." % w.hour)
        else:
            w.setState(AfternoonState())
            w.WriteProgram()

class AfternoonState(State):
    def WriteProgram(self, w):
        if (w.hour < 17):
            print("Now is %s o'clock, afternoon working." % w.hour)
        else:
            w.setState(EveningState())
            w.WriteProgram()

class EveningState(State):
    def WriteProgram(self, w):
        if (w.hour < 21):
            print("Now is %s o'clock, evening, I will go home." % w.hour)
        else:
            w.setState(SleepState())
            w.WriteProgram()

class SleepState(State):
    def WriteProgram(self, w):
        print("Now is %s o'clock, I am sleepy." % w.hour)

if __name__ == "__main__":
    worker = Work()
    worker.WriteProgram()
    worker.hour = 12
    worker.WriteProgram()
    worker.hour = 13
    worker.WriteProgram()
    worker.hour = 17
    worker.WriteProgram()
    worker.hour = 21
    worker.WriteProgram()