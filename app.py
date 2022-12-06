#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import streamlit as st

def main():
  st.title("Even or Odd Number")
  html_temp = """
  <div style="background-color:black;padding:10px">
  <h2 style="color:white;text-align:center;">Identify whether the number is Even or Odd</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  result="none"
  if num1%2==0:
    result = "Even"
  else:
    result="Odd"

  st.success('The number {} is {}'.format(num1,result))
  
if __name__=='__main__':
  main()


# In[ ]:




