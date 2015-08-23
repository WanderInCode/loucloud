# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import libvirt
import os

class parseXML(object):
    """工具类，修改xml文件设置"""
    def __init__(self, xmlfile=None):
        if xmlfile is None:
            self.xmlfile = 'louvm1.xml'
        else:
            self.xmlfile = xmlfile
        self.tree = ET.parse(self.xmlfile)
        self.root = self.tree.getroot()

    def setName(self, name):
        self.root.find('name').text = name

    def setCPU(self, num):
        self.root.find('vcpu').text = str(num)

    def setMemory(self, num):
        self.root.find('memory').text = str(num)

    def setDisk(self, position):
        self.root.find('devices').find('disk').find('source').attrib['file'] = position

    def getName(self):
        return self.root.find('name').text

    def getCPU(self):
        return int(self.root.find('vcpu').text)

    def getMemory(self):
        return int(self.root.find('memory').text)

    def getDisk(self):
        return self.root.find('devices').find('disk').find('source').attrib['file']

    def getVNC(self):
        return int(self.root.find('devices').find('graphics').attrib['port'])

    def toString(self):
        return ET.tostring(self.root)

    def writeXML(self, newname):
        self.tree.write(newname)

class VM(object):

    def __init__(self):
        self.__hostUri = 'qemu+ssh://zhanyh@localhost/system'
        self.host = libvirt.open(self.__hostUri)
        self.xml = None

    def setXML(self, name=None, cpu_num=None, mem_num=None, disk_position=None ):
        '''设置xml文件参数'''
        xml = parseXML()
        if name is not None:
            xml.setName(name)
        if cpu_num is not None:
            xml.setCPU(cpu_num)
        if mem_num is not None:
            xml.setMemory(mem_num)
        if disk_position is not None:
            xml.setDisk(disk_position)
        self.xml = xml

    def createVM(self):
        '''根据设置好的xml文件，启动虚拟机'''
        domainXMLString = self.xml.toString()
        domain = self.host.createXML(domainXMLString, 0)
        return domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING

    def defineVM(self):
        '''根据xml文件定义虚拟机，暂不启动'''
        self.host.defineXML(self.xml.toString())

    def shutdownVM(self, name):
        '''关闭虚拟机'''
        domain = self.host.lookupByName(name)
        domain.destroy()
        #return domain.state()[0] == 5

    def startVM(self, name):
        '''启动定义好的虚拟机'''
        domain = self.host.lookupByName(name)
        domain.create()
        return domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING

    def getVNCPort(self, name):
        '''得到vnc端口号'''
        domain = self.host.lookupByName(name)
        f = open('tmp.xml', 'w')
        f.write(domain.XMLDesc())
        f.close()
        port = parseXML('tmp.xml').getVNC()
        os.remove('tmp.xml')
        return port

    def rebootVM(self, name):
        '''重启虚拟机，该功能目前无法使用'''
        domain = self.host.lookupByName(name)
        domain.reboot()
        return domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING

    def deleteVM(self, name):
        '''删除虚拟机。对于createXML方法创建的虚拟机，执行destroy方法即可;如果
        是defineXML方法创建，额需执行undefine方法'''
        domain = self.host.lookupByName(name)
        domain.destroy()
        domain.undefine()

if __name__ == '__main__':
    vm1 = VM()
    vm1.setXML('test1', 1, 1024)
    vm1.defineVM()
    vm1.setXML('test2', 2, 2048)
    vm1.defineVM()
    vm1.setXML('test3', 4, 20480)
    sta1 = vm1.createVM()
    print 'createVM', sta1
    #sta2 = vm1.shutdownVM('test3')
    #print 'shutdownVM', sta2
    vm1.shutdownVM('test3')
    sta3 = vm1.startVM('test1')
    print 'startVM', sta3
    print 'vnc ', vm1.getVNCPort('test1')
    vm1.deleteVM('test1')
      