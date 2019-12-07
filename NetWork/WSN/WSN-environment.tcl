# This script is created by NSG2 beta1
# <http://wushoupong.googlepages.com/nsg>

#===================================
#     Simulation parameters setup
#===================================
set val(chan)   Channel/WirelessChannel    ;# channel type
set val(prop)   Propagation/TwoRayGround   ;# radio-propagation model
set val(netif)  Phy/WirelessPhy            ;# network interface type
set val(mac)    Mac/802_11                 ;# MAC type
set val(ifq)    Queue/DropTail/PriQueue    ;# interface queue type
set val(ll)     LL                         ;# link layer type
set val(ant)    Antenna/OmniAntenna        ;# antenna model
set val(ifqlen) 50                         ;# max packet in ifq
set val(nn)     43                         ;# number of mobilenodes
set val(rp)     DSDV                       ;# routing protocol
set val(x)      7741                      ;# X dimension of topography
set val(y)      100                      ;# Y dimension of topography
set val(stop)   180.0                         ;# time of simulation end

#===================================
#        Initialization        
#===================================
#Create a ns simulator
set ns [new Simulator]

#Setup topography object
set topo       [new Topography]
$topo load_flatgrid $val(x) $val(y)
create-god $val(nn)

#Open the NS trace file
set tracefile [open out.tr w]
$ns trace-all $tracefile

#Open the NAM trace file
set namfile [open out.nam w]
$ns namtrace-all $namfile
$ns namtrace-all-wireless $namfile $val(x) $val(y)
set chan [new $val(chan)];#Create wireless channel

#===================================
#     Mobile node parameter setup
#===================================
$ns node-config -adhocRouting  $val(rp) \
                -llType        $val(ll) \
                -macType       $val(mac) \
                -ifqType       $val(ifq) \
                -ifqLen        $val(ifqlen) \
                -antType       $val(ant) \
                -propType      $val(prop) \
                -phyType       $val(netif) \
                -channel       $chan \
                -topoInstance  $topo \
                -agentTrace    ON \
                -routerTrace   ON \
                -macTrace      ON \
                -movementTrace ON

