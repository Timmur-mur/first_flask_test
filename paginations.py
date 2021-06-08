class Peginatuion():
    
    def __init__(self, massiv, output_volume, page):
        self.page = page
        self.massiv = massiv
        self.output_volume = output_volume
        self.offset = (self.page*self.output_volume)- self.output_volume
        

    def get_pages(self):
        current_page = self.massiv[self.offset:(self.offset+self.output_volume)]
        if current_page == []:
            return 'sjbvlvfreribvkscns'
        else:
            return current_page

    def get_all_pages(self):
        all_pages = len(self.massiv) // self.output_volume
        last_page = len(self.massiv) % self.output_volume
        if last_page > 0:
            return all_pages + 1
        else:
            return all_pages
    
    def get_prev(self):
        page = self.massiv[(self.offset - self.output_volume):self.output_volume + (self.offset - self.output_volume)]
        if page == []:
            return False
        return page

    def get_next(self):
        page = self.massiv[(self.offset+self.output_volume):self.output_volume + (self.offset+self.output_volume)]
        if page == []:
            return False
        else:
            return page

    def prev_num(self):
        if self.page > 1:
            return self.page - 1
        else:
            return 1

    
    def next_num(self):
        all_pages = len(self.massiv) // self.output_volume
        last_page = len(self.massiv) % self.output_volume
        if last_page > 0:
            pages = all_pages + 1
        else:
            pages = all_pages
        if self.page < pages:
            return self.page + 1
        else:
            return 1


obj = Peginatuion([1,2,3,4,5,6,7,8,9,0,12,34,55,67,12], 3, 7)
print(obj.get_pages())
print(obj.next_num())