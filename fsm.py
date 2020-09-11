from transitions import Machine
from runner import Runner
from config_app import Config
import time

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

        self.runner = Runner()
        self.config = Config()

    def on_enter_run_state(self):
        print ('setup_run_state')
        self.runner.run(0)

    def on_exit_run_state(self):
        print ('quit_run_state')
        self.runner.stop()

    def on_enter_config_state(self):
        print ('setup config state')
        time.sleep(5)
        self.config.run()

    def on_exit_config_state(self):
        print ('quit config state')
        self.config.stop()
        