#===================================
#        Nodes Definition        
#===================================
#Create 43 nodes
set n0 [$ns node]
$n0 set X_ 3500
$n0 set Y_ 2500
$n0 set Z_ 0.0
$ns initial_node_pos $n0 20
set n1 [$ns node]
$n1 set X_ 3600
$n1 set Y_ 2500
$n1 set Z_ 0.0
$ns initial_node_pos $n1 20
set n2 [$ns node]
$n2 set X_ 3500
$n2 set Y_ 2300
$n2 set Z_ 0.0
$ns initial_node_pos $n2 20
set n3 [$ns node]
$n3 set X_ 3600
$n3 set Y_ 2300
$n3 set Z_ 0.0
$ns initial_node_pos $n3 20
set n4 [$ns node]
$n4 set X_ 3500
$n4 set Y_ 2100
$n4 set Z_ 0.0
$ns initial_node_pos $n4 20
set n5 [$ns node]
$n5 set X_ 3600
$n5 set Y_ 2100
$n5 set Z_ 0.0
$ns initial_node_pos $n5 20
set n6 [$ns node]
$n6 set X_ 3500
$n6 set Y_ 1900
$n6 set Z_ 0.0
$ns initial_node_pos $n6 20
set n7 [$ns node]
$n7 set X_ 3600
$n7 set Y_ 1900
$n7 set Z_ 0.0
$ns initial_node_pos $n7 20
set n8 [$ns node]
$n8 set X_ 3500
$n8 set Y_ 1700
$n8 set Z_ 0.0
$ns initial_node_pos $n8 20
set n9 [$ns node]
$n9 set X_ 3600
$n9 set Y_ 1700
$n9 set Z_ 0.0
$ns initial_node_pos $n9 20
set n10 [$ns node]
$n10 set X_ 3500
$n10 set Y_ 1500
$n10 set Z_ 0.0
$ns initial_node_pos $n10 20
set n11 [$ns node]
$n11 set X_ 3600
$n11 set Y_ 1500
$n11 set Z_ 0.0
$ns initial_node_pos $n11 20
set n12 [$ns node]
$n12 set X_ 3500
$n12 set Y_ 1300
$n12 set Z_ 0.0
$ns initial_node_pos $n12 20
set n13 [$ns node]
$n13 set X_ 3600
$n13 set Y_ 1300
$n13 set Z_ 0.0
$ns initial_node_pos $n13 20
set n14 [$ns node]
$n14 set X_ 3500
$n14 set Y_ 1100
$n14 set Z_ 0.0
$ns initial_node_pos $n14 20
set n15 [$ns node]
$n15 set X_ 3600
$n15 set Y_ 1100
$n15 set Z_ 0.0
$ns initial_node_pos $n15 20
set n16 [$ns node]
$n16 set X_ 3798
$n16 set Y_ 2598
$n16 set Z_ 0.0
$ns initial_node_pos $n16 20
set n17 [$ns node]
$n17 set X_ 3998
$n17 set Y_ 2598
$n17 set Z_ 0.0
$ns initial_node_pos $n17 20
set n18 [$ns node]
$n18 set X_ 4198
$n18 set Y_ 2598
$n18 set Z_ 0.0
$ns initial_node_pos $n18 20
set n19 [$ns node]
$n19 set X_ 3798
$n19 set Y_ 2498
$n19 set Z_ 0.0
$ns initial_node_pos $n19 20
set n20 [$ns node]
$n20 set X_ 3998
$n20 set Y_ 2498
$n20 set Z_ 0.0
$ns initial_node_pos $n20 20
set n21 [$ns node]
$n21 set X_ 4198
$n21 set Y_ 2498
$n21 set Z_ 0.0
$ns initial_node_pos $n21 20
set n22 [$ns node]
$n22 set X_ 3798
$n22 set Y_ 2398
$n22 set Z_ 0.0
$ns initial_node_pos $n22 20
set n23 [$ns node]
$n23 set X_ 3998
$n23 set Y_ 2398
$n23 set Z_ 0.0
$ns initial_node_pos $n23 20
set n24 [$ns node]
$n24 set X_ 4198
$n24 set Y_ 2398
$n24 set Z_ 0.0
$ns initial_node_pos $n24 20
set n25 [$ns node]
$n25 set X_ 3798
$n25 set Y_ 1898
$n25 set Z_ 0.0
$ns initial_node_pos $n25 20
set n26 [$ns node]
$n26 set X_ 3998
$n26 set Y_ 1898
$n26 set Z_ 0.0
$ns initial_node_pos $n26 20
set n27 [$ns node]
$n27 set X_ 4198
$n27 set Y_ 1898
$n27 set Z_ 0.0
$ns initial_node_pos $n27 20
set n28 [$ns node]
$n28 set X_ 3798
$n28 set Y_ 1798
$n28 set Z_ 0.0
$ns initial_node_pos $n28 20
set n29 [$ns node]
$n29 set X_ 3998
$n29 set Y_ 1798
$n29 set Z_ 0.0
$ns initial_node_pos $n29 20
set n30 [$ns node]
$n30 set X_ 4198
$n30 set Y_ 1798
$n30 set Z_ 0.0
$ns initial_node_pos $n30 20
set n31 [$ns node]
$n31 set X_ 3798
$n31 set Y_ 1698
$n31 set Z_ 0.0
$ns initial_node_pos $n31 20
set n32 [$ns node]
$n32 set X_ 3998
$n32 set Y_ 1698
$n32 set Z_ 0.0
$ns initial_node_pos $n32 20
set n33 [$ns node]
$n33 set X_ 4198
$n33 set Y_ 1698
$n33 set Z_ 0.0
$ns initial_node_pos $n33 20
set n34 [$ns node]
$n34 set X_ 3803
$n34 set Y_ 1296
$n34 set Z_ 0.0
$ns initial_node_pos $n34 20
set n35 [$ns node]
$n35 set X_ 4003
$n35 set Y_ 1296
$n35 set Z_ 0.0
$ns initial_node_pos $n35 20
set n36 [$ns node]
$n36 set X_ 4203
$n36 set Y_ 1296
$n36 set Z_ 0.0
$ns initial_node_pos $n36 20
set n37 [$ns node]
$n37 set X_ 3803
$n37 set Y_ 1196
$n37 set Z_ 0.0
$ns initial_node_pos $n37 20
set n38 [$ns node]
$n38 set X_ 4003
$n38 set Y_ 1196
$n38 set Z_ 0.0
$ns initial_node_pos $n38 20
set n39 [$ns node]
$n39 set X_ 4203
$n39 set Y_ 1196
$n39 set Z_ 0.0
$ns initial_node_pos $n39 20
set n40 [$ns node]
$n40 set X_ 3803
$n40 set Y_ 1096
$n40 set Z_ 0.0
$ns initial_node_pos $n40 20
set n41 [$ns node]
$n41 set X_ 4003
$n41 set Y_ 1096
$n41 set Z_ 0.0
$ns initial_node_pos $n41 20
set n42 [$ns node]
$n42 set X_ 4203
$n42 set Y_ 1096
$n42 set Z_ 0.0
$ns initial_node_pos $n42 20

