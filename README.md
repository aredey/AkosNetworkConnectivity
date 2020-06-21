# Akos' Network Connectivity visualisation app

This is a python3 script that generates a CSV file that can be used in https://app.diagrams.net/ to display the associated network topology. The topology consist if firewall (gateway) devices between security domains. 

The input to the script is a set of configuration (device_host_name.cfg) files describing the device interfaces (and static routes - this info is not currently used), saved under the subdirectory `Configs/*.cfg` . A sample of 4 such config files (emulating four Checkpoint firewall configuration scripts) have been supplied.

Run the script as `cfg2csv.py`. This will result in the output of a CSV file that can be used to dra the topology diagram with [draw.io](https://app.diagrams.net/):

`diagram > new page > Arrange > Insert > Advanced > CSV` < <paste cfg2csv.py output>

This project is in development, I mainly created to experiemnt with python programming and using various tools like the draw.oio application and github.

This app is not supported but you are welcome to use it at your own risk.

### Development History and general brain dump:
This is just some ramdo, motes, thoughts and vague plans.
1. Diagram

1.1. Manually created diagram with

https://www.diagrams.net/ Note on the home page:
>diagrams.net is open source, online, desktop and container deployable diagramming software
>No login or registration required


1.2. CSV from gateways.csv
Source docs:
- https://drawio-app.com/automatically-create-draw-io-diagrams-from-csv-files/
- https://drawio-app.com/import-from-csv-to-drawio/

### Todo:
1.3 Fix grammar and make README comprehensible for humans

1.4 Embedded html from the github file

2. Spreadsheet (network-list.ods) list + Src IP address & Dst IP address > path calculation

2.1. Check, clense and sanities the *.cfg config files (static routes)

2.2. IP address to Security Domain

2.3. Shortest path calculation and display from SrcIP + DstIP (and SrcDomain to DstDomain)

2.4. Generate IP to Domain mapping from opearional data (DNS database or Gateway device (firewalls, routers topology or routing) info)

2.5. Query firewalls or Policy database

2.6. Evaluate connectivity request from codified Security Policy

