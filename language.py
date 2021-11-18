from dataclasses import dataclass

from command import ShellCommand


@dataclass
class Language:
    compile: ShellCommand
    exec: ShellCommand

