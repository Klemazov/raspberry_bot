import os
class BashControls():
    def __init__(self, bash_comand: str):
        self.bash_command = bash_comand
    
    def execute_command(self):
        return (os.system(self.bash_command))
        
            