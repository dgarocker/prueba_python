
class Data:
    jump = 0
    def order(self,data,level_options,priority_options):
        self.jump = 0
        self.level_options = level_options
        self.priority_options = priority_options
        level = level_options.split(',')
        priority = priority_options.split(',')

        order_level = {}
        order_priority = {}

        for lev in level:
            order_level[lev] = []
            order_priority[lev] = []
            for child in data.keys():
                if data[child]['level'] == lev:
                    order_level[lev].append({child: data[child]})

        for prior in priority:
            for level in order_level.keys():
                for child in order_level[level]:
                    for elem in child:
                        if child[elem]['priority'] == prior:
                            order_priority[level].append(child)
                            order_level[level].remove(child)

        for level in order_priority.keys():
            for childs in order_priority[level]:
                for elem in childs:
                    for items in childs[elem]:
                        if type(childs[elem][items]) is dict:
                            childs[elem][items] = self.order(childs[elem][items],level_options,priority_options)

        result = {}

        for res in order_priority.keys():
            if len(order_priority[res]) > 0:
                for val in order_priority[res]:
                    result.update(val)
        self._order = result
        return result


    def order_show(self,data):
        indent = '\t' * self.jump
        result = ''
        for key in data.keys():
            result += indent+key+'\n'
            result += indent+'  '+data[key]['name']+'\n'
            for item in data[key].keys():
                if type(data[key][item]) is dict:
                    self.jump += 1
                    result += self.order_show(data[key][item])
        return result

    def show(self):
        p = self.order_show(self._order)
        print(p)


    def addData(self,data):
        self._order.update(data)
        return self.order(self._order,self.level_options,self.priority_options)


if __name__ == "__main__":
    import doctest
    doctest.testfile('testA2.txt')
