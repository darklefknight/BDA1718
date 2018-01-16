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
        if self.data != None:
            s1 = "The Data consists: \n%4i Rows\n%4i Columns\n\n"%(len(self.data),len(self.data[0]))
            s2 = "The shape of the Columns is:\n%s"%",".join([" " +str(_) + " " + str(type(i)) for _,i in enumerate(self.data[0])])
            return s1+s2

        else:
            return "Class to process data from csv files."

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
        :param file: String of the file name to store the data into.
        """
        with open(file,"w") as f:
            for line in self.data:
                f.write("%s\n"%";".join([str(s) for s in line])) # converts each element of each tuple into a string

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

        self.data = self.new_data.copy() # the copy() is to not just point to the same location in the storage.

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

        self.data = self.new_data.copy() # the copy() is to not just point to the same location in the storage.

        return self.__returnDataFlow()

    def flatmap(self,function):
        pass

    def group(self,function):
        pass

    def reduce(self,function):
        pass

    def join(self,function):
        pass

    def __returnDataFlow(self):
        return DataFlow(self.new_data)



if __name__ == "__main__":
    FILE = "/home/mpim/m300517/Downloads/Cart_Site201602.csv"
    d = DataFlow()
    a = d.read(FILE,delimiter=";",header_lines=2)