#===================================
#        Agents Definition        
#===================================
#Setup a TCP connection
set tcp0 [new Agent/TCP]
$ns attach-agent $n42 $tcp0
set sink107 [new Agent/TCPSink]
$ns attach-agent $n10 $sink107
$ns connect $tcp0 $sink107
$tcp0 set packetSize_ 1500

#Setup a TCP connection
set tcp1 [new Agent/TCP]
$ns attach-agent $n42 $tcp1
set sink109 [new Agent/TCPSink]
$ns attach-agent $n10 $sink109
$ns connect $tcp1 $sink109
$tcp1 set packetSize_ 1500

#Setup a TCP connection
set tcp2 [new Agent/TCP]
$ns attach-agent $n39 $tcp2
set sink61 [new Agent/TCPSink]
$ns attach-agent $n4 $sink61
$ns connect $tcp2 $sink61
$tcp2 set packetSize_ 1500

#Setup a TCP connection
set tcp3 [new Agent/TCP]
$ns attach-agent $n39 $tcp3
set sink103 [new Agent/TCPSink]
$ns attach-agent $n10 $sink103
$ns connect $tcp3 $sink103
$tcp3 set packetSize_ 1500

#Setup a TCP connection
set tcp4 [new Agent/TCP]
$ns attach-agent $n36 $tcp4
set sink79 [new Agent/TCPSink]
$ns attach-agent $n4 $sink79
$ns connect $tcp4 $sink79
$tcp4 set packetSize_ 1500

#Setup a TCP connection
set tcp5 [new Agent/TCP]
$ns attach-agent $n36 $tcp5
set sink78 [new Agent/TCPSink]
$ns attach-agent $n4 $sink78
$ns connect $tcp5 $sink78
$tcp5 set packetSize_ 1500

#Setup a TCP connection
set tcp6 [new Agent/TCP]
$ns attach-agent $n41 $tcp6
set sink104 [new Agent/TCPSink]
$ns attach-agent $n10 $sink104
$ns connect $tcp6 $sink104
$tcp6 set packetSize_ 1500

#Setup a TCP connection
set tcp7 [new Agent/TCP]
$ns attach-agent $n41 $tcp7
set sink108 [new Agent/TCPSink]
$ns attach-agent $n10 $sink108
$ns connect $tcp7 $sink108
$tcp7 set packetSize_ 1500

#Setup a TCP connection
set tcp8 [new Agent/TCP]
$ns attach-agent $n40 $tcp8
set sink106 [new Agent/TCPSink]
$ns attach-agent $n10 $sink106
$ns connect $tcp8 $sink106
$tcp8 set packetSize_ 1500

#Setup a TCP connection
set tcp9 [new Agent/TCP]
$ns attach-agent $n40 $tcp9
set sink105 [new Agent/TCPSink]
$ns attach-agent $n10 $sink105
$ns connect $tcp9 $sink105
$tcp9 set packetSize_ 1500

#Setup a TCP connection
set tcp10 [new Agent/TCP]
$ns attach-agent $n34 $tcp10
set sink68 [new Agent/TCPSink]
$ns attach-agent $n4 $sink68
$ns connect $tcp10 $sink68
$tcp10 set packetSize_ 1500

#Setup a TCP connection
set tcp11 [new Agent/TCP]
$ns attach-agent $n34 $tcp11
set sink81 [new Agent/TCPSink]
$ns attach-agent $n4 $sink81
$ns connect $tcp11 $sink81
$tcp11 set packetSize_ 1500

#Setup a TCP connection
set tcp12 [new Agent/TCP]
$ns attach-agent $n35 $tcp12
set sink64 [new Agent/TCPSink]
$ns attach-agent $n4 $sink64
$ns connect $tcp12 $sink64
$tcp12 set packetSize_ 1500

#Setup a TCP connection
set tcp13 [new Agent/TCP]
$ns attach-agent $n35 $tcp13
set sink80 [new Agent/TCPSink]
$ns attach-agent $n4 $sink80
$ns connect $tcp13 $sink80
$tcp13 set packetSize_ 1500

#Setup a TCP connection
set tcp14 [new Agent/TCP]
$ns attach-agent $n38 $tcp14
set sink62 [new Agent/TCPSink]
$ns attach-agent $n4 $sink62
$ns connect $tcp14 $sink62
$tcp14 set packetSize_ 1500

#Setup a TCP connection
set tcp15 [new Agent/TCP]
$ns attach-agent $n38 $tcp15
set sink102 [new Agent/TCPSink]
$ns attach-agent $n10 $sink102
$ns connect $tcp15 $sink102
$tcp15 set packetSize_ 1500

#Setup a TCP connection
set tcp16 [new Agent/TCP]
$ns attach-agent $n37 $tcp16
set sink63 [new Agent/TCPSink]
$ns attach-agent $n4 $sink63
$ns connect $tcp16 $sink63
$tcp16 set packetSize_ 1500

#Setup a TCP connection
set tcp17 [new Agent/TCP]
$ns attach-agent $n37 $tcp17
set sink101 [new Agent/TCPSink]
$ns attach-agent $n10 $sink101
$ns connect $tcp17 $sink101
$tcp17 set packetSize_ 1500

#Setup a TCP connection
set tcp18 [new Agent/TCP]
$ns attach-agent $n31 $tcp18
set sink100 [new Agent/TCPSink]
$ns attach-agent $n10 $sink100
$ns connect $tcp18 $sink100
$tcp18 set packetSize_ 1500

#Setup a TCP connection
set tcp19 [new Agent/TCP]
$ns attach-agent $n31 $tcp19
set sink99 [new Agent/TCPSink]
$ns attach-agent $n10 $sink99
$ns connect $tcp19 $sink99
$tcp19 set packetSize_ 1500

#Setup a TCP connection
set tcp20 [new Agent/TCP]
$ns attach-agent $n32 $tcp20
set sink98 [new Agent/TCPSink]
$ns attach-agent $n10 $sink98
$ns connect $tcp20 $sink98
$tcp20 set packetSize_ 1500

#Setup a TCP connection
set tcp21 [new Agent/TCP]
$ns attach-agent $n32 $tcp21
set sink97 [new Agent/TCPSink]
$ns attach-agent $n10 $sink97
$ns connect $tcp21 $sink97
$tcp21 set packetSize_ 1500

#Setup a TCP connection
set tcp22 [new Agent/TCP]
$ns attach-agent $n33 $tcp22
set sink96 [new Agent/TCPSink]
$ns attach-agent $n10 $sink96
$ns connect $tcp22 $sink96
$tcp22 set packetSize_ 1500

#Setup a TCP connection
set tcp23 [new Agent/TCP]
$ns attach-agent $n33 $tcp23
set sink95 [new Agent/TCPSink]
$ns attach-agent $n10 $sink95
$ns connect $tcp23 $sink95
$tcp23 set packetSize_ 1500

#Setup a TCP connection
set tcp24 [new Agent/TCP]
$ns attach-agent $n30 $tcp24
set sink82 [new Agent/TCPSink]
$ns attach-agent $n4 $sink82
$ns connect $tcp24 $sink82
$tcp24 set packetSize_ 1500

#Setup a TCP connection
set tcp25 [new Agent/TCP]
$ns attach-agent $n30 $tcp25
set sink92 [new Agent/TCPSink]
$ns attach-agent $n10 $sink92
$ns connect $tcp25 $sink92
$tcp25 set packetSize_ 1500

#Setup a TCP connection
set tcp26 [new Agent/TCP]
$ns attach-agent $n28 $tcp26
set sink71 [new Agent/TCPSink]
$ns attach-agent $n4 $sink71
$ns connect $tcp26 $sink71
$tcp26 set packetSize_ 1500

#Setup a TCP connection
set tcp27 [new Agent/TCP]
$ns attach-agent $n28 $tcp27
set sink94 [new Agent/TCPSink]
$ns attach-agent $n10 $sink94
$ns connect $tcp27 $sink94
$tcp27 set packetSize_ 1500

#Setup a TCP connection
set tcp29 [new Agent/TCP]
$ns attach-agent $n29 $tcp29
set sink70 [new Agent/TCPSink]
$ns attach-agent $n4 $sink70
$ns connect $tcp29 $sink70
$tcp29 set packetSize_ 1500

#Setup a TCP connection
set tcp30 [new Agent/TCP]
$ns attach-agent $n29 $tcp30
set sink93 [new Agent/TCPSink]
$ns attach-agent $n10 $sink93
$ns connect $tcp30 $sink93
$tcp30 set packetSize_ 1500

#Setup a TCP connection
set tcp31 [new Agent/TCP]
$ns attach-agent $n25 $tcp31
set sink76 [new Agent/TCPSink]
$ns attach-agent $n4 $sink76
$ns connect $tcp31 $sink76
$tcp31 set packetSize_ 1500

#Setup a TCP connection
set tcp32 [new Agent/TCP]
$ns attach-agent $n25 $tcp32
set sink75 [new Agent/TCPSink]
$ns attach-agent $n4 $sink75
$ns connect $tcp32 $sink75
$tcp32 set packetSize_ 1500

