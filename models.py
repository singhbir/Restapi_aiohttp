"""
this modules contains all the methods that can be implemented on database
"""
from db import Agent, System

def save_new_agent(uu_id, agent_ip):
    """
    method for saving new agent
    """
    agent1 = Agent.create(uuid=uu_id, agentip=agent_ip)
    agent1.save()


def get_agent(uu_id):
    """
    method for getting agent info
    """
    agent1 = Agent.select().where(Agent.uuid == uu_id).get()
    return agent1


def update_agent(oldip, newip):
    """
    method for updating agent
    """
    query = Agent.update(agentip=newip).where(Agent.agentip == oldip)
    no_after_query = query.execute()


def delete_agent(ip):
    """
    method for deleting agent
    """
    query_first = Agent.select().where(Agent.agentip == ip).get()

    if System.select().where(System.agent_id == query_first.uuid).count():
        return "Cannot be deleted"
    else:
        q = Agent.delete().where(Agent.agentip == ip)
        no_after_query = q.execute()
        return "record successfully deleted "

def add_system(agentid, sys_name, sys_id):
    """
    method for adding system
    """
    sys1 = System.create(agent_id=agentid, sysname=sys_name, sid=sys_id)
    sys1.save()


def get_system(agentid):
    """
    method for getting system info
    """
    query_first = System.select().where(System.agent_id == agentid).get()
    return query_first


def delete_system(sys_id):
    """
    method for deleting system
    """
    query_first = System.delete().where(System.sid == sys_id)
    query_first.execute()