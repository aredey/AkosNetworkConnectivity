1. diagram
1.1. Manually created diagram 
#https://www.diagrams.net/
>diagrams.net is open source, online, desktop and container deployable diagramming software
>No login or registration required


1.2. CSV from gateways.csv
Source docs:
#https://drawio-app.com/automatically-create-draw-io-diagrams-from-csv-files/
#https://drawio-app.com/import-from-csv-to-drawio/

And experimenting with python3 on Ubuntu:
```
sudo apt install python3 python3-pip geany
sudo apt installipcalc
```

`diagram > new page > Arrange > Insert > Advanced > CSV` < <paste cfg2csv.py output>


Todo:
2. Spreadsheet (network-list.ods) list + Src IP address & Dst IP address > path calculation
#Todo: 
2.1 Check, clense and sanities the *.cfg config files (static routes)
2.2 IP address to Security Domain
2.3 Shortest path calculation and display from SrcIP + DstIP (and SrcDomain to DstDomain)
2.4 Generate IP to Domain mapping from opearional data (DNS database or Gateway device (firewalls, routers topology or routing) info)
2.5 Query firewalls or Policy database
2.6 Evaluate connectivity request from codified Security Policy

