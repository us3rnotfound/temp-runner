from transitions import Machine
from runner import Runner
import threading, time

# UNITS:
F = 0
C = 1

class fsm():

    states = ['idle', 'run_state', 'config_state']
    transitions = [
        { 'trigger': 'trigger_run',
          'source': ['idle','config_state'], 'dest': 'run_state'},
        { 'trigger': 'trigger_configure',
          'source': 'idle', 'dest': 'config_state',
          'before': 'setup_config_state'},
        { 'trigger': 'trigger_configure',
          'source': 'run_state', 'dest': 'config_state',
          'after': 'quit_run_state'}
    ]

    def __init__(self):
        self.name = 'temp_runner'

        # Initialize the state machine
        self.machine = Machine(model=self,
                               states=fsm.states,
                               transitions=fsm.transitions,
                               initial='idle')

        self.run_thread = threading.Thread(target=self._run_thread)
        self.config_thread = threading.Thread(target=self._config_thread)
    
        self.run_thread.start()
        self.config_thread.start()

        self.r = Runner(F)

    def _run_thread(self):
        while True:
            if self.state == 'run_state':                
                self.r.loop(0)
            time.sleep(1)

    def _config_thread(self):
        while True:
            if self.state == 'config_state':
                print ('in config state')
            time.sleep(1)

    def setup_config_state(self):
        print ('state setup config state')

    def quit_run_state(self):
        print ('quit run state')
        self.r.stop_running()
