class Node:
    """Класс узла списка"""

    def __init__(self, data):
        self.data = data
        self.prev_element = None
        self.next_element = None


class DoubleConnList:
    """Класс двусвязного списка"""

    def __init__(self):
        self.first_element = None
        self.last_element = None

    def add(self, data):
        newNode = Node(data)
        """ Если список пуст то первый и последний элемент указывают на newNode, у первого элемента предыдущий - None и у последнего элемента следующий - None """
        if self.first_element is None:
            self.first_element = self.last_element = newNode
            self.first_element.prev_element = None
            self.last_element.next_element = None
            """Если список не пустой то у последнего - следующий = newNode, у node предыдущий указывает на последний элемент, newNode становится последним элементом
            а у следующего после последнего - None"""
        else:
            self.last_element.next_element = newNode
            newNode.prev_element = self.last_element
            self.last_element = newNode
            self.last_element.next_element = None

    def is_empty(self):
        if self.first_element is None:
            return True

    def show(self):
        current = self.first_element
        if self.is_empty() is True:
            print("List is empty")
            return
        while current is not None:
            print(current.data)
            current = current.next_element

    def reverse(self):
        rev = self.first_element
        while rev is not None:
            rev.next_element, rev.prev_element = rev.prev_element, rev.next_element
            rev = rev.prev_element
        self.first_element, self.last_element = self.last_element, self.first_element
    """И так, что у нас здесь
        сначала мы доходим до того индекса куда хотим засунуть элемент
        в зависимости от положения делаем нужные вещи"""
    def insert(self, data, index):
        if self.is_empty() is True:
            if index != 1:
                print('incorrect position')
            else:
                self.add(data)
        else:
            i = 0
            ins_place = self.first_element
            for i in range(index):
                if ins_place.next_element is None:
                    break
                ins_place = ins_place.next_element
                i += 1
            index -= 1 # Это я делаю чтобы индекс совпадал с позицией на которую я собираюсь всунуть данные
            if index < 0 or index > i + 1:
                print("incorrect position")
                return
            if index is i + 1:
                self.add(data)
            elif index == 0:
                first_place = Node(data)
                first_place.next_element = self.first_element
                self.first_element.prev_element = first_place
                self.first_element = first_place
            else:
                prev_ins = ins_place.prev_element # переменная равна указателю на back от того куда мы ставим
                place = Node(data)
                prev_ins.next_element = place # back элемент на место которого ставим указывает на новый элемент
                place.next_element = ins_place # указатель на следующий элемент нового элемента указывает на тот на место которого мы ставим
                place.prev_element = prev_ins # указатель на предыдущий нового элемента указывает (прочитай про переменную)
                ins_place.prev_element = place # back указатель сдвинутой переменной указывает на новую переменную

    def remove(self, index):
        if self.is_empty() is True:
            print("List empty")
        else:
            i = 0
            del_elem = self.first_element
            for i in range(index-1):
                if del_elem.next_element is None:
                    break
                del_elem = del_elem.next_element
                i += 1
            index -= 1  # Это я делаю чтобы индекс совпадал с позицией на которую я собираюсь всунуть данные
            if index < 0 or index > i:
                print("incorrect position")
                return
            prev_del = del_elem.prev_element
            next_del = del_elem.next_element
            if prev_del is not None and prev_del.next_element is not None:
                prev_del.next_element = next_del
            if next_del is not None:
                next_del.prev_element = prev_del
            if index == 0:
                self.first_element = next_del
            if index == i:
                self.last_element = prev_del




A = (1, 'b')
Flist = DoubleConnList()
Flist.insert('he', 2)
Flist.show()
Flist.add(1)
Flist.add('b')
Flist.add(A)
Flist.add(4)
Flist.add(5)
Flist.show()
print(" ")
Flist.reverse()
Flist.show()
print(" ")
Flist.insert('Hello', 1)
Flist.show()
print(" ")
Flist.remove(7)
Flist.show()
