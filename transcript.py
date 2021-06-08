

class Transcript():
    alf_ru = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'j','з':'z','и':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'x','ц':'c','ч':'ch','ш':'sh','щ':'sh','ы':'y','э':
    'e','ю':'uy','я':'ya','й':'i','Ъ':'','ь':'','-':'-','_':'_',' ':'_',':':'_'}
    
    def __init__(self, s):
        self.word = s.lower()
    
    def tran_word(self):
        simv = [i for i in self.word]
        #print(simv)
        engs = []
        for si in simv:
            if si.isdigit():
                engs.append(si)
                continue
            try:
                engs.append(self.alf_ru[si])
            except:
                engs.append(si)
        engs = ''.join(engs)
        return engs

