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