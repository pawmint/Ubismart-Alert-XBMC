import xbmc
import xbmcaddon
import xbmcgui
import sys
import urlparse


__addon__ = xbmcaddon.Addon()
name = __addon__.getAddonInfo('name')


def popup(line1, line2):
    line3 = "Have a nice day!"
    xbmcgui.Dialog().ok("Alert", line1[0], line2[0], line3)


params = urlparse.parse_qs('&'.join(sys.argv[1:]))

popup(**params)
