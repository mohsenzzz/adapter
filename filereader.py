import json
from adapter import adapter

class File:
    def __init__(self, fileAddress):
        self.fileAddress = fileAddress

    def read(self):
        with open(self.fileAddress, 'r') as f:
            return f.read()


if __name__ == '__main__':

    xml_file = adapter('test.xml')
    xml_file_name = xml_file.convertor()
    file1 = File(xml_file_name)
    data = file1.read()
    print(data)