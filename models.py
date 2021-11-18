from typing import List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

from machines import TeacherMachine


class TestResult(Enum):
    PASSED = 1
    FAILED = 2
    ERROR = 3    # runtime error
    TIMEOUT = 3


@dataclass
class Test:
    input: str 
    output: str 

    def run(self) -> TestResult:
        raise NotImplementedError


@dataclass
class Problem: 
    name: str
    description: str 
    tests: List[Test]
    time_start: datetime
    time_limit: datetime


@dataclass
class Course:
    name: str
    problems: List[Problem]


@dataclass 
class Person:
    name: str 
    id: str 

    def login(self):
        raise NotImplementedError


@dataclass 
class Teacher(Person):
    courses: List[Course]


@dataclass
class Student(Person):
    courses: List[str]
