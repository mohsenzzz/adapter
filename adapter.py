import xmltodict,json

class adapter:
    def __init__(self,XMLFile):
        self.XMLFile = XMLFile


    def convertor(self):
        # data = xmltodict.parse(self.XMLFile)
        with open("test.xml") as xml_file:
            data_dict = xmltodict.parse(xml_file.read())

            with open('test.json','w') as f:
                f.write(json.dumps(data_dict))

        return 'test.json'