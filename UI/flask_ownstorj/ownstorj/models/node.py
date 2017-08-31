from UI.utilities import account_manager
from UI.engine import StorjEngine

import socket
from ipwhois import IPWhois
import pycountry

# Module for node details displaying for OwnStorj

storj_engine = StorjEngine()  # init StorjEngine

class OwnStorjNodeDetails:
    def __init__(self):
        self.node_details_content = None

    def get_most_recent_known_nodes_batch(self):
        return storj_engine.storj_client.contact_list()

    def node_details(self, nodeID):
        node_details_array = {}
        self.node_details_content = storj_engine.storj_client.contact_lookup(str(nodeID))

        node_details_array["address"] = self.node_details_content.address
        node_details_array["lastTimeout"] = self.node_details_content.lastTimeout
        node_details_array["timeoutRate"] = self.node_details_content.timeoutRate
        node_details_array["userAgent"] = self.node_details_content.userAgent
        node_details_array["protocol"] = self.node_details_content.protocol
        node_details_array["responseTime"] = self.node_details_content.responseTime
        node_details_array["lastSeen"] = self.node_details_content.lastSeen
        node_details_array["port"] = self.node_details_content.port
        node_details_array["nodeID"] = self.node_details_content.nodeID

        ip_addr = socket.gethostbyname(str(self.node_details_content.address))

        obj = IPWhois(ip_addr)
        res = obj.lookup_whois()
        country = res["nets"][0]['country']

        country_parsed = pycountry.countries.get(alpha_2=str(country))

        country_full_name = country_parsed.name

        node_details_array["country_full_name"] = country_full_name
        node_details_array["country_code"] = country

        return node_details_array