#Setup a TCP connection
set tcp33 [new Agent/TCP]
$ns attach-agent $n26 $tcp33
set sink77 [new Agent/TCPSink]
$ns attach-agent $n4 $sink77
$ns connect $tcp33 $sink77
$tcp33 set packetSize_ 1500

#Setup a TCP connection
set tcp34 [new Agent/TCP]
$ns attach-agent $n26 $tcp34
set sink74 [new Agent/TCPSink]
$ns attach-agent $n4 $sink74
$ns connect $tcp34 $sink74
$tcp34 set packetSize_ 1500

#Setup a TCP connection
set tcp35 [new Agent/TCP]
$ns attach-agent $n27 $tcp35
set sink73 [new Agent/TCPSink]
$ns attach-agent $n4 $sink73
$ns connect $tcp35 $sink73
$tcp35 set packetSize_ 1500

#Setup a TCP connection
set tcp36 [new Agent/TCP]
$ns attach-agent $n27 $tcp36
set sink72 [new Agent/TCPSink]
$ns attach-agent $n4 $sink72
$ns connect $tcp36 $sink72
$tcp36 set packetSize_ 1500

#Setup a TCP connection
set tcp37 [new Agent/TCP]
$ns attach-agent $n16 $tcp37
set sink60 [new Agent/TCPSink]
$ns attach-agent $n4 $sink60
$ns connect $tcp37 $sink60
$tcp37 set packetSize_ 1500

#Setup a TCP connection
set tcp38 [new Agent/TCP]
$ns attach-agent $n16 $tcp38
set sink59 [new Agent/TCPSink]
$ns attach-agent $n4 $sink59
$ns connect $tcp38 $sink59
$tcp38 set packetSize_ 1500

#Setup a TCP connection
set tcp39 [new Agent/TCP]
$ns attach-agent $n19 $tcp39
set sink66 [new Agent/TCPSink]
$ns attach-agent $n4 $sink66
$ns connect $tcp39 $sink66
$tcp39 set packetSize_ 1500

#Setup a TCP connection
set tcp40 [new Agent/TCP]
$ns attach-agent $n19 $tcp40
set sink91 [new Agent/TCPSink]
$ns attach-agent $n10 $sink91
$ns connect $tcp40 $sink91
$tcp40 set packetSize_ 1500

#Setup a TCP connection
set tcp42 [new Agent/TCP]
$ns attach-agent $n22 $tcp42
set sink88 [new Agent/TCPSink]
$ns attach-agent $n10 $sink88
$ns connect $tcp42 $sink88
$tcp42 set packetSize_ 1500

#Setup a TCP connection
set tcp43 [new Agent/TCP]
$ns attach-agent $n22 $tcp43
set sink87 [new Agent/TCPSink]
$ns attach-agent $n10 $sink87
$ns connect $tcp43 $sink87
$tcp43 set packetSize_ 1500

#Setup a TCP connection
set tcp44 [new Agent/TCP]
$ns attach-agent $n23 $tcp44
set sink86 [new Agent/TCPSink]
$ns attach-agent $n10 $sink86
$ns connect $tcp44 $sink86
$tcp44 set packetSize_ 1500

#Setup a TCP connection
set tcp45 [new Agent/TCP]
$ns attach-agent $n23 $tcp45
set sink85 [new Agent/TCPSink]
$ns attach-agent $n10 $sink85
$ns connect $tcp45 $sink85
$tcp45 set packetSize_ 1500

#Setup a TCP connection
set tcp46 [new Agent/TCP]
$ns attach-agent $n24 $tcp46
set sink84 [new Agent/TCPSink]
$ns attach-agent $n10 $sink84
$ns connect $tcp46 $sink84
$tcp46 set packetSize_ 1500

#Setup a TCP connection
set tcp47 [new Agent/TCP]
$ns attach-agent $n24 $tcp47
set sink83 [new Agent/TCPSink]
$ns attach-agent $n10 $sink83
$ns connect $tcp47 $sink83
$tcp47 set packetSize_ 1500

#Setup a TCP connection
set tcp48 [new Agent/TCP]
$ns attach-agent $n20 $tcp48
set sink69 [new Agent/TCPSink]
$ns attach-agent $n4 $sink69
$ns connect $tcp48 $sink69
$tcp48 set packetSize_ 1500

#Setup a TCP connection
set tcp49 [new Agent/TCP]
$ns attach-agent $n20 $tcp49
set sink90 [new Agent/TCPSink]
$ns attach-agent $n10 $sink90
$ns connect $tcp49 $sink90
$tcp49 set packetSize_ 1500

