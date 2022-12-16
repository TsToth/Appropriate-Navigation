from ncclient import manager 
import xml.dom.minidom 

m = manager.connect( 
host="192.168.227.128", 
port=830, 
username="cisco", 
password="cisco123!", 
hostkey_verify=False 
) 


print("#Supported Capabilities (YANG models):") 
for capability in m.server_capabilities: 
    print(capability)

netconf_reply = m.get_config(source="running") 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 

netconf_filter = """ 
<filter> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" /> 
</filter> 
""" 
netconf_reply = m.get_config(source="running", filter=netconf_filter) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 

netconf_hostname = """ 
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <hostname>R1</hostname> 
 </native> 
</config> 
""" 
netconf_reply = m.edit_config(target="running", config=netconf_hostname) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#was added because i had to restart the VM removing the config
netconf_loopback = """ 
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <interface> 
   <Loopback> 
    <name>1</name> 
    <description>Heres a new description</description> 
    <ip> 
     <address> 
      <primary> 
       <address>10.1.1.1</address> 
       <mask>255.255.255.0</mask> 
      </primary> 
     </address> 
    </ip> 
   </Loopback> 
  </interface> 
 </native> 
</config> 
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_loopback2 = """ 
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <interface> 
   <Loopback> 
    <name>2</name> 
    <description>Heres a new description2</description> 
    <ip> 
     <address> 
      <primary> 
       <address>172.16.1.2</address> 
       <mask>255.255.255.0</mask> 
      </primary> 
     </address> 
    </ip> 
   </Loopback> 
  </interface> 
 </native> 
</config> 
""" 

netconf_reply = m.edit_config(target="running", config=netconf_loopback2) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_newloop = """
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <interface> 
   <Loopback> 
    <name>3</name> 
    <description>This one is kinda whacky</description> 
    <ip> 
     <address> 
     <primary> 
       <address>209.165.200.66</address> 
       <mask>255.255.255.252</mask>
      </primary> 
     </address> 
    </ip> 
   </Loopback> 
  </interface> 
 </native> 
</config> 
""" 
netconf_reply = m.edit_config(target="running", config=netconf_newloop)