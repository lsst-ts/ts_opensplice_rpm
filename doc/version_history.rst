.. py:currentmodule:: lsst.ts.opensplice_rpm

.. _lsst.ts.opensplice_rpm.version_history:

###############
Version History
###############

v-18
====

Updated ddsutil.py to ADLINK latest version with Rubin provided patch
(this will be included in the next ADLINK release - 6.11.2)

All RPM versions bumped to -18

 * ts_yum/releases/OpenSpliceDDS-6.9.0-18.el7.x86_64.rpm  : 
	OpenSplice DDS Community 6.9.0 , ts_dds_python 6.10.4-18

 * ts_yum_private/releases/OpenSpliceDDS-6.10.4-18.el7.x86_64.rpm : 
	OpenSplice Enterprise 6.10.4p2 , ts_dds_python 6.10.4-18

Sources
-------

* OpenSplice DDS 6.9.0 https://github.com/ADLINK-IST/opensplice/commit/5ec834ef215e82036bc2f1ac4530ae6001de47cc

* OpenSplice DDS 6.10.4p2 Private download from ADLINK

* ts_dds_python 6.10.4-18 : https://github.com/lsst-ts/ts_dds_python/releases/tag/v6.10.4-18


v-17
====

All RPM versions bumped to -17, reverted to 6.10.4p2 due to 6.11.x failures

 * ts_yum/releases/OpenSpliceDDS-6.9.0-17.el7.x86_64.rpm  : 
	OpenSplice DDS Community 6.9.0 , ts_dds_python 6.10.4

 * ts_yum_private/releases/OpenSpliceDDS-6.10.4-17.el7.x86_64.rpm : 
	OpenSplice Enterprise 6.10.4p2 , ts_dds_python 6.10.4


v-16
====

Applied Rubin patch to remove _def_dealloc from Class Condition

All RPM versions bumped to -16

 * ts_yum/releases/OpenSpliceDDS-6.9.0-16.el7.x86_64.rpm  : 
	OpenSplice DDS Community 6.9.0 , ts_dds_python 6.11.0

 * ts_yum/releases/OpenSpliceDDS-6.9.0-16.el7.aarch64.rpm : 
	OpenSplice DDS Community 6.9.0 , ts_dds_python 6.11.0

 * ts_yum_private/releases/OpenSpliceDDS-6.11.0-16.el7.x86_64.rpm : 
	OpenSplice Enterprise 6.11.0 , ts_dds_python 6.11.0

 * ts_yum_private/releases/OpenSpliceDDS-6.11.0-16.el7.aarch64.rpm
	OpenSplice Enterprise 6.11.0 , ts_dds_python 6.11.0

Sources
-------

* OpenSplice DDS 6.9.0 https://github.com/ADLINK-IST/opensplice/commit/5ec834ef215e82036bc2f1ac4530ae6001de47cc

* OpenSplice DDS 6.11.0 Private download from ADLINK

* ts_dds_python 6.11.0 : https://github.com/lsst-ts/ts_dds_python/releases/tag/v6.11.0-16

v-15
====

First release of this version tracking repo. All RPM versions bumped to -15

 * ts_yum/releases/OpenSpliceDDS-6.9.0-15.el7.x86_64.rpm  : 
	OpenSplice DDS Community 6.9.0 , ts_dds_python 6.11.0
 * ts_yum/releases/OpenSpliceDDS-6.9.0-15.el7.aarch64.rpm : 
	OpenSplice DDS Community 6.9.0 , ts_dds_python 6.11.0
 * ts_yum_private/releases/OpenSpliceDDS-6.11.0-15.el7.x86_64.rpm : 
	OpenSplice Enterprise 6.11.0 , ts_dds_python 6.11.0

Sources
-------

* OpenSplice DDS 6.9.0 https://github.com/ADLINK-IST/opensplice/commit/5ec834ef215e82036bc2f1ac4530ae6001de47cc

* OpenSplice DDS 6.11.0 Private download from ADLINK

* ts_dds_python 6.11.0 : https://github.com/lsst-ts/ts_dds_python/releases/tag/v6.11.0
