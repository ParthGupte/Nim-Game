# create a heap object with attributes no of coins and functions to remove coins

class Heap:
    def __init__(self,coins) -> None:
        self.coins = coins
    
    def remove(self,*args,**kwargs):
        k = int(args[0])
        game = kwargs['game']
        heapno = kwargs['heapno']
        try:
            all = kwargs['all']
            if all:
                self.coins = 0
            elif all:
                self.coins -= k
                if self.coins <= 0:
                    self.coins = 0
        except:
            self.coins -= k
            if self.coins <= 0:
                self.coins = 0
        if self.coins == 0:
            del game.heapobjs[heapno]
        return self.coins
        
#create a game using no of coins in each heap
class Game:
    def __init__(self,heapslist) -> None:
        self.player = 0
        heapsobjdict = {}
        i = 0
        for val in heapslist:
            heapsobjdict[i] = Heap(val)
            i += 1
        self.heapobjs = heapsobjdict
    
    def isbalanced(self):
        subheapsdict = {}
        for heap in self.heapobjs.values():
            n = 0
            for i in bin(heap.coins)[:1:-1]:
                if n in subheapsdict.keys():
                    subheapsdict[n] += int(i)
                else:
                    subheapsdict[n] = int(i)
                n += 1
        for val in subheapsdict.values():
            if val%2 == 0:
                continue
            else:
                return False
        else:
            return True
    
    def show(self):
        coinsdict = dict(zip(self.heapobjs.keys(),[heap.coins for heap in self.heapobjs.values()]))
        print(coinsdict)
        return coinsdict
    
    def move(self,noofcoins,heapno):
        self.player = (self.player+1)%2
        
        self.heapobjs[heapno].remove(noofcoins,game=self,heapno=heapno)
        if self.heapobjs == {}:
            return (self.player+1)%2
        else:
            return None

    
    

    
    

                
