#Global Parameter
DUT1 = "DUT1"
#TestCase Specific Parameters

#Interface Configuration
INTF1_reqMethod = "POST"
INTF1_objURL = """/public/v1/config/IPv4Intf"""
INTF1_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.1/24"}"""          #Valid values passed
INTF1_ExpectedResponse = """Success"""

INTF2_reqMethod = "POST"
INTF2_objURL = """/public/v1/config/IPv4Intf"""
INTF2_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.1/24"}"""
INTF2_ExpectedResponse = """Error""" 									 #Trying to configure IP on interface that is already configured

INTF3_reqMethod = "PATCH"
INTF3_objURL = """/public/v1/config/IPv4Intf"""
INTF3_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.1/24"}"""
INTF3_ExpectedResponse = """Error"""                                                                       #Trying to update with same values

INTF4_reqMethod = "PATCH"
INTF4_objURL = """/public/v1/config/IPv4Intf"""
INTF4_payload = """{"IntfRef":"DUT1_P1","IpAddr":"10.0.0.2/24","AdminState":"UP"}"""         #Trying to update with different values
INTF4_ExpectedResponse = "Success"

INTF5_reqMethod = "PATCH"
INTF5_objURL = """/public/v1/config/IPv4Intf"""
INTF5_payload = """{"IntfRef":"DUT1_P1","IpAddr":"10.0.0.2/24","AdminState":"DOWN"}"""     #Trying to update the default value, for instance value of "AdminState" from "UP" to "DOWN"
INTF5_ExpectedResponse = "Success"

INTF6_reqMethod = "PATCH"
INTF6_objURL = """/public/v1/config/IPv4Intf"""
INTF6_payload = """{"IntfRef":"DUT1_P1","IpAddr":"10.0.0.2/24","AdminState":"UP"}"""          #Updating again to a default value 
INTF6_ExpectedResponse = "Success"

INTF7_reqMethod = "PATCH"
INTF7_objURL = """/public/v1/config/IPv4Intf"""
INTF7_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.2"}"""              #Missing Subnet mask
INTF7_ExpectedResponse = """Error"""

INTF8_reqMethod = "PATCH"
INTF8_objURL = """/public/v1/config/IPv4Intf"""
INTF8_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.256/24"}"""      #Invalid IP address
INTF8_ExpectedResponse = """Error"""

INTF9_reqMethod = "PATCH"
INTF9_objURL = """/public/v1/config/IPv4Intf"""
INTF9_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.2/33"}"""         #Invalid Subnet mask
INTF9_ExpectedResponse = """Error"""

INTF10_reqMethod = "POST"
INTF10_objURL = """/public/v1/config/IPv4Intf"""
INTF10_payload = """{"IntfRef":"DUT1_P2","AdminState":"UP","IpAddr":"10.0.0.2/24"}"""         #Invalid Intfref while creating
INTF10_ExpectedResponse = "Error"

INTF11_reqMethod = "PATCH"
INTF11_objURL = """/public/v1/config/IPv4Intf"""
INTF11_payload = """{"IntfRef":"DUT1_P2","AdminState":"UP","IpAddr":"10.0.0.2/24"}"""         #Invalid Intfref while updating 
INTF11_ExpectedResponse = "Error"

INTF12_reqMethod = "POST"
INTF12_objURL = """/public/v1/config/IPv4Intf"""
INTF12_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.2\24"}"""         #Invalid Slash while creating
INTF12_ExpectedResponse = """Error"""

INTF13_reqMethod = "POST"
INTF13_objURL = """/public/v1/config/IPv4Intf"""
INTF13_payload = """{"IntfRef":"DUT1_P1","AdminState":"UP","IpAddr":"10.0.0.2\24"}"""         #Invalid Slash while updating
INTF13_ExpectedResponse = """Error"""

INTF14_reqMethod = "POST"
INTF14_objURL = """/public/v1/config/IPv4Intf"""
INTF14_payload = """{"IntfRef":"DUT1_P2","AdminState":"UP","IpAddr":"10.0.0.2/24"}"""        #Configuring 2nd interface of the same router in same network as that of first interface
INTF14_ExpectedResponse = """Error"""

