import logging


class ListTask:
    import logging
    logging.basicConfig(filename='listTask.log', level=logging.DEBUG,format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


    def __init__(self, l):
        try:
            self.l=l
        except Exception as e:
            logging.exception(e)
    def reverse_list(self):
        logging.info("entered inside a reverse_list function ")
        try:
            logging.info("Success reversing of list l = %s", self.l[::-1])
            return self.l[::-1]
        except Exception as e:
            logging.exception(e)

    def find_entity(self,n):
        try:
            logging.info("entered find a number function of class")

            for i in self.l:
                if i==n:
                    print(self.index(i), i)
                elif type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i :
                        if j==n:
                            print(j)
                elif type(i)==dict:
                    for k in i.keys():
                        if k==n:
                            print("key ", k)
                    for v in i.values():
                        if v==n:
                            print('values ', v)
        except Exception as e :
            logging.exception(e)

    def extract_list(self):
        try:
            logging.info("entered extract list method of class ListTask")
            for i in self.l:
                if type(i)==list :
                    print(i)
        except Exception as e:
            logging.exception(e)
    def extract_keys(self):
        try:
            logging.info("entered inside extract_keys function")
            for i in self.l:
                if type(i)==dict:
                    print(i.keys())
        except Exception as e:
            logging.exception(e)

    def extract_values(self):
        try:
            logging.info("entered inside extract_values function")
            for i in self.l:
                if type(i) == dict:
                    print(i.values())
        except Exception as e:
            logging.exception(e)



l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
234:[23,45,656]}]
obj=ListTask(l)
#1 . Try to reverse a list
print(obj.reverse_list())
#2. try to access 234 out of this list
obj.find_entity(234)
#3 . try to access 456
obj.find_entity(456)
#4 . Try to extract only a list collection form list l
obj.extract_list()
#5 . Try to extract "sudh"
obj.find_entity('sudh')
#6 . Try to list all the key in dict element avaible in list
obj.extract_keys()
#7 . Try to extract all the value element form dict available in list
obj.extract_values()



