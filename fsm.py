from transitions import Machine
from runner import Runner

# UNITS:
F = 0
C = 1

class fsm():

    states = ['idle', 'run_state', 'config_state']
    transitions = [
        { 'trigger': 'start_running',
          'source': ['idle','config_state'], 'dest': 'run_state',
          'before': 'setup_run_state'},
        { 'trigger': 'starting_configuring',
          'source': ['idle','run_state'], 'dest': 'config_state',
          'before': 'setup_config_state'}
    ]

    def __init__(self):
        self.name = 'temp_runner'

        # Initialize the state machine
        self.machine = Machine(model=self,
                               states=fsm.states,
                               transitions=fsm.transitions,
                               initial='idle')

    def setup_config_state(self):
        print ('hello')

    def setup_run_state(self):
        units = F
        self.r = Runner(units)
        self.r.loop(0)

    def quit_run_state(self):