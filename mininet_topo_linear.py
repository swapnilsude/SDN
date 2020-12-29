
from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host=['h{}'.format(i) for i in range(1, 21)]
        switch=['s{}'.format(i) for i in range(1, 21)]

        for i in host:
            globals()[i] = self.addHost( i )

        for i in switch:
            globals()[i] = self.addSwitch( i )

        # Add links
        for i in range(0,20):
            temp=(str((i+1)*10)+'ms')
            temp2={'delay':temp}
            self.addLink( host[i], switch[i], cls=TCLink , **temp2 )
            if (i<19):
                temp3={'delay':'5ms'}
                self.addLink( switch[i], switch[i+1], cls=TCLink , **temp3 )

topos = { 'mytopo': ( lambda: MyTopo() ) }