INTF15_reqMethod = "DELETE"                                                                           
INTF15_objURL = """/public/v1/config/IPv4Intf"""
INTF15_payload = """{"IntfRef":"DUT1_P1"}"""                                                 #Deleting the valid interface
INTF15_ExpectedResponse = "Success"

INTF16_reqMethod = "DELETE"
INTF16_objURL = """/public/v1/config/IPv4Intf"""
INTF16_payload = """{"IntfRef":"DUT1_P1"}"""                                                 #Re-Deleting the interface
INTF16_ExpectedResponse = "Error"


#VLAN Configuration Parameters
VLAN1_reqMethod = "POST"
VLAN1_objURL = """/public/v1/config/Vlan"""
VLAN1_payload = """{"VlanId":300}"""
VLAN1_ExpectedResponse = "Success"

VLAN2_reqMethod = "PATCH"
VLAN2_objURL = """/public/v1/config/Vlan"""
VLAN2_payload = """{"VlanId":300, "IntfList":["DUT1_P1"]}"""
VLAN2_ExpectedResponse = "Success"

VLAN3_reqMethod = "PATCH"
VLAN3_objURL = """/public/v1/config/Vlan"""
VLAN3_payload = """{"VlanId":300, "IntfList":["DUT1_P2"]}"""
VLAN3_ExpectedResponse = "Success"

VLAN4_reqMethod = "PATCH"
VLAN4_objURL = """/public/v1/config/Vlan"""
VLAN4_payload = """{"VlanId":300, "Description":"This is for testing"}"""
VLAN4_ExpectedResponse = "Success"

VLAN5_reqMethod = "PATCH"
VLAN5_objURL = """/public/v1/config/Vlan"""
VLAN5_payload = """{"VlanId":300,"AdminState":"DOWN"}"""
VLAN5_ExpectedResponse = "Success"

VLAN6_reqMethod = "PATCH"
VLAN6_objURL = """/public/v1/config/Vlan"""
VLAN6_payload = """{"VlanId":300,"AdminState":"UP"}"""
VLAN6_ExpectedResponse = "Success"

VLAN7_reqMethod = "DELETE"
VLAN7_objURL = """/public/v1/config/Vlan"""
VLAN7_payload = """{"VlanId":300}"""
VLAN7_ExpectedResponse = "Success"


#ARP Configurtion parameters
ARP1_reqMethod = "PATCH"
ARP1_objURL = """/public/v1/config/ArpGlobal"""
ARP1_payload = """{"Vrf":"default", "Timeout":600}"""
ARP1_ExpectedResponse = "Error"


ARP2_reqMethod = "PATCH"
ARP2_objURL = """/public/v1/config/ArpGlobal"""
ARP2_payload = """{"Vrf":"default", "Timeout":800}"""
ARP2_ExpectedResponse = "Success"


#LLDP Configurtion parameters

LLDP1_reqMethod = "PATCH"
LLDP1_objURL = """/public/v1/config/LLDPIntf"""
LLDP1_payload = """{"IntfRef":"DUT1_P1", "TxRxMode":"RxOnly" }"""
LLDP1_ExpectedResponse = "Success"

LLDP2_reqMethod = "PATCH"
LLDP2_objURL = """/public/v1/config/LLDPIntf"""
LLDP2_payload = """{"IntfRef":"DUT1_P1", "TxRxMode":"TxOnly"}"""
LLDP2_ExpectedResponse = "Success"

LLDP3_reqMethod = "PATCH"
LLDP3_objURL = """/public/v1/config/LLDPIntf"""
LLDP3_payload = """{"IntfRef":"DUT1_P1", "TxRxMode":"TxRx" }"""
LLDP3_ExpectedResponse = "Success"

LLDP4_reqMethod = "PATCH"
LLDP4_objURL = """/public/v1/config/LLDPGlobal"""
LLDP4_payload = """{"Vrf":"default", "Enable":true}"""
LLDP4_ExpectedResponse = "Success"

