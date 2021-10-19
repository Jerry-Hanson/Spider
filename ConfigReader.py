import yaml

class ConfigReader:
    def __init__(self, path, instance_list=None):
        if instance_list is None:
            instance_list = []
        self.path = path
        self.instance_list = instance_list

    def get_item(self):
        with open(self.path, 'r', encoding='utf-8') as fp:
            yaml_data = fp.read()
        data_dic = yaml.load(yaml_data, yaml.FullLoader)
        for key, val in data_dic.items():
            if key in self.instance_list:
                l = data_dic[key]
                data_dic[key] = {}
                for full_class_name, priority in l.items():
                    clz_name = full_class_name.split('.')[-1]
                    module = __import__(''.join(full_class_name.split('.')[:-1]))
                    data_dic[key][getattr(module, clz_name)] = priority
        self.data_dic = data_dic
        return self.data_dic

if __name__ == "__main__":
    path = 'config/settings.yaml'
    config_reader = ConfigReader(path, ["DOWNLOADER_MIDDLEWARES", "ITEM_PIPELINES"])
    settings = config_reader.get_item()
    print(settings)
