import sys # import sys module
script, input_encoding, error = sys.argv #Maps the parameters added in the command line to these variables
                                         #User will mention the script name, encoding (eg.UTF-8) and error

def main(language_file, encoding, errors):  #Declares the main function with 3 argumentos
    line = language_file.readline()         #Reads only one line from the pointer of the language_file
    if line:                                #Tests if line variable has something in it
        print_line(line, encoding, errors)  #Calls the function print_line, line = the line we've opened
        return main(language_file, encoding, errors) #Calls the function again and makes a loop, if line is empty the program will stop

def print_line(line, encoding, errors):
    next_lang = line.strip()  #Strip() returns a copy of the string with both leading and trailing characters removed, removes /n in this case.
    raw_bytes = next_lang.encode(encoding, errors=errors)   #encode() method encodes the string, using the specified encoding.
                                                            #If no encoding is specified, UTF-8 will be used
    cooked_string = raw_bytes.decode(encoding, errors=errors) #decode() decodes the string using the codec registered for encoding
    print(raw_bytes, "<===>", cooked_string) #Prints the encode and the decode string in the same line in order to compare them

languages = open('languages.txt', encoding='utf-8') #Opens the file declared in the command line using the encode UTF-8

main(languages, input_encoding, error)  #Calls the function and sends the file and the encodign given by the user

#Ejmplo de encode y decode
#string.encode()->("Mañana toca programación"); → MaÃ±ana toca programaciÃ³n
#string.decode()->("MaÃ±ana toca programaciÃ³n"); → Mañana toca programación
#DBES = Decode bytes, Encode Strings
#Errors - response when encoding fails. There are six types of error response
    #strict - default response which raises a UnicodeDecodeError exception on failure
    #ignore - ignores the unencodable unicode from the result
    #replace - replaces the unencodable unicode to a question mark ?
    #xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
    #backslashreplace - inserts a \uNNNN espace sequence instead of unencodable unicode
    #namereplace - inserts a \N{...} escape sequence instead of unencodable unicode
