class Node:
    def __init__(self,Value):
        
        self.Value=Value
        self.Parent=None
        self.Child=None
        self.Leftt=None
        self.Rightt=None
        self.Deg=0
        self.Mark=False
class febonacci_heap:
    def __init__(self):
        self.Root_lst=None
        self.MinNode=None
        
        self.TotalElement=0
    def IInsert(self, Value):
        node=Node(Value)
        node.Leftt=node.Rightt=node
        self.Meld_To_Root_Lst(node)
        if self.MinNode is not None:
            if self.MinNode.Value > node.Value:
                self.MinNode=node
        else:
            self.MinNode=node
        self.TotalElement+=1
        return node
    

    def Meld_To_Root_Lst(self,node):
        if self.Root_lst is None:
            self.Root_lst=node
        else:
            node.Rightt=self.Root_lst.Rightt
            node.Leftt=self.Root_lst
            self.Root_lst.Rightt.Leftt=node
            self.Root_lst.Rightt=node
            
    def IIterate(self,Head=None):
        if Head is None:
            Head=self.Root_lst
        Cruent=Head
        while True:
            yield Cruent
            if Cruent is None:
                break
            Cruent=Cruent.Rightt
            if Cruent==Head:
                break    
                
    def REmove_root_Lst(self,node):
        if self.Root_lst is None:
            print('empty')
            
        if self.Root_lst==node:
            
            if self.Root_lst==self.Root_lst.Rightt:
                self.Root_lst=None
                return
            else:
                self.Root_lst=node.Rightt    
        node.Leftt.Rightt=node.Rightt
        node.Rightt.Leftt=node.Leftt
        return
    
    def ConsoLidate(self):
        if self.Root_lst is None:
            return
        RankMapp=[None]*self.TotalElement
        nodes=[x for x in self.IIterate(self.Root_lst)]
        for node in nodes:
            Degree=node.Deg
            while RankMapp[Degree]!=None:
                Another=RankMapp[Degree]
                if node.Value>Another.Value:
                    #print(node.value)
                    node,Another=Another,node
                self.Merge(node,Another)
                
                RankMapp[Degree] = None
                Degree+=1
                
            RankMapp[Degree]=node
        return

    def Merge(self,node,Another):
        #if self.MergeWithNode
        self.REmove_root_Lst(Another)
        Another.Leftt=Another.Rightt=Another
        self.MergeWithNode(node,Another)
        node.Deg+=1
        Another.Parent=node
        #print(Another.Parent)
        Another.Mark=False
        #print(Another.Mark)
        return
    def MergeWithNode(self,Parent,node):
        if Parent.Child is None:
            #print(Parent.Child)
            Parent.Child=node
        else:
            node.Rightt=Parent.Child.Rightt
            #print(node)
            node.Leftt=Parent.Child
            #print(node.Rightt)
            Parent.Child.Rightt.Leftt=node
            #print(node.Leftt)
            Parent.Child.Rightt=node
    def Minimum(self):
        
        if self.MinNode is None:
            print('empty febonacci')
        #print(self.MinNode)
        return self.MinNode.Value
    def MInn_Nodee(self):
        
        if self.Root_lst is None:
            return None
        else:
            min=self.Root_lst
            #print(min)
            for x in self.IIterate(self.Root_lst):
                #print(x)
                if x.Value<min.Value:
                    min=x
                    #
            return min.Value
    def extract_minimum(self):
        
        mm=self.MinNode
        #print(mm)
        if mm is None:
            #print(mm)
            print("empty febonacci heap")
        if mm.Child is not None:
            Children=[x for x in self.IIterate(mm.Child)]
            #print(Children)
            for i in range(0,len(Children)):
                #print(i)
                self.Meld_To_Root_Lst(Children[i])
                
                Children[i].Parent=None
        self.REmove_root_Lst(mm)
        #total elemnts in feb
        self.TotalElement-=1
        
        self.ConsoLidate()
        if mm==mm.Rightt:
            #print(mm)
            self.MinNode=None
            #print(self.MinNode)
            self.Root_lst=None
            #print(self.root_lst) 
        else:
            
            self.MinNode=self.MInn_Nodee()
            #print(self.MinNode)
        return mm.Value
    
    def print_tree(self,node):
        if node is None:
            #print(node)
            return
        print(node.Value)
        if node.Child is not None:
            #loop for
            for Child in self.IIterate(node.Child):
                #print(Child)
                self.print_tree(Child)

    def Print(self,Head=None):
        
        if self.Root_lst is not None:
            #print(self.Root_lst)
            for heap in self.IIterate():
                #print(heap)
                self.print_tree(heap)
                #print(self.print_tree)

 
obj=febonacci_heap()

obj.IInsert(7)
obj.IInsert(3)
obj.IInsert(5)
obj.IInsert(1)
obj.Print()
print("extract minimum")
obj.extract_minimum()

print("min")
obj.MInn_Nodee()