LLDP5_reqMethod = "PATCH"
LLDP5_objURL = """/public/v1/config/LLDPGlobal"""
LLDP5_payload = """{"Vrf":"default", "Enable":false}"""
LLDP5_ExpectedResponse = "Success"

LLDP6_reqMethod = "PATCH"
LLDP6_objURL = """/public/v1/config/LLDPGlobal"""
LLDP6_payload = """{"Vrf":"default", "TranmitInterval":70}"""
LLDP6_ExpectedResponse = "Success"

LLDP7_reqMethod = "PATCH"
LLDP7_objURL = """/public/v1/config/LLDPGlobal"""
LLDP7_payload = """{"Vrf":"default", "TranmitInterval":30}"""
LLDP7_ExpectedResponse = "Success"

LLDP8_reqMethod = "PATCH"
LLDP8_objURL = """/public/v1/config/LLDPGlobal"""
LLDP8_payload = """{"Vrf":"default", "TxRxMode":"TxOnly"}"""
LLDP8_ExpectedResponse = "Success"

LLDP9_reqMethod = "PATCH"
LLDP9_objURL = """/public/v1/config/LLDPGlobal"""
LLDP9_payload = """{"Vrf":"default", "TxRxMode":"RxOnly"}"""
LLDP9_ExpectedResponse = "Success"

LLDP10_reqMethod = "PATCH"
LLDP10_objURL = """/public/v1/config/LLDPGlobal"""
LLDP10_payload = """{"Vrf":"default", "TxRxMode":"TxRx"}"""
LLDP10_ExpectedResponse = "Success"

LLDP11_reqMethod = "PATCH"
LLDP11_objURL = """/public/v1/config/LLDPGlobal"""
LLDP11_payload = """{"Vrf":"default", "SnoopAndDrop":true}"""
LLDP11_ExpectedResponse = "Success"

LLDP12_reqMethod = "PATCH"
LLDP12_objURL = """/public/v1/config/LLDPGlobal"""
LLDP12_payload = """{"Vrf":"default", "SnoopAndDrop":false}"""
LLDP12_ExpectedResponse = "Success"

#Create Loopback
LO1_reqMethod = "POST"
LO1_objURL = """/public/v1/config/LogicalIntf"""
LO1_payload = """{"Name":"lo1", "Type":"Loopback"}"""
LO1_ExpectedResponse = "Success"

LO2_reqMethod = "POST"
LO2_objURL = """/public/v1/config/LogicalIntf"""
LO2_payload = """{"Name":"lo1", "Type":"Loopback"}"""
LO2_ExpectedResponse = "Error"

LO3_reqMethod = "DELETE"
LO3_objURL = """/public/v1/config/LogicalIntf"""
LO3_payload = """{"Name":"lo1"}"""
LO3_ExpectedResponse = "Success"

LO4_reqMethod = "DELETE"
LO4_objURL = """/public/v1/config/LogicalIntf"""
LO4_payload = """{"Name":"lo1"}"""
LO4_ExpectedResponse = "Error"

#BGP Configurtion parameters

#For BGP Global

BGP1_reqMethod = "PATCH"
BGP1_objURL = """/public/v1/config/BGPGlobal"""                           #vrf
BGP1_payload = """{"Vrf" : "default"}"""       
BGP1_ExpectedResponse = """Error"""

BGP2_reqMethod = "PATCH"
BGP2_objURL = """/public/v1/config/BGPGlobal"""                            #vrf
BGP2_payload = """{"Vrf" : "vrf1"}"""       
BGP2_ExpectedResponse = """Error"""

BGP3_reqMethod = "PATCH"
BGP3_objURL = """/public/v1/config/BGPGlobal"""                            #ASNum
BGP3_payload = """{"Vrf" : "default","ASNum" : "200"}"""       
BGP3_ExpectedResponse = """Success"""

BGP4_reqMethod = "PATCH"
BGP4_objURL = """/public/v1/config/BGPGlobal"""                            #RouterId
BGP4_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1"}"""       
BGP4_ExpectedResponse = """Success"""

BGP5_reqMethod = "PATCH"
BGP5_objURL = """/public/v1/config/BGPGlobal"""                            #RouterId(invalid)
BGP5_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1"}"""       
BGP5_ExpectedResponse = """Error"""

