from crewai import Task

class ResumeTask(Task):
    def __init__(self, description, expected_output, agent):
        super().__init__(
            description=description,
            expected_output=expected_output,
            agent=agent
        )


class CoverLetterTask(Task):
    def __init__(self, description, expected_output, agent):
        super().__init__(
            description=description,
            expected_output=expected_output,
            agent=agent
        )