#Setup a TCP connection
set tcp50 [new Agent/TCP]
$ns attach-agent $n17 $tcp50
set sink58 [new Agent/TCPSink]
$ns attach-agent $n4 $sink58
$ns connect $tcp50 $sink58
$tcp50 set packetSize_ 1500

#Setup a TCP connection
set tcp51 [new Agent/TCP]
$ns attach-agent $n17 $tcp51
set sink57 [new Agent/TCPSink]
$ns attach-agent $n4 $sink57
$ns connect $tcp51 $sink57
$tcp51 set packetSize_ 1500

#Setup a TCP connection
set tcp52 [new Agent/TCP]
$ns attach-agent $n18 $tcp52
set sink56 [new Agent/TCPSink]
$ns attach-agent $n4 $sink56
$ns connect $tcp52 $sink56
$tcp52 set packetSize_ 1500

#Setup a TCP connection
set tcp53 [new Agent/TCP]
$ns attach-agent $n18 $tcp53
set sink67 [new Agent/TCPSink]
$ns attach-agent $n4 $sink67
$ns connect $tcp53 $sink67
$tcp53 set packetSize_ 1500

#Setup a TCP connection
set tcp54 [new Agent/TCP]
$ns attach-agent $n21 $tcp54
set sink65 [new Agent/TCPSink]
$ns attach-agent $n4 $sink65
$ns connect $tcp54 $sink65
$tcp54 set packetSize_ 1500

#Setup a TCP connection
set tcp55 [new Agent/TCP]
$ns attach-agent $n21 $tcp55
set sink89 [new Agent/TCPSink]
$ns attach-agent $n10 $sink89
$ns connect $tcp55 $sink89
$tcp55 set packetSize_ 1500


#===================================
#        Applications Definition        
#===================================
#Setup a FTP Application over TCP connection
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp37
$ns at 100.0 "$ftp0 start"
$ns at 125.0 "$ftp0 stop"

#Setup a FTP Application over TCP connection
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp38
$ns at 100.0 "$ftp1 start"
$ns at 125.0 "$ftp1 stop"

#Setup a FTP Application over TCP connection
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp50
$ns at 100.0 "$ftp2 start"
$ns at 125.0 "$ftp2 stop"

#Setup a FTP Application over TCP connection
set ftp3 [new Application/FTP]
$ftp3 attach-agent $tcp51
$ns at 100.0 "$ftp3 start"
$ns at 125.0 "$ftp3 stop"

#Setup a FTP Application over TCP connection
set ftp4 [new Application/FTP]
$ftp4 attach-agent $tcp52
$ns at 100.0 "$ftp4 start"
$ns at 125.0 "$ftp4 stop"

#Setup a FTP Application over TCP connection
set ftp5 [new Application/FTP]
$ftp5 attach-agent $tcp53
$ns at 100.0 "$ftp5 start"
$ns at 125.0 "$ftp5 stop"

#Setup a FTP Application over TCP connection
set ftp6 [new Application/FTP]
$ftp6 attach-agent $tcp39
$ns at 100.0 "$ftp6 start"
$ns at 125.0 "$ftp6 stop"

#Setup a FTP Application over TCP connection
set ftp7 [new Application/FTP]
$ftp7 attach-agent $tcp40
$ns at 100.0 "$ftp7 start"
$ns at 125.0 "$ftp7 stop"

#Setup a FTP Application over TCP connection
set ftp8 [new Application/FTP]
$ftp8 attach-agent $tcp48
$ns at 100.0 "$ftp8 start"
$ns at 125.0 "$ftp8 stop"

#Setup a FTP Application over TCP connection
set ftp9 [new Application/FTP]
$ftp9 attach-agent $tcp49
$ns at 100.0 "$ftp9 start"
$ns at 125.0 "$ftp9 stop"

#Setup a FTP Application over TCP connection
set ftp10 [new Application/FTP]
$ftp10 attach-agent $tcp54
$ns at 100.0 "$ftp10 start"
$ns at 125.0 "$ftp10 stop"

#Setup a FTP Application over TCP connection
set ftp11 [new Application/FTP]
$ftp11 attach-agent $tcp55
$ns at 100.0 "$ftp11 start"
$ns at 125.0 "$ftp11 stop"

#Setup a FTP Application over TCP connection
set ftp12 [new Application/FTP]
$ftp12 attach-agent $tcp44
$ns at 100.0 "$ftp12 start"
$ns at 125.0 "$ftp12 stop"

#Setup a FTP Application over TCP connection
set ftp13 [new Application/FTP]
$ftp13 attach-agent $tcp45
$ns at 100.0 "$ftp13 start"
$ns at 125.0 "$ftp13 stop"

