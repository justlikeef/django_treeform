# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__","__requirements__"
]

__requirements__ = ["Django","mysqlclient","django_treebeard"]
__title__ = "django_treeform"
__summary__ = "Dynamic form build from a treebeard tree and saved to the specified master and child value table"
__uri__ = "https://git01.pfsfhq.com/Operations/NetDM/homepage/"

__version__ = "1.0.0a0"

__author__ = "Rob Hutton"
__email__ = "justlikeef@gmail.com"

__license__ = "GNU General Public License, version 3"
__copyright__ = "Copyright 2019 {}".format(__author__)
__includedata__ = True
__includedatafiles__ = {'' : ['__cmdbcache__/.dirinfo','']}
__excludedatafiles__ = {}
