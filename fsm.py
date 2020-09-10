from transitions import Machine
from runner import Runner
from config_app import Config
import config_parser

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
        config_list = config_parser.read_config()

        self.name = 'temp_runner'

        # Initialize the state machine
        self.machine = Machine(model=self,
                               states=fsm.states,
                               transitions=fsm.transitions,
                               initial='idle')

        self.runner = Runner(config_list)
        self.config = Config()

    def on_enter_run_state(self):
        print ('setup_run_state')
        self.runner.loop(0)

    def on_exit_run_state(self):
        print ('quit_run_state')
        self.runner.stop_running()

    def on_enter_config_state(self):
        print ('setup config state')
        self.config.run()

    def on_exit_config_state(self):
        print ('quit config state')
        self.config.stop_running()
        
