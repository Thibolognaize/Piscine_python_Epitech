# Prompt the user for a string:
# - if it's ”open sesame”, display ”access granted” ;
# - if it's ”will you open, you goddamn !@&/°, display ”access fucking granted” ;
# - else, display ”permission denied”.
usr_str = input("Enter a string:\n")

if usr_str == "open sesame":
    print("access granted")
elif usr_str == "will you open, you goddamn !@&/°":
    print("access fucking granted")
else:
    print("permission denied")
