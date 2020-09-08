#from transitions.extensions import LockedMachine as Machine
from transitions import Machine
from runner import Runner

# UNITS:
F = 0
C = 1

class fsm():

    states = [
             {'name':'idle'},
             {'name':'run_state',},
             {'name':'config_state'}
             ]
    transitions = [
             { 'trigger': 'trigger_run',
             'source': ['idle','config_state'],
             'dest': 'run_state'},
             { 'trigger': 'trigger_config',
             'source': ['idle','run_state'],
             'dest': 'config_state'}
             ]

    def __init__(self):
        self.name = 'temp_runner'

        # Initialize the state machine
        self.machine = Machine(model=self,
                               states=fsm.states,
                               transitions=fsm.transitions,
                               initial='idle')

        self.r = Runner(F)

    def on_enter_run_state(self):
        print ('setup_run_state')
        self.r.loop(0)

    def on_exit_run_state(self):
        print ('quit_run_state')
        self.r.stop_running()

    def on_enter_config_state(self):
        print ('setup config state')

    def on_exit_config_state(self):
        print ('quit config state')