#Setup a FTP Application over TCP connection
set ftp14 [new Application/FTP]
$ftp14 attach-agent $tcp42
$ns at 100.0 "$ftp14 start"
$ns at 125.0 "$ftp14 stop"

#Setup a FTP Application over TCP connection
set ftp15 [new Application/FTP]
$ftp15 attach-agent $tcp43
$ns at 100.0 "$ftp15 start"
$ns at 125.0 "$ftp15 stop"

#Setup a FTP Application over TCP connection
set ftp16 [new Application/FTP]
$ftp16 attach-agent $tcp46
$ns at 100.0 "$ftp16 start"
$ns at 125.0 "$ftp16 stop"

#Setup a FTP Application over TCP connection
set ftp17 [new Application/FTP]
$ftp17 attach-agent $tcp47
$ns at 100.0 "$ftp17 start"
$ns at 125.0 "$ftp17 stop"

#Setup a FTP Application over TCP connection
set ftp18 [new Application/FTP]
$ftp18 attach-agent $tcp31
$ns at 125.0 "$ftp18 start"
$ns at 150.0 "$ftp18 stop"

#Setup a FTP Application over TCP connection
set ftp19 [new Application/FTP]
$ftp19 attach-agent $tcp32
$ns at 125.0 "$ftp19 start"
$ns at 150.0 "$ftp19 stop"

#Setup a FTP Application over TCP connection
set ftp20 [new Application/FTP]
$ftp20 attach-agent $tcp33
$ns at 125.0 "$ftp20 start"
$ns at 150.0 "$ftp20 stop"

#Setup a FTP Application over TCP connection
set ftp21 [new Application/FTP]
$ftp21 attach-agent $tcp34
$ns at 125.0 "$ftp21 start"
$ns at 150.0 "$ftp21 stop"

#Setup a FTP Application over TCP connection
set ftp22 [new Application/FTP]
$ftp22 attach-agent $tcp35
$ns at 125.0 "$ftp22 start"
$ns at 150.0 "$ftp22 stop"

#Setup a FTP Application over TCP connection
set ftp23 [new Application/FTP]
$ftp23 attach-agent $tcp36
$ns at 125.0 "$ftp23 start"
$ns at 150.0 "$ftp23 stop"

#Setup a FTP Application over TCP connection
set ftp24 [new Application/FTP]
$ftp24 attach-agent $tcp24
$ns at 125.0 "$ftp24 start"
$ns at 150.0 "$ftp24 stop"

#Setup a FTP Application over TCP connection
set ftp25 [new Application/FTP]
$ftp25 attach-agent $tcp25
$ns at 125.0 "$ftp25 start"
$ns at 150.0 "$ftp25 stop"

#Setup a FTP Application over TCP connection
set ftp26 [new Application/FTP]
$ftp26 attach-agent $tcp29
$ns at 125.0 "$ftp26 start"
$ns at 150.0 "$ftp26 stop"

#Setup a FTP Application over TCP connection
set ftp27 [new Application/FTP]
$ftp27 attach-agent $tcp30
$ns at 125.0 "$ftp27 start"
$ns at 150.0 "$ftp27 stop"

#Setup a FTP Application over TCP connection
set ftp28 [new Application/FTP]
$ftp28 attach-agent $tcp26
$ns at 125.0 "$ftp28 start"
$ns at 150.0 "$ftp28 stop"

#Setup a FTP Application over TCP connection
set ftp29 [new Application/FTP]
$ftp29 attach-agent $tcp27
$ns at 125.0 "$ftp29 start"
$ns at 150.0 "$ftp29 stop"

#Setup a FTP Application over TCP connection
set ftp30 [new Application/FTP]
$ftp30 attach-agent $tcp18
$ns at 125.0 "$ftp30 start"
$ns at 150.0 "$ftp30 stop"

#Setup a FTP Application over TCP connection
set ftp31 [new Application/FTP]
$ftp31 attach-agent $tcp19
$ns at 125.0 "$ftp31 start"
$ns at 150.0 "$ftp31 stop"

#Setup a FTP Application over TCP connection
set ftp32 [new Application/FTP]
$ftp32 attach-agent $tcp20
$ns at 125.0 "$ftp32 start"
$ns at 150.0 "$ftp32 stop"

#Setup a FTP Application over TCP connection
set ftp33 [new Application/FTP]
$ftp33 attach-agent $tcp21
$ns at 125.0 "$ftp33 start"
$ns at 150.0 "$ftp33 stop"

#Setup a FTP Application over TCP connection
set ftp34 [new Application/FTP]
$ftp34 attach-agent $tcp22
$ns at 125.0 "$ftp34 start"
$ns at 150.0 "$ftp34 stop"

