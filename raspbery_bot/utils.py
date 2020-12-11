import subprocess
import settings

class BashControls():
    def __init__(self, bash_comand: str):
        self.bash_command = bash_comand
    
    def execute_command(self):
        return (
            subprocess.run([self.bash_command]).stdout
        )

            