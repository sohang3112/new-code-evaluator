from typing import Optional
from datetime import time
from asyncio import create_subprocess_exec


class ShellCommand:
    """
    Represents a shell (terminal) command which executes a single program.
    Does not support any way to combine multiple programs using pipes, sequential run, etc.
    """
    def __init__(self, cmd: str):
        self._value = cmd

    def __str__(self):
        return self._value 

    def __repr__(self):
        return f'ShellCommand({self._value})'

    def __call__(self, stdin: str, timeout: Optional[time] = None) -> str:   
        proc = subprocess.run(
                    self._value, capture_output=True, 
                    input=stdin, encoding='ascii', 
                    timeout=timeout and timeout.second)
        return proc.stdout

