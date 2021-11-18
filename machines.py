"""Finite State Machines for each Object"""

from statemachine import StateMachine, State


class TeacherMachine(StateMachine):
    no_problem_defined = State('No Problem Defined', initial=True)
    problem_defined = State('Problem Defined')
    submissions_allowed = State('Students can upload Code Submissions')
    submissions_end = State('Time Up for Submissions')
    all_submissions_evaluated = State('All student Submissions Evaluated')

    define_problem = no_problem_defined.to(problem_defined)
    allow_submissions = problem_defined.to(submissions_allowed)
    submission_uploaded = submissions_allowed.to(submissions_allowed)
    timeout_submissions = submissions_allowed.to(submissions_end)
    evaluate_code = submissions_end.to(all_submissions_evaluated)


class StudentMachine(StateMachine):
    problem_defined = State('Teacher has uploaded problem', initial=True)
    submitted = State('Code submitted for evaluation')
    time_end = State('Timeout - No Code Submitted')
    result = State('Code Submission Results uploaded')

    submit_code = problem_defined.to(submitted)
    timeout = problem_defined.to(time_end)     # no code submitted
    show_results = submitted.to(result) | time_end.to(result)






    