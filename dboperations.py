#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pip._internal import main
main(['install','mysql-connector-python-rf'])


# In[ ]:





# In[3]:


try:
    import mysql.connector as mysql
    db = mysql.connect(host="localhost", user="secondjeffrey", passwd="abc123")
    cursor = db.cursor()
    firstname = 'jeffrey'
    lastname = 'chan'
    coursename = 'bus443'
    courselocation = 'b410'
    cursor.execute("insert into jeffrey_schema.faculty (firstname, lastname, coursename, courselocation) values (%s, %s, %s, %s)",(firstname, lastname, coursename, courselocation)) 
    cursor.execute("SELECT * FROM jeffrey_schema.faculty")
    data = cursor.fetchall()
    print(data)
    #open command and write data into that file & close said file. 
    #closing the file & ending the connection. 
finally:
    cursor.close()
    db.close()


# In[ ]:





# In[ ]:




