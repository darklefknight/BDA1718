class DataFlow(object):

    def __init__(self,data=None):
        self.data = data

    def __str__(self):
        """
        If the class is called in a print() or str() function or as a str statement, then this function will be called.
        If data is read already then this will return the shape of the data.
        Else it will return information about what this class is for.

        :return:
        """
        if type(self.data) == dict:
            s1 = "The data has been Grouped. The Following keys are valid:\n%s\n" % ", ".join(self.data.keys())
            s2 = "Depending of your input data your keys might be strings!"
            return s1

        if self.data != None:
            s1 = "The Data consists: \n%4i Rows\n%4i Columns\n\n"%(len(self.data),len(self.data[0]))
            s2 = "The shape of the Columns is:\n%s"%",".join([" " +str(_) + " " + str(type(i)) for _,i in enumerate(self.data[0])])
            return s1+s2

        else:
            return "Class to process data from csv files."

    def copy(self):
        """
        After the idea from numpy-arrays.

        :return: new instance of DataFlow with the same data.
        """
        return self.__returnDataFlow(data=self.data)

    def read(self,file,delimiter=",",comments="#",header_lines=0):
        """
        Reads a csv file into the variable self.data. Keeping one line as one tuple.
        If data contains numbers they will be transformed into floats.

        :param file: String of the file name (+ path)
        :param delimiter:  String of the sign which delimits columns
        :param comments:  String of the sign which indicates the start of a commenting line
        :param header_lines: Integer: Number of lines which should be skipped at the beginning
        :return: self
        """
        self.new_data = []
        header = 0
        with open(file,"r") as f:
            for line in f:
                if line[0].lstrip() == comments:
                    continue

                if header_lines > header:
                    header += 1
                    continue

                splitted = line.split(delimiter)
                for i in range(len(splitted)):
                    try:
                        splitted[i] = float(splitted[i]) # converting string to float where possible
                    except:
                        continue

                splitted = tuple(splitted) # converting the list into a tuple

                self.new_data.append(splitted) # append the tuple to the data-list

        return self.__returnDataFlow()

    def write(self,file):
        """
        Writes the content which currently is stored in self.data into a given file.
        Dependent on if the data was grouped (is now in dictionary format) the output will be different.
        If in dictionary form output will be in the format:

            key1;[(v1,v2),(v3,v4),(....)]
            key2;[(v1,v2),(v3,v4),(....)]
            ...

        Else the output will be in the format:

            v1;v2;v3;v4
            v5;v6;v7;v8
            ...


        :param file: String of the file name to store the data into.
        """

        if not type(self.data) == dict:
            with open(file,"w") as f:
                for line in self.data:
                    f.write("%s\n"%";".join([str(s) for s in line])) # converts each element of each tuple into a string

        else:
            with open(file,"w") as f:
                for key in self.data:
                    f.write(str(key))
                    f.write(";")
                    f.write(str(self.data[key]))
                    f.write("\n")


    def filter(self,function):
        """
        Since the data takes each line seperate as argument none needs to be provided.

        :param function: some function to process a line (tuple)
        :return: self

        Example:
        >>> d.filter(lambda x : x[-1] < 1)

        The example would keep each line where the last element is smaller than 1.
        """

        self.new_data = []
        for line in self.data:
            if function(line) == True:
                self.new_data.append(line)


        return self.__returnDataFlow()

    def map(self,function):
        """
        This function maps each line depending on the given function.

        :param function: some function to define how things should be mapped.
        :return: self

        Example:
        >>> d.map(lambda x : ( x[0],x[1] ))
        """

        self.new_data = []
        for line in self.data:
            self.new_data.append(function(line)) # append the result of the function for each line.

        return self.__returnDataFlow()

    def flatmap(self,function):
        """
        I did not really understand what this should do.
        """

        self.new_data = []
        for line in self.data:
            lists = function(line)
            self.new_data.append(tuple(lists)) # append the result of the function for each line.

        return self.__returnDataFlow()


    def group(self,function):
        """
        Groups the data according to the input function. The output is a dictionary.

        :param function:
        :return:
        """
        self.new_data = {}
        key_list = []
        for line in self.data:
            key = function(line)
            if not key in key_list:
                result_line = []
                if type(key) in (list,tuple):
                    for element in line:
                        if not element in key:
                            result_line.append(element)

                    result = tuple(result_line)
                    self.new_data[key] = [result]

                else:
                    for element in line:
                        if not element == key:
                            result_line.append(element)
                    result =  tuple(result_line)
                    self.new_data[key] = [result]

                key_list.append(key)
            else:
                result_line = []
                if type(key) in (list, tuple):
                    for element in line:
                        if not element in key:
                            result_line.append(element)

                    result = tuple(result_line)
                    self.new_data[key].append(result)

                else:
                    for element in line:
                        if not element == key:
                            result_line.append(element)
                    result = tuple(result_line)
                    self.new_data[key].append(result)

        return self.__returnDataFlow()

    def reduce(self,function):
        """
        Reduces grouped data, so that for every group the reduce will be called separately.

        :param function:
        :return: self
        """
        check = self.__check_type(dict)
        if not check:
            return None

        self.new_data = []
        for key in self.data:
            result = function(self.data[key])
            self.new_data.append(result)

        return self.__returnDataFlow()

    def join(self,y,function):
        """
        Joins two datasets. y needs to be of the DataFlow Class as well.
        Furthermore y needs to have the same length as self.data.

        :param y:
        :param function:
        :return:
        """
        self.new_data = []

        # Check if both dataset have same length:
        if not len(y.data) == len(self.data):
            print("For joining both datasets need to have the same length.")
            return None

        for a,b in zip(self.data,y.data):
            result = function(a,b)
            self.new_data.append(result)

        return self.__returnDataFlow()


    def __returnDataFlow(self,data=None):
        """
        Creates a new instance with the processed data, so that the data of the original instance is not touched.

        :return: DataFlow-object
        """
        if not data:
            return DataFlow(self.new_data)
        else:
            return DataFlow(data)

    def __check_type(self,data_type):
        if type(self.data) != data_type:
            print("The reduce function can only be called with grouped data.")
            return None
        else:
            return "Working"

def test_flatmap(x):
    if x[-1] < 0.01:
        return x[1],x[2],x[3]

    else:
        return []

def test_join(x,y):
    """
    Adds each value from x to y

    :param x: tuple
    :param y: tuple
    :return: tuple
    """
    result = []
    for a,b in zip(x,y):
        result.append(a+b)

    result = tuple(result)
    return result

if __name__ == "__main__":
    FILE = "test.txt"
    df = DataFlow()
    data = df.read(FILE,delimiter=";",header_lines=2)

    filtered = data.filter(lambda x : x[-1] < 1) # keep lines where laast column is smaller than 1
    mapped = data.map(lambda x : (x[0],x[1],x[-2])) # map first, second and second-last column
    grouped = data.group(lambda x : x[0]) # group by first column
    fmapped = data.flatmap(test_flatmap)
    reduced = grouped.reduce(lambda x : sum(y[-1] for y in x))
    joined = data.join(data,test_join)

