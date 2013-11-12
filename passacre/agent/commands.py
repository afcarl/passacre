from twisted.protocols import amp


class AgentLocked(Exception):
    pass


class AgentUnlocked(Exception):
    pass


class Unlock(amp.Command):
    arguments = [
        ('password', amp.Unicode()),
    ]
    response = []
    errors = {AgentUnlocked: 'AGENT_UNLOCKED'}


class Lock(amp.Command):
    arguments = []
    response = []
    errors = {AgentLocked: 'AGENT_LOCKED'}


class Generate(amp.Command):
    arguments = [
        ('site', amp.Unicode()),
        ('username', amp.Unicode(optional=True)),
        ('password', amp.Unicode(optional=True)),
    ]
    response = [
        ('password', amp.Unicode()),
    ]
    errors = {AgentLocked: 'AGENT_LOCKED'}
