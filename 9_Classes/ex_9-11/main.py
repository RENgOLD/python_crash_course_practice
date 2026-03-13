from user import User, Admin, Privileges

admin1 = Admin("AdminName","AdminLastName","Admin",
               "AdminPassword","Admin@email.com")
admin1.privileges.show_privileges()