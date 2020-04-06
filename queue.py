#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
    def Addtoqueue(self, entry):
        self.size += 1
        return self.queue.append(entry)
    def Popfromqueue(self):
        self.size -=1
        return self.queue.pop()
    def Sizeofqueue(self):
        return self.size
    
new = Queue()
new.Addtoqueue('helloworld')
new.Addtoqueue('helloword2')
new.Addtoqueue('helloworld3')
new.Popfromqueue()
new.Sizeofqueue()
print(new.queue)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




