Write a Python program with the following elements

All elements should be present in last week's notes.

1. the script identifies its interpreter in its first line "#!/...blahblahah"
  1a. the script is executable (set permissions with a unix tool)

2. read the provided file 
records.txt

, one line at a time
  2a. use string stripping to remove the newline at the end of each line (see string.strip ())
  2a. split each line into a list of fields (see string.split (delim))
  2b. use slicing (see notes) to store all BUT the 1st and last fields into a sublist
  2c. store the first field, the last field, and the list into a tuple (see notes),
      in that order
  2d. store the tuples into a dictionary (see notes), using the first field as uppercase
      (see notes on strings) as the key

3. show the user a menu using a multiline string (notes)
    a) show all records
    q) query individual record
    x) exit
  3a. in a loop (we'll call it your main loop), get input from stdin
  3b. process the input using an if-elif-else tree, and perform the related actions
  3c. code the related actions in functions
  3d. for a), use a for-each style loop (for a in b:)
      3c1: have the keys sorted (see sorted (), dict.keys ())
  3e. for q), uppercase the string
  3f. if for q) the queried value does not exist, have the querying function throw an
      exception that will be caught by your main loop.
  3g. when the user exits, print this as a multiline string
        His wings are gray and trailing,
        Azrael, Angel of Death.
        And yet the souls that Azrael brings
        Across the dark and cold,
        Look up beneath those folded wings,
        And find them lined with gold
        - Robert Welsh
  3h. if you're bored, add a remove () and an add () as well

4. package records.txt and your python program into a self-extracting executable
  4a. use uuencode/uudecode (and tar)

If you just print your whole dictionary, you should see this:
{'COOKIES': ('cookies', '3.29', ['chocolate', 'peanut butter', 'oatmeal']), 'CUPCAKES': ('cupcakes', '2.50', ['lavender', 'banana split']), 'PIE': ('pie', '9.39', ['apple', 'cherry', 'strawberry', 'pumpkin']), 'ICE CREAM': ('ice cream', '5.80', ['chocolate', 'vanilla', 'mint'])}