from django_enumfield import enum


class TaskStatus(enum.Enum):
    NOT_STARTED = 0
    WORK_IN_PROGRESS = 10
    DONE = 20