BGP6_reqMethod = "PATCH"
BGP6_objURL = """/public/v1/config/BGPGlobal"""                            #EBGPAllowMultipleAS(default)
BGP6_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1","EBGPAllowMultipleAS":false}"""       
BGP6_ExpectedResponse = """Error"""

BGP7_reqMethod = "PATCH"
BGP7_objURL = """/public/v1/config/BGPGlobal"""                            #EBGPAllowMultipleAS
BGP7_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1","EBGPAllowMultipleAS":true}"""       
BGP7_ExpectedResponse = """Success"""

BGP8_reqMethod = "PATCH"
BGP8_objURL = """/public/v1/config/BGPGlobal"""                            #EBGPAllowMultipleAS(default)
BGP8_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1","EBGPAllowMultipleAS":false}"""       
BGP8_ExpectedResponse = """Success"""

BGP9_reqMethod = "PATCH"
BGP9_objURL = """/public/v1/config/BGPGlobal"""                            #UseMultiplePaths
BGP9_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1","UseMultiplePaths":false}"""       
BGP9_ExpectedResponse = """Error"""
	
BGP10_reqMethod = "PATCH"
BGP10_objURL = """/public/v1/config/BGPGlobal"""                            #UseMultiplePaths
BGP10_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1","UseMultiplePaths":false}"""       
BGP10_ExpectedResponse = """Error"""
	
BGP11_reqMethod = "PATCH"
BGP11_objURL = """/public/v1/config/BGPGlobal"""                            #UseMultiplePaths
BGP11_payload = """{"Vrf" : "default","ASNum" : "200","RouterId":"1.1.1.1","UseMultiplePaths":true}"""       
BGP11_ExpectedResponse = """Success"""
	
BGP12_reqMethod = "PATCH"
BGP12_objURL = """/public/v1/config/BGPGlobal"""                            #IBGPMaxPaths
BGP12_payload = """{"Vrf" : "default","IBGPMaxPaths" : 0}"""       
BGP12_ExpectedResponse = """Error"""
	
BGP13_reqMethod = "PATCH"
BGP13_objURL = """/public/v1/config/BGPGlobal"""                            #IBGPMaxPaths(Max value)
BGP13_payload = """{"Vrf" : "default","IBGPMaxPaths" : 4294967294}"""       
BGP13_ExpectedResponse = """Success"""
	
BGP14_reqMethod = "PATCH"
BGP14_objURL = """/public/v1/config/BGPGlobal"""                            #IBGPMaxPaths
BGP14_payload = """{"Vrf" : "default","IBGPMaxPaths" : 4294967298}"""       
BGP14_ExpectedResponse = """cannot unmarshal"""
	
BGP15_reqMethod = "PATCH"
BGP15_objURL = """/public/v1/config/BGPGlobal"""                            #EBGPMaxPaths
BGP15_payload = """{"Vrf" : "default","IBGPMaxPaths" : 0}"""       
BGP15_ExpectedResponse = """Error"""
	
BGP16_reqMethod = "PATCH"
BGP16_objURL = """/public/v1/config/BGPGlobal"""                            #EBGPMaxPaths
BGP16_payload = """{"Vrf" : "default","IBGPMaxPaths" : 0}"""       
BGP16_ExpectedResponse = """Success"""

BGP17_reqMethod = "PATCH"
BGP17_objURL = """/public/v1/config/BGPGlobal"""                            #EBGPMaxPaths
BGP17_payload = """{"Vrf" : "default","IBGPMaxPaths" : 4294967298}"""       
BGP17_ExpectedResponse = """cannot unmarshal"""

BGP18_reqMethod = "PATCH"
BGP18_objURL = """/public/v1/config/BGPGlobal"""                            #Disabled
BGP18_payload = """{"Vrf" : "default","Disabled": false}"""       
BGP18_ExpectedResponse = """Error"""
		
BGP19_reqMethod = "PATCH"
BGP19_objURL = """/public/v1/config/BGPGlobal"""                            #Disabled
BGP19_payload = """{"Vrf" : "default","Disabled": true}"""       
BGP19_ExpectedResponse = """Success"""
	
