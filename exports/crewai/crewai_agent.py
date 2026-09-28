from crewai import Agent
def create_agent():
    return Agent(role='GitContractShield', goal='Autonomous Commercial Contract Risk, Liability Cap & Clause Deviation Sentry Agent', backstory='Autonomous agent', verbose=True)
