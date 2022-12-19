#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 12月, 19, 2022 17:30:35

class Money:
  def __init__(self,JPY,USD,lev):
    self.JPY = JPY
    self.USD = USD
    self.MP_max = JPY
    self.MP_min = JPY
    self.lev = lev 
  
  def get_MP(self,rate):
    return 
  
  def max_min(self,rate):
    self.MP_max = max(self.MP_max,self.get_MP(rate))
    self.MP_min = mix(self.MP_min,self.get_MP(rate))


def main():
  import pandas_datareader.data as pdr
  import datetime
  start = datetime.datetime(2018,12,19)
  end = datetime.datetime(2020,12,18)
  JPY_USD = pdr.DataReader('DEXJPUS', 'fred', start, end)
  ## print(len(JPY_USD))
  JPY_USD = JPY_USD.dropna(how='any')
  ## print(len(JPY_USD))
  ## print(JPY_USD)
  ## import sys
  ## sys.exit()
  ## JPY_USD = pdr.DataReader('DEXJPUS', 'yahoo', start, end)
  ## print(JPY_USD)

  JPY = 1000000
  USD = 0
  lev = 1
  commission = 0
  step = 0
  step_money = [10000,20000,40000,80000,160000,320000,640000,1280000,2560000]
  JPY_max = JPY
  JPY_min = JPY
  for index, row in JPY_USD.iterrows():
    ## print(row.DEXJPUS.__class__)
    ## print(index)
    if step == 0:
      print(index,row.DEXJPUS)
      standard = row.DEXJPUS
      JPY -= step_money[step]
      USD += step_money[step]*lev/row.DEXJPUS
      step +=1
    else:
      ## if standard +1 < row.DEXJPUS:
      if standard + 0.8 < row.DEXJPUS:
        ## JPY += USD*row.DEXJPUS - step_money[0]
        JPY += USD*row.DEXJPUS - step_money[(step-1)//2]
        ## USD = step_money[0] / row.DEXJPUS
        USD = step_money[(step-1)//2]*lev / row.DEXJPUS
        ## step = 1
        step = (step-1)//2+1
        standard = row.DEXJPUS
        ## print(index,row.DEXJPUS,step)
        print(JPY + USD*row.DEXJPUS)
        JPY_max = max(JPY_max,JPY+USD*row.DEXJPUS)
        JPY_min = min(JPY_min,JPY+USD*row.DEXJPUS)
      ## elif standard -1 > row.DEXJPUS and step:
      elif standard -0.8 > row.DEXJPUS:
        if JPY > step_money[step]:
          JPY -= step_money[step]
          USD += step_money[step]*lev / row.DEXJPUS
          step += 1
          standard = row.DEXJPUS
          ## print(index,row.DEXJPUS,step)
          print(JPY + USD*row.DEXJPUS)
        JPY_max = max(JPY_max,JPY+USD*row.DEXJPUS)
        JPY_min = min(JPY_min,JPY+USD*row.DEXJPUS)
    ## if step >= len(step_money):
      ## print(index)
      ## print('')
      ## break
  
  JPY += USD*row.DEXJPUS
  USD = 0
  print(JPY)
  print(JPY_max)
  print(JPY_min)

if(__name__ == '__main__'):
  main()
