from ncclient import manager
import xml.dom.minidom
import time

#Router interface desc change
"""
    
    https://webexapis.com/v1/messages
    Bot access token: Njc2ZDI5YjctMDEyNi00NjUwLThjZTktOGY5YWRmOWYwZWFmYzBmMGU3NDEtM2M2_P0A1_5b272d7d-050a-4b1a-9dd3-c6d4d4c029ed
    Bot ID: Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzBmMTIyMjVjLTViOWItNDY0OS1iYzZhLTZmMTI1NjQzNmM4OQ
    
    
    """
    
    
#bot shit
#loop search messages
#post message
#get input
#post reply
#run program
#post complete
#netconf sections


#router info
router = {
   'ip': '192.168.227.128',
   'port': '830',
   'username': 'cisco',
   'password': 'cisco123!'
}
m = manager.connect( 
host= router['ip'], 
port= router['port'], 
username= router['username'], 
password= router['password'], 
hostkey_verify=False 
) 

#creates running config file
def GetRunning():
    with open("%s.xml" % router['ip'], 'w') as Runningconf:
        newline = "-----------------------------"
        Runningconf.write(newline)
        date = time.time()
        Runningconf.write(date)
        c = m.get_config(source='running').data_xml
        Runningconf.write(c)

#netconf work


netconf_filter = """ 
<filter> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" /> 
</filter> 
""" 
netconf_reply = m.get_config(source="running", filter=netconf_filter) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 

#was added because i had to restart the VM removing the config
netconf_edit = """ 
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <interface> 
   <{interfaceID}> 
    <name>{interfacename}</name> 
    <description>{}</description> 
    <ip> 
     <address> 
      <primary> 
       <address>192.192.192.1</address> 
       <mask>255.255.255.0</mask> 
      </primary> 
     </address> 
    </ip> 
   </{interfaceID}}> 
  </interface> 
 </native> 
</config> 
"""

netconf_reply = m.edit_config(target="running", config=netconf_edit) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
