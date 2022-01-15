import xml.dom.minidom
from ncclient import manager
m = manager.connect(
    host="192.168.1.10",
    port=830,username="cisco",
    password="cisco123!",
    hostkey_verify=False)
nc_configospf = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router operation="replace">
            <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <id>100</id>
                    <router-id>1.1.1.1</router-id>
                        <network>
                            <ip>192.168.1.10</ip>
                            <mask>0.0.0.0</mask>
                            <area>0</area>
                        </network>
            </ospf>
        </router>

        </native>
    </config>
    
    """

netconf_reply = m.edit_config(target="running", config=nc_configospf)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())