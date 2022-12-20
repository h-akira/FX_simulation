#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 12月, 19, 2022 17:30:35

class Money:
  def __init__(self,JPY,lev=10,commisoin=0):
    self.JPY = JPY  # 保有する円
    self.deposit = 0  # 保証金（円）
    self.USD = 0 # 取引しているドル
    self.MP_max = JPY  # 時価の最高値
    self.MP_min = JPY  # 時価の最安値
    self.lev = lev  # レバレッジ　 
  
  def get_MP(self,rate):  # Market Price
    return self.JPY + self.deposit + self.USD*rate - self.deposit*self.lev 
  
  def max_min(self,rate):
    self.MP_max = max(self.MP_max,self.get_MP(rate))
    self.MP_min = min(self.MP_min,self.get_MP(rate))

  def buy_USD(self,yen,rate):
    self.JPY -= yen
    self.deposit += yen
    self.USD += yen*self.lev/rate
  
  def sell_USD(self,dollar,rate):
    ## if self.deposit*(dollar/self.USD)*self.lev < dollar*rate:
    self.JPY += self.deposit*(dollar/self.USD) + dollar*rate - self.deposit*(dollar/self.USD)*self.lev
    self.deposit -= self.deposit*(dollar/self.USD) + dollar*rate - self.deposit*(dollar/self.USD)*self.lev
    self.USD -= dollar
    if self.deposit < 0:
      self.JPY += self.deposit
      self.deposit = 0
      print("保証金が不足しました．")

  def debug(self,rate):
    print(f"""\
==================================
rate            {rate}
JPY             {self.JPY}
USD             {self.USD}
deposit         {self.deposit}
Market price    {self.get_MP(rate)}
==================================""")



def main():
  import pandas_datareader.data as pdr
  import datetime
  import numpy
  start = datetime.datetime(2018,12,19)
  end = datetime.datetime(2020,12,18)
  JPY_USD = pdr.DataReader('DEXJPUS', 'fred', start, end)
  JPY_USD = JPY_USD.dropna(how='any')

  money = Money(JPY=1000000,lev=10)
  ## money.debug(row.DEXJPUS)
  step = 0
  step_money = numpy.array([10000,20000,40000,80000,160000,320000,640000,1280000,2560000])
  dev = 0
  for index, row in JPY_USD.iterrows():
    no_transaction = False
    if step == 0:
      money.buy_USD(step_money[step],row.DEXJPUS)
      print(money.deposit)
      print(money.JPY)
      print(money.USD)
      print(money.get_MP(row.DEXJPUS))
      print(money.lev)
      step +=1
    else:
      if standard +1 < row.DEXJPUS:
      ## if standard + 0.8 < row.DEXJPUS:
        money.sell_USD(money.USD,row.DEXJPUS)
        step = 0
        money.buy_USD(step_money[step],row.DEXJPUS)
        step += 1
        standard = row.DEXJPUS
      elif standard -1 > row.DEXJPUS and step:
      ## elif standard -0.8 > row.DEXJPUS:
        if money.JPY > step_money[step]:
          money.buy_USD(step_money[step],row.DEXJPUS)
          step += 1
          standard = row.DEXJPUS
        else:
          print('損切りします．')
          money.sell_USD(money.USD,row.DEXJPUS)
          step = 0
          money.buy_USD(step_money[step],row.DEXJPUS)
          step += 1
      else:
        no_transaction = True
    ## print('デバッグ', money.get_MP(row.DEXJPUS))
    if not no_transaction:
      money.debug(row.DEXJPUS)
      print('step', step)
      dev += 1
      if dev == 10:
        import sys
        sys.exit()
    money.max_min(row.DEXJPUS)
    if not no_transaction:
      standard = row.DEXJPUS
      ## print(f"{index}:レート={row.DEXJPUS}, step={step}")
  print('最終時価総額:',money.get_MP(row.DEXJPUS))
  print('最高時価総額', money.MP_max)
  print('最低時価総額', money.MP_min)

if(__name__ == '__main__'):
  main()
