from functools import partial
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.node import OVSController


#from ryu.topology import event, switches
#from ryu.topology.api import get_switch, get_link

class myTopo(Topo):
#function that creates topology
  def __init__(self):
    #net = Mininet()
    try:
      #create an empty topology 
      topo = Topo()
      
      # Initialize topology
      Topo.__init__( self )
      
      # Add hosts and switches
      h1 = self.addHost( 'h1' )    #attached to s1
      h2 = self.addHost( 'h2' )    #attached to s6      
      '''
      h3 = self.addHost( 'h3' )    #attached to s2
      h4 = self.addHost( 'h4' )    #attached to s3
      h5 = self.addHost( 'h5' )    #attached to s4
      h6 = self.addHost( 'h6' )    #attached to s5
      '''
            
      s1 = self.addSwitch( 's1' )
      s2 = self.addSwitch( 's2' )
      s3 = self.addSwitch( 's3' )
      s4 = self.addSwitch( 's4' )
      s5 = self.addSwitch( 's5' )
      s6 = self.addSwitch( 's6' )

      # add host links
      self.addLink(h1, s1)
      self.addLink(h2, s6)
      '''
      self.addLink(h3, s2)
      self.addLink(h4, s3)
      self.addLink(h5, s4)
      self.addLink(h6, s5)
      '''      
      
      # add switch links
      self.addLink(s1, s2, bw = 15)  #link a to b
      self.addLink(s1, s3, bw = 16)  #link a to c
      self.addLink(s2, s3)  #link b to c
      self.addLink(s1, s4, bw = 5)  #link a to d  
      self.addLink(s2, s4, bw = 10)  #link c to d
      self.addLink(s3, s4, bw = 14)
      self.addLink(s3, s5, bw = 12)  
      self.addLink(s4, s5)  #link d to e
      self.addLink(s4, s6, bw = 18)
      self.addLink(s5, s6, bw = 14)
      
      
    except Exception as ex:
      print("Error: " + str(ex))
      pass
    finally:
      #net.stop()
      pass
  
topos = { 'mytopo': ( lambda: myTopo() ) }
