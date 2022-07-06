import logging


class StringTask:
    import logging
    logging.basicConfig(filename='string.log', level=logging.DEBUG, format='%(levelname)s : %(name)s : %(asctime)s : %(message)s ')
    def __init__(self, s):
        logging.info("Entered the string ")
        self.s = s
    def extract_jump(self,x,y,j):
        logging.info("entered the extract with jump function ")
        try:
            logging.info("executed success and answer is %s", self.s[x:y:j])
            return self.s[x:y:j]

        except Exception as e:
            logging.info(e)

    def reverse_string(self):
        try:
            logging.info('reverse string successful %s', self.s[::-1])
            return self.s[::-1]
        except Exception as e:
            logging.exception(e)

    def upp(self):
        try:
            logging.info("converting the string to uppercase %s", self.s.upper())
            return self.s.upper()
        except Exception as e:
            logging.exception(e)
    def split(self):
        try:
            logging.info("split the string = %s ", self.s.split())
        except Exception as e:
            logging.exception(e)

    def lower(self):
        try:
            logging.info("the string is lower case = %s",self.s.lower())
            return self.s.lower()
        except Exception as e:
            logging.exception(e)
    def capitalize(self):
        try:
            logging.info("Success capitalizing the string = %s",self.s.title())
            return self.s.title()
        except Exception as e:
            logging.exception(e)

    def strip(self):
        try:
            logging.info("success stripping operation on string = %s", self.s.strip())
            return self.s.strip()
        except Exception as e:
            logging.exception(e)

    def rstrip(self):
        try:
            logging.info("success right stripping operation on string = %s", self.s.rstrip())
            return self.s.rstrip()
        except Exception as e:
            logging.exception(e)

    def lstrip(self):
        try:
            logging.info("success left stripping operation on string = %s", self.s.lstrip())
            return self.s.lstrip()
        except Exception as e:
            logging.exception(e)

    def replace(self,x,y):
        try:
            logging.info("successfully replaced %s", self.s.replace(x,y))
            return self.s.replace(x,y)
        except Exception as e:
            logging.exception(e)

    def center(self,x,y):
        try:
            logging.info("success centering of the string passed %s", self.s.center(x,y))
            return self.s.center(x,y)
        except Exception as e:
            logging.exception(e)

s="this is My First Python programming class and i am learNING python string and its function"
obj=StringTask(s)
#1.Try to extract data from index one to index 300 with a jump of 3
print(obj.extract_jump(1,300,3))
#2. Try to reverse a string without using reverse function
print(obj.reverse_string())
#3.Try to split a string after conversion of entire string in uppercase
x=obj.upp()
print(x.split())
#4.. try to convert the whole string into lower case
print(obj.lower())
#5. Try to capitalize the whole string
print(obj.capitalize())
#6.Give an example of strip , lstrip and rstrip
x=' hello '
obj1=StringTask(x)
print(obj1.strip())
print(obj1.lstrip())
print(obj1.rstrip())
#7 Replace a string charecter by another charector by taking your own example"sudhanshu"
y="Hello world!"
obj2=StringTask(y)
print(obj2.replace("H", "y"))
#8  Try to give a defination of string center function with and exmple
z="veera"
obj3=StringTask(z)
print(obj3.center(20,"$"))

