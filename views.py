"""
all operations of api are in app.py file
"""
import json
import uuid
from aiohttp import web
from models import (
    save_new_agent,
    get_agent,
    update_agent,
    delete_agent,
    add_system,
    get_system,
    delete_system,
)


class AgentMethods(web.View):
    """
    ALL METHODS OF AGENT ARE IMPLEMENTED HERE
    """

    async def post(self):
        """
        description: creating agent
        params: agentip
        """
        try:
            uu_id = str(uuid.uuid1()).replace("-", "")
            agent = await self.request.json()
            agent_ip = agent["agentip"]
            # agent_ip = self.request.json('agentip')
            save_new_agent(uu_id, agent_ip)
            print(f"Creating agent with uuid {uu_id} and ip {agent_ip} ")
            response_obj = {
                "status": "success",
                "message": f"agent created successfully with  ip {agent_ip}",
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            if str(error_delete) == "UNIQUE constraint failed: agent.uuid":
                response_obj = {
                    "status": "failed",
                    "message": "agent uuid present already",
                }
            else:
                response_obj = {"status": "failed", "message": str(error_delete)}
                print(str(error_delete))
            return web.Response(text=json.dumps(response_obj), status=500)

    async def get(self):
        """
        description: Get agent info 
        params: uuid
        
        """
        try:
            uid = await self.request.json()
            uu_id = uid["uuid"]
            data = get_agent(uu_id)
            print(
                f"uuid : - {data.uuid}   agentip:- {data.agentip} created_date:-{data.agentdate}"
            )
            response_obj = {
                "status": "success",
                "message": f"uuid {data.uuid} agentip {data.agentip} created_date {data.agentdate}",
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            return web.Response(text=f"No Record Found {error_delete}", status=404)

    async def put(self):
        """
        description: updating agent 
        params: old ip , new ip
        
        """
        try:
            data = await self.request.json()
            old_ip = data["oldip"]
            new_ip = data["newip"]
            update_agent(old_ip, new_ip)
            response_obj = {
                "status": "success",
                "message": f"agent updated successfully from old-ip {old_ip} to new-ip:{new_ip}",
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            return web.Response(text=f"{str(error_delete)}", status=500)

    async def delete(self):
        """
        description: deleting agent 
        params: agentip
        
        """
        try:
            data = await self.request.json()
            agent_ip = data["agentip"]
            response_msg = delete_agent(agent_ip)
            response_obj = {
                "status": "success",
                "message": response_msg,
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            return web.Response(text=f"{str(error_delete)}", status=500)


class SystemMethods(web.View):
    """
    ALL METHODS OF SYSTEM API ARE IMPLEMENTED HERE
    """

    async def post(self):
        """
        description: creating system
        params: agentid , sysname(system name)
        
        """
        try:
            data = await self.request.json()
            agent_id = data["agentid"]
            sys_name = data["sysname"]
            sys_id = str(uuid.uuid1()).replace("-", "")
            add_system(agent_id, sys_name, sys_id)
            print(f"Creating system on agent :- {agent_id} with name :-  {sys_name}")
            response_obj = {
                "status": "success",
                "message": f"Creating system on agent :- {agent_id} with name :- {sys_name}",
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            return web.Response(text=f"{str(error_delete)}", status=500)

    async def get(self):
        """
        description: getting system
        params: agentid
        
        """
        try:
            data = await self.request.json()
            agent_id = data["agentid"]
            info = get_system(agent_id)
            response_obj = {
                "status": "success",
                "message": f"systemname:-{info.sysname} id:-{info.sid} ",
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            return web.Response(text=f"{str(error_delete)}", status=500)

    async def delete(self):
        """
        description: deleting system 
        params: sysid
        
        """
        try:
            data = await self.request.json()
            sys_id = data["sysid"]
            delete_system(sys_id)
            response_obj = {
                "status": "success",
                "message": f"system deleted successfully systemid {sys_id}",
            }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as error_delete:
            return web.Response(text=f"{str(error_delete)}", status=500)
