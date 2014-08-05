
import logging
logging.basicConfig()
import optparse

logger = logging.getLogger("script")


def parse_args():
    """Parses the standard args and returns a configuration object."""
    parser = optparse.OptionParser()

    parser.add_option(
        "--infile", type=str,
        help="Path to distributor feed file.")

    options, args = parser.parse_args()

    return options, args


def parse_infile(path):
    with open(path, "r") as infile:
        return infile.read()

def print_ext():
    print("""His wings are gray and trailing,
Azrael, Angel of Death.
And yet the souls that Azrael brings
Across the dark and cold,
Look up beneath those folded wings,
And find them lined with gold
- Robert Welsh""")

def show_all(myDictionary):
    dicItemsCount = 0
    for key in sorted(myDictionary.keys()):
        dicItemsCount += 1
        print("{0}\n{1}: {2}\n".format(dicItemsCount, key, myDictionary[key]))
    print("\n")

def query(myDictionary):
    userInput = raw_input("Please enter your query string: ").upper()
    print("\n")
    print("{0}: {1}".format(userInput, myDictionary[userInput]))
    print("\n")

def main():
    """Entry point for the application."""
    options, args = parse_args()
    print("hurr")
    logger.debug("Started parsing file %s\n" % options.infile)
    data = parse_infile(options.infile)

    myDictionary = {}
    
    # Spliting the file to a rows array
    data_rows = data.split('\n')

    # START - Loop through the file rows
    for row in data_rows:

        # Splitting each row by comma to get items
        row_fields = row.split(',')

        # START - Validations
        if (len(row_fields) < 2):
            continue
        if (row_fields[0] == ""):
            continue
        # END - Validations

        firstField = row_fields[0]
        lastField = row_fields[len(row_fields) - 1]

        otherFields = ""
        fieldCount = 0
        for field in row_fields:
            fieldCount += 1
            if (fieldCount == 1 or fieldCount == len(row_fields)):
                continue
            otherFields = otherFields + field + ", "
        otherFields = otherFields[:-2]
        otherFields = "[" + otherFields + "]"

        myTuple = firstField, lastField, otherFields
        myDictionary[firstField.upper()] = myTuple

        continue

    # END - Loop through the file rows
    print("")
    logger.debug("Completed parsing file %s\n" % options.infile)


    # START - OUTPUT

    #print(myDictionary)
        
    while 1:
        print("*** Available Options ***\n")
        string = """a. Show All Records
q. Query Individual Record
x. Exit program

Please enter required option:"""
        print(string)
        userInput = raw_input("").upper()
        print("\n")
        


        if (userInput == "A"):
            show_all(myDictionary)
            
        elif (userInput == "Q"):
            try:
                query(myDictionary)
            except:
                print("Couldn't find any details\n\n")
        
        elif (userInput == "X"):
            print_ext()

            print("\n")
            logger.debug("Exiting program...")

            break
        else:
            print("Input couldn't be recognized, please enter correct option.\n")
            continue

    # END - OUTPUT

    pass

if __name__ == "__main__":
    main()
