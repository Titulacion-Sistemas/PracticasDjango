import pythoncom
from usuarios import iSeries

__author__ = 'Andrea Loaiza'

pythoncom.CoInitialize()
conn = iSeries.ConnectionManager()
availableConnection = conn.getAvailableConnection()
conn.openSession(availableConnection, 'gronquillo', 'jcesar')
conn.setActiveSession(availableConnection)