BGP20_reqMethod = "PATCH"
BGP20_objURL = """/public/v1/config/BGPGlobal"""                            #Disabled
BGP20_payload = """{"Vrf" : "default","Disabled": false}"""       
BGP20_ExpectedResponse = """Error"""

#BGPv4Neighbor

BGP21_reqMethod = "POST"
BGP21_objURL = """/public/v1/config/BGPv4Neighbor"""                            #NeighborAddress
BGP21_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1"}"""    
BGP21_ExpectedResponse = """Success"""

BGP22_reqMethod = "POST"
BGP22_objURL = """/public/v1/config/BGPv4Neighbor"""                            #NeighborAddress
BGP22_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1"}"""    
BGP22_ExpectedResponse = """Error"""

BGP23_reqMethod = "PATCH"
BGP23_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP23_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1"}"""    
BGP23_ExpectedResponse = """Error"""

BGP24_reqMethod = "PATCH"
BGP24_objURL = """/public/v1/config/BGPv4Neighbor"""                            #NeighborAddress
BGP24_payload = """{"NeighborAddress" : "192.168.0.256", "IntfRef" : "DUT1_P1"}"""    
BGP24_ExpectedResponse = """Error"""

BGP25_reqMethod = "PATCH"
BGP25_objURL = """/public/v1/config/BGPv4Neighbor"""                            #NeighborAddress
BGP25_payload = """{"NeighborAddress" : "192.168.0", "IntfRef" : "DUT1_P1"}"""    
BGP25_ExpectedResponse = """Error"""

BGP26_reqMethod = "PATCH"
BGP26_objURL = """/public/v1/config/BGPv4Neighbor"""                            #NeighborAddress
BGP26_payload = """{"NeighborAddress" : "192.168.0", "IntfRef" : "DUT1_P1"}"""    
BGP26_ExpectedResponse = """Error"""

BGP27_reqMethod = "PATCH"
BGP27_objURL = """/public/v1/config/BGPv4Neighbor"""                            #Intfef(invalid)
BGP27_payload = """{"NeighborAddress" : "192.168.0", "IntfRef" : "DUT1_P3"}"""    
BGP27_ExpectedResponse = """Error"""

BGP28_reqMethod = "PATCH"
BGP28_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP28_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","PeerAS" : "200"}"""    
BGP28_ExpectedResponse = """Success"""

BGP29_reqMethod = "PATCH"
BGP29_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP29_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","PeerAS" : "200"}"""    
BGP29_ExpectedResponse = """Success"""

BGP30_reqMethod = "PATCH"
BGP30_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP30_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","PeerAS" : "200","MaxPrefixesDisconnect":false}"""    
BGP30_ExpectedResponse = """Error"""

BGP31_reqMethod = "PATCH"
BGP31_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP31_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MaxPrefixesDisconnect":true}"""    
BGP31_ExpectedResponse = """Success"""

BGP32_reqMethod = "PATCH"
BGP32_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP32_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MaxPrefixesDisconnect":false}"""    
BGP32_ExpectedResponse = """Success"""

BGP33_reqMethod = "PATCH"
BGP33_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP33_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","LocalAS" : "201"}"""    
BGP33_ExpectedResponse = """Success"""

BGP34_reqMethod = "PATCH"
BGP34_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP34_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MaxPrefixesThresholdPct" : 0}"""    
BGP34_ExpectedResponse = """Error"""

BGP35_reqMethod = "PATCH"
BGP35_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP35_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MaxPrefixesThresholdPct" : 254}"""    
BGP35_ExpectedResponse = """Success"""

BGP36_reqMethod = "PATCH"
BGP36_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP36_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MaxPrefixesThresholdPct" : 258}"""    
BGP36_ExpectedResponse = """cannot unmarshal"""

BGP37_reqMethod = "PATCH"
BGP37_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP37_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MaxPrefixesThresholdPct" : 258}"""    
BGP37_ExpectedResponse = """cannot unmarshal"""

BGP38_reqMethod = "PATCH"
BGP38_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP38_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","Description" : "This is for testing"}"""    
BGP38_ExpectedResponse = """Success"""

BGP39_reqMethod = "PATCH"
BGP39_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP39_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MultiHopEnable" : false}"""    
BGP39_ExpectedResponse = """Error"""

BGP40_reqMethod = "PATCH"
BGP40_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP40_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MultiHopEnable" : true}"""    
BGP40_ExpectedResponse = """Success"""

BGP41_reqMethod = "PATCH"
BGP41_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP41_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","MultiHopEnable" : false}"""    
BGP41_ExpectedResponse = """Success"""

BGP42_reqMethod = "PATCH"
BGP42_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP42_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","RouteReflectorClient" : false}"""    
BGP42_ExpectedResponse = """Error"""

BGP43_reqMethod = "PATCH"
BGP43_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP43_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","RouteReflectorClient" : true}"""    
BGP43_ExpectedResponse = """Success"""

BGP44_reqMethod = "PATCH"
BGP44_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP44_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","RouteReflectorClient" : false}"""    
BGP44_ExpectedResponse = """Success"""

BGP45_reqMethod = "PATCH"
BGP45_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP45_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","NextHopSelf" : false}"""    
BGP45_ExpectedResponse = """Error"""

BGP46_reqMethod = "PATCH"
BGP46_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP46_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","NextHopSelf" : true}"""    
BGP46_ExpectedResponse = """Success"""

BGP47_reqMethod = "PATCH"
BGP47_objURL = """/public/v1/config/BGPv4Neighbor"""                            
BGP47_payload = """{"NeighborAddress" : "192.168.0.2", "IntfRef" : "DUT1_P1","NextHopSelf" : false}"""    
BGP47_ExpectedResponse = """Success"""

BGP48_reqMethod = "PATCH"
BGP48_objURL = "/public/v1/config/BGPv4Neighbor"
BGP48_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"DUT1_P1","Disabled":false}"""   #updating using same default values
BGP48_ExpectedResponse = "Error"

BGP49_reqMethod = "PATCH"
BGP49_objURL = "/public/v1/config/BGPv4Neighbor"
BGP49_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"DUT1_P1","Disabled":true}"""    #updating
BGP49_ExpectedResponse = "Success"

BGP50_reqMethod = "PATCH"
BGP50_objURL = "/public/v1/config/BGPv4Neighbor"
BGP50_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"DUT1_P1","Disabled":false}"""    #Updating again to  default value
BGP50_ExpectedResponse = "Success"


BGP51_reqMethod = "DELETE"
BGP51_objURL = "/public/v1/config/BGPv4Neighbor"
BGP51_payload = """{"NeighborAddress":"192.168.0.2","IntfRef":"DUT1_P1"}"""                          #Trying to delete an entry
BGP51_ExpectedResponse = "Success"

BGP52_reqMethod = "DELETE"
BGP52_objURL = "/public/v1/config/BGPv4Neighbor"
BGP52_payload = """{"NeighborAddress":"192.168.0.2","IntfRef":"DUT1_P1"}"""                          #Trying to Re-Delete an entry
BGP52_ExpectedResponse = "Error"


#Clean up parameters
CP1_reqMethod = "DELETE"
CP1_objURL = """/public/v1/config/IPv4Intf"""
CP1_payload = """{"IntfRef":"DUT1_P1"}"""
CP1_ExpectedResponse = "Success"

CP2_reqMethod = "DELETE"
CP2_objURL = """/public/v1/config/IPv4Intf"""
CP2_payload = """{"IntfRef":"DUT_P2"}"""
CP2_ExpectedResponse = "Success"

CP3_reqMethod = "PATCH"
CP3_objURL = """/public/v1/config/BGPGlobal"""
CP3_payload = """{"ASNum":"200","RouterId":"1.1.1.1","Disabled":true}"""
CP3_ExpectedResponse = "Success"

CP4_reqMethod = "DELETE"
CP4_objURL = """/public/v1/config/BGPv4Neighbor"""
CP4_payload = """{"NeighborAddress":"192.168.0.2","IntfRef":"DUT1_P1"}"""
CP4_ExpectedResponse = "Success"









































