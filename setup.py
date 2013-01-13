from distutils.core import setup
from distutils.extension import Extension
import os

SUBPACKAGES=["AttNotification", "AttNotification_skel",
             "CosEventChannelAdmin", "CosEventChannelAdmin_skel",
             "CosEventComm", "CosEventComm_skel",
             "CosNotification", "CosNotification_skel", 
             "CosNotifyChannelAdmin", "CosNotifyChannelAdmin_skel",
             "CosNotifyComm", "CosNotifyComm_skel",
             "CosNotifyFilter", "CosNotifyFilter_skel",
             "Tango", "Tango_skel" ]

setup(name="hapPyTango",
      version="0.1",
      author="Matias Guijarro",
      package_dir={ 'hapPyTango': 'src/hapPyTango' },
      packages = ['hapPyTango'] + ["hapPyTango.%s" % pkg for pkg in SUBPACKAGES],      
) 