#Setup a FTP Application over TCP connection
set ftp35 [new Application/FTP]
$ftp35 attach-agent $tcp23
$ns at 125.0 "$ftp35 start"
$ns at 150.0 "$ftp35 stop"

#Setup a FTP Application over TCP connection
set ftp36 [new Application/FTP]
$ftp36 attach-agent $tcp10
$ns at 150.0 "$ftp36 start"
$ns at 175.0 "$ftp36 stop"

#Setup a FTP Application over TCP connection
set ftp37 [new Application/FTP]
$ftp37 attach-agent $tcp11
$ns at 150.0 "$ftp37 start"
$ns at 175.0 "$ftp37 stop"

#Setup a FTP Application over TCP connection
set ftp38 [new Application/FTP]
$ftp38 attach-agent $tcp12
$ns at 150.0 "$ftp38 start"
$ns at 175.0 "$ftp38 stop"

#Setup a FTP Application over TCP connection
set ftp39 [new Application/FTP]
$ftp39 attach-agent $tcp13
$ns at 150.0 "$ftp39 start"
$ns at 175.0 "$ftp39 stop"

#Setup a FTP Application over TCP connection
set ftp40 [new Application/FTP]
$ftp40 attach-agent $tcp4
$ns at 150.0 "$ftp40 start"
$ns at 175.0 "$ftp40 stop"

#Setup a FTP Application over TCP connection
set ftp41 [new Application/FTP]
$ftp41 attach-agent $tcp5
$ns at 150.0 "$ftp41 start"
$ns at 175.0 "$ftp41 stop"

#Setup a FTP Application over TCP connection
set ftp42 [new Application/FTP]
$ftp42 attach-agent $tcp2
$ns at 150.0 "$ftp42 start"
$ns at 175.0 "$ftp42 stop"

#Setup a FTP Application over TCP connection
set ftp43 [new Application/FTP]
$ftp43 attach-agent $tcp3
$ns at 150.0 "$ftp43 start"
$ns at 175.0 "$ftp43 stop"

#Setup a FTP Application over TCP connection
set ftp44 [new Application/FTP]
$ftp44 attach-agent $tcp0
$ns at 150.0 "$ftp44 start"
$ns at 175.0 "$ftp44 stop"

#Setup a FTP Application over TCP connection
set ftp45 [new Application/FTP]
$ftp45 attach-agent $tcp1
$ns at 150.0 "$ftp45 start"
$ns at 175.0 "$ftp45 stop"

#Setup a FTP Application over TCP connection
set ftp46 [new Application/FTP]
$ftp46 attach-agent $tcp7
$ns at 150.0 "$ftp46 start"
$ns at 175.0 "$ftp46 stop"

#Setup a FTP Application over TCP connection
set ftp47 [new Application/FTP]
$ftp47 attach-agent $tcp6
$ns at 150.0 "$ftp47 start"
$ns at 175.0 "$ftp47 stop"

#Setup a FTP Application over TCP connection
set ftp48 [new Application/FTP]
$ftp48 attach-agent $tcp9
$ns at 150.0 "$ftp48 start"
$ns at 175.0 "$ftp48 stop"

#Setup a FTP Application over TCP connection
set ftp49 [new Application/FTP]
$ftp49 attach-agent $tcp8
$ns at 150.0 "$ftp49 start"
$ns at 175.0 "$ftp49 stop"

#Setup a FTP Application over TCP connection
set ftp50 [new Application/FTP]
$ftp50 attach-agent $tcp16
$ns at 150.0 "$ftp50 start"
$ns at 175.0 "$ftp50 stop"

#Setup a FTP Application over TCP connection
set ftp51 [new Application/FTP]
$ftp51 attach-agent $tcp17
$ns at 150.0 "$ftp51 start"
$ns at 175.0 "$ftp51 stop"

#Setup a FTP Application over TCP connection
set ftp52 [new Application/FTP]
$ftp52 attach-agent $tcp15
$ns at 150.0 "$ftp52 start"
$ns at 175.0 "$ftp52 stop"

#Setup a FTP Application over TCP connection
set ftp53 [new Application/FTP]
$ftp53 attach-agent $tcp14
$ns at 150.0 "$ftp53 start"
$ns at 175.0 "$ftp53 stop"


#===================================
#        Termination        
#===================================
#Define a 'finish' procedure
proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    exec nam out.nam &
    exit 0
}
for {set i 0} {$i < $val(nn) } { incr i } {
    $ns at $val(stop) "\$n$i reset"
}
$ns at $val(stop) "$ns nam-end-wireless $val(stop)"
$ns at $val(stop) "finish"
$ns at $val(stop) "puts \"done\" ; $ns halt"
$ns run
