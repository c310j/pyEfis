#  Copyright (c) 2013 Phil Birkelbach
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
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# This is the User Config File for pyEfis.  All user configuration directives
# should be placed in this file.

# CAN-FIX Connection setup
# Uncomment the adapter that you would like to use
#canAdapter = 'canfixusb'
#canAdapter = 'simulate'
#canAdapter = 'easy'
canAdapter = 'network'

# CAN Bitrate to use in kbps
canBitrate = 125

# The Serial/USB device that the above adapter would use
canDevice = '/dev/ttyUSB1'

# IP information for network adapter
canServer = '127.0.0.1'
canPort = 63349

# Screen Geometry
screenSize = (1280,720)
# Set EFIS to occupy the entire screen without system border / menu
screenFullSize = False
# Screen background color RGB
#screenColor = False #default
screenColor = 'black' #Black