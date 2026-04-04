"""
class ExamException (Exception):
    pass
class MovingAverage:
    def __init__(self,window_length):
        self.window_length=window_length
        if window_length<=0: raise ExamException("la finestra deve essre strettamente positiva")
    def compute(self,data):
        if type(data)!=list: raise ExamException("non è stata inserita una lista")
        if len(data)<self.window_length: raise ExamException("lunghezza della finestra superiore alla lunghezza della lista")
        for elem in data:
            if type(elem)!=(int or float): raise ExamException("la lista non contiene solo numeri")
        output=[]
        for i in range(len(data)-self.window_length+1):
            elem=data[i:(i+self.window_length)]
            output.append(sum(elem)/self.window_length)
        return output

moving_average=MovingAverage(2)
result=moving_average.compute([2,4,8,16])
print(result)
"""

class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self,window_length):
        if(isinstance(window_length,int)):
            if(window_length>0):
                self.window_length=window_length
            else:
                raise ExamException("numero minore o uguale a 0")
        else:
            raise ExamException("la finestra deve essere un numero strettamente positivo")
    def compute(self,data):
        if(not isinstance(data,list)): raise ExamException("l'argomento non è una lista")
        if(len(data)<self.window_length):
            raise ExamException("finestra maggiore del numero di argomenti della lista")
        for idx,elem in enumerate(data):
            if(not isinstance(elem,(int,float))):
                raise ExamException(f"la lista contiene un elemento che non è un numero alla posizione {idx}")
        output=[]
        for i in range(len(data)-self.window_length+1):
            sum=0
            for n in range(self.window_length):
                sum=sum+data[i+n]
            media=float(sum/self.window_length)
            output.append(media)
        return output
    
mv=MovingAverage(2)
print(mv.compute([2,4,8,16]))
