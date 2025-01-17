# -*- coding: UTF-8 -*-
#
#  config.py : Store all dirs, commands, files used in the same place
#  Copyright (C) 2007 Mertens Florent <flomertens@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

prefix     = "/usr/local"
PACKAGE    = "disk-manager"
VERSION    = "1.1.1"
HOMEPAGE   = "http://flomertens.free.fr/disk-manager/"
AUTHORS    = ["Mertens Florent <flomertens AT gmail.com>"]

DATADIR   = prefix + "/share/" + PACKAGE
GLADEFILE = DATADIR + "/" + PACKAGE + ".glade"
localedir = prefix + "/share/locale"

# NTFS external policy files :
HAL_CONFIG_DIR	  = "/etc/hal/fdi/policy"
TARGET_NTFS_WRITE = HAL_CONFIG_DIR + "/20-ntfs-config-write-policy.fdi"
TARGET_NTFS_READ  = HAL_CONFIG_DIR + "/20-ntfs-config-read-policy.fdi"
NTFS_WRITE        = DATADIR + "/write-policy.fdi"
NTFS_READ         = DATADIR + "/ro-policy.fdi"

# Config files :
CONF_FILE         = "/.disk-manager.conf"

# Su handler :
SU_HANDLER 	      = "su-to-root -X -c"
