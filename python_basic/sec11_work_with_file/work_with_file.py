class FileWrapper:

    def write_list_to_file(self, l, file_name, mode):
        my_file = open(file_name, mode)
        for item in l:
            my_file.write(str(item) + "\n")
        my_file.close()

    def read_file_linebyline(self, file_name, mode):
        my_file = open("file_for_note", "r")
        for line in my_file:
            print(line, end="")
        my_file.close()

    def write_string_to_file(self, string, file_name, mode):
        with open(file_name, mode) as fileObj:
            fileObj.write(string + "\n")

    def read_file(self, file_name, mode):
        with open(file_name, mode) as fileObj:
            print(str(fileObj.read()))

if __name__ == "__main__":

    somelist = ["1 line", "string", 3]
    fw = FileWrapper()
    fw.write_list_to_file(somelist, "file_for_note", "w")
    fw.read_file_linebyline("file_for_note","r")
    fw.write_string_to_file("keywords WITH and AS", "file_for_note", "a")
    fw.read_file("file_for_note","r+")
