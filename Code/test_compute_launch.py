
# coding: utf-8

# Before you begin, make sure to run this command in your terminal to install pytest:
# ```
# pip install -U pytest
# ```
# Then, to run pytest, just enter:
# ```
# pytest
# ```
# Right now, not all of the tests should pass. Fix the function to pass all its tests! Once all your tests pass, try writing some additional unit tests of your own!

# In[7]:


from compute_launch import days_until_launch


# In[8]:


def test_days_until_launch_4():
    assert (days_until_launch(22,26)==4)


# In[9]:


def test_days_until_launch_0():
    assert (days_until_launch(253,253)==0)


# In[10]:


def test_days_until_launch_0_negative():
    assert(days_until_launch(83, 64) == 0)


# In[15]:


def test_days_until_launch_4():
    assert (days_until_launch(83, 64) == 0)


# In[16]:


get_ipython().system('ls')


# In[18]:


get_ipython().system(' pytest')

