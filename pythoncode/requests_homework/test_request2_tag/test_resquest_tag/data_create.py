class DataCreate:
    def create_tag_data(self):
        data = [("c" + str(x), int(x) + 13, ["1user" + str(x), "2user" + str(x)], ["1par" + str(x), "2par" + str(x)])
                for x in range(10)]
        # data = [("wu12345wu" + str(x), "zhangsan1", "138%08d" % x) for x in range(20)]
        return data