zabbix-disk-performance
=======================

Zabbix template for collecting IO statistics

With this template you can collect different disk statistics.

Installation
------------
To install, copy `userparameter_diskstats.conf` to /etc/zabbix/zabbix_agentd.d/userparameter_diskstats.conf and `lld-disks.py` to `/usr/local/bin/lld-disks.py`.
Do not forget to mark it executable.

`userparameter_diskstats.conf` is user parameters for Zabbix.
`lld-disks.py` is low level discovery script for enumerating disks of your system.

After that restart zabbix-agent
```sudo service zabbix-agent restart```

Go to Zabbix's web interface, Configuration->Templates and import `Template Disk Performance.xml`.
After that you should be able to monitor disk activity for all your disks.

Low level discovery will list your RAID devices, and LVM volumes, but LVM
volumes will be mapped with their device-mapper ID, not the pretty names.

Using without User Parameters
-----------------------------
Zabbix have [standard parameters](https://www.zabbix.com/documentation/2.0/manual/appendix/items/supported_by_platform) for monitoring disk io: `vfs.dev.read` and `vfs.dev.write` with several types:
* sectors
* operations
* sps
* ops

Template have this values configured, but disabled by default.


Testing
-------
To test that everything work use `zabbix_get`:
```
zabbix_get -s 127.0.0.1 -k "custom.vfs.dev.write.sectors[sda]"
```
