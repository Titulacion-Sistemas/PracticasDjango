from time import sleep
import win32com
import win32com.client

__author__ = 'JC'

class ConnectionManager:
  def __init__(self):
    """

    :rtype : object
    """
    self.PCommConnMgr= win32com.client.Dispatch("PCOMM.autECLConnMgr")
    self.connList= self.PCommConnMgr.autECLConnList
    self.activeSession= None
    self.sessions= {}

  def setActiveSession(self, connectionName):
    self.activeSession= self.sessions[connectionName]

  # return value from screen at position (row, col)
  def getText(self, row, col, length= None, session= None):
    result= None
    tempSession= self.activeSession
    if session is not None:
      tempSession= self.sessions[session]

    if length is None:
      tempSession.autECLPS.autECLFieldList.Refresh()
      field= tempSession.autECLPS.autECLFieldList.FindFieldByRowCol(row, col)
      length= field.Length

    result= tempSession.autECLPS.GetText(row, col, length)
    return result
  def sendKeys(self, count, key, row= None, col= None, session= None):
    n= 0
    while n< count:
      tempSession= self.activeSession
      if session is not None:
        tempSession= self.sessions[session]

      if row is None or col is None:
        tempSession.session.autECLPS.SendKeys("%s" % (key))
      else:
        tempSession.session.autECLPS.SendKeys("%s" % (key), row, col)

      n+= 1
  def getAvailableConnections(self, usuario="Gronquillo", contrasenia="Spardo"):
    self.connList.Refresh()
    connections= []
    if 0 == self.connList.Count:
      self.openProgram(usuario, contrasenia)
      self.connList.Refresh()
    for i in range (self.connList.Count):
      connections.append(self.connList(i+ 1).Name)
    return connections

  def openSession(self, session):
    _session= win32com.client.Dispatch("PCOMM.autECLSession")
    _session.SetConnectionByName(session)
    if not _session.Ready:
        print "la session no esta lista"
      # _session.StartCommunication()
    self.sessions[session]= _session

  def openProgram(self, usuario, contrasenia):
      print "Abriendo el Programa"
      self.PCommConnMgr.StartConnection("PROFILE=.\sico\CNEL.WS CONNNAME=s WINSTATE=MIN")
      shell = win32com.client.Dispatch('WScript.Shell')
      sleep(3)
      shell.SendKeys(usuario, 0)
      shell.SendKeys("{tab}", 0)
      shell.SendKeys(contrasenia, 0)
      shell.SendKeys("{enter}", 0)
      sleep(15)