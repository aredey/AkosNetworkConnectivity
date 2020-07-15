Akos' Network Connectivity visualisation app
============================================


These are python3 scripts, mainly to learn and explore the programming language while trying to solve specific issues in my professional work.

These apps are not supported in any way but you are welcome to use them in any way you want - at your own risk.

CFG2CSV
=======
`cfg2csv.py` generates a CSV file that can be plugged into `https://app.diagrams.net/` to display the a network topology. The topology consist if firewall (gateway) devices between security domains. 

The input to the script is a set of configuration (device_host_name.cfg) files describing the device network interfaces (and static routes - though this info is not currently used in the script), saved under the sub directory `Configs/*.cfg` . A sample of 4 such config files (emulating four Checkpoint firewall configuration scripts) have been supplied, along with a "dummy" device (`_.cfg`) that represent a number of isolated security domains (so that no firewalls are actually bordering them). The .cfg files are modelled from Checkpoint's configuration file format, but using the same format other firewalls or gateway devices can be easily modelled. Please note, it is mandatory that each interface has one comments line, representing the domain connected to the given network interface and one IPv4 address line and that the comments line precedes the IP address. The comment line must precede the IP address line in the device specific config file.

Prerequisites and Usage:
------------------------
Save the gateway device (firewall) configuration files in the `Configs` directory following the examples (file naming standard and format of content) given in this repository, one config script per device. You can represent isolated network domains by connecting them to a "dummy" gateway device as demonstrated by `_.cfg` where the "domains" represented by the "comments" parameter are distinct to this dummy device only.

Run the script as `cfg2csv.py` (without command line arguments). This will generate a CSV formatted output that can be pasted into a [draw.io/diagrams.net](https://app.diagrams.net/) diagram to draw the topology diagram. The output file starts with a number of (comment-like) instructions used by the diagram application for formatting and displaying the network elements and links. The resulting diagram can then be manually adjusted as needed (change the colour of links, devices and domains and move around picture elements to suit taste). The script should be able to handle hundreds or low thousands of devices and domains.

`diagram > new page > Arrange > Insert > Advanced > CSV < <paste cfg2csv.py output>`

NET_LIST_CSV2DOMAINS
====================

`net_list_csv2domains.py 1.2.3.4` is a script that outputs the security domain a given IP address (1.2.3.4, for example) belongs to.

Prerequisites and Usage:
------------------------
At lest one IP address has to be supplied on the command line, as shown above. If two addresses supplied, the second with the option `-d/--dest_addr` then the latter is used as "destination" and the associated security domains for both will be printed. With an optional `-a/--all` command line flag all matches, not just the longest one will be printed for each matched address. With the optional `-q/--quiet` flag only the domain(s) will be printed, while with `-v/--verbose` all the security domains and constituent networks will be displayed before the final result(s).

EXCEL2CSV
============
`excel2csv.py` (stored in the Scrap sub directory) is a helper script. It is intended to generate the CSV file used by `net_list_csv2domains.py ...` from the gateway device configuration scripts (as used by `cfg2csv.py`). It is expected that the above two scripts will eventually be combined to a single program.

Prerequisites and Usage:
------------------------
input `All-networks-list.xlsx` and output `All-networks-list.csv` files (latter one will be overwritten at every run of this script.


### Development History and general brain dump/notes to self:
This is just some random, motes, thoughts and vague plans.
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
1. Embedded the html diagram  within an iframe

2. Spreadsheet (network-list.ods) list + Src IP address & Dst IP address > path calculation

2.1. Check, cleanse and sanitise the *.cfg config files (static routes) properly

2.3. Shortest path calculation and display from SrcIP + DstIP (and SrcDomain to DstDomain)
  a. Using the device configuration files (hop by hop tracing the packet path)
  b. SPF
  c. Surge Routing (Hopfield neural net) - maybe

2.4. Generate IP to Domain mapping from operational data (DNS database or Gateway device (firewalls, routers topology or routing) info)

2.5. Query firewalls or Policy database or both (auditing)

2.6. Evaluate connectivity request from codified Security Policy

