#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 12月, 19, 2022 17:30:35

class Money:
  def __init__(self,cash,commisoin=0, max_lev=25):
    self.cash = cash  # 現金
    self.deposit = 0  # 預け入れ金=保証金（円）
    self.JPY  # ドル購入資金
    self.USD = 0 # 取引しているドル
    self.MP_max = JPY  # 時価の最高値
    self.MP_min = JPY  # 時価の最安値
    self.max_lev = max_lev  # 最大レバレッジ　 
  
  def cash2deposit(self,yen):
    if 0 < yen <= self.cash:
      self.cash -= yen
      self.deposit += yen
    else:
      raise ValueError

  def deposit2cash(self,yen,rate):
    if yen>0:
      if (self.deposit - yen) * self.max_lev > self.JPY
        self.deposit -= yen
        self.cash += yen
      else:
        print('必要な保証金額は残す必要があります.')
    else:
      raise ValueError

  def get_MP(self,rate):  # Market Price
    return self.cash + self.deposit + self.USD*rate - self.JPY

  def max_min(self,rate):
    self.MP_max = max(self.MP_max,self.get_MP(rate))
    self.MP_min = min(self.MP_min,self.get_MP(rate))

  def buy_USD(self,yen,rate):
    if yen>0:
      if yen + self.JPY < self.deposit * self.max_lev:
        self.JPY += yen
        self.USD += yen/rate
      else:
        print("保証金が不足しています.")
    else:
      raise ValueError

  def sell_USD(self,dollar,rate):
    if 0 < dollar <= self.USD:
      self.JPY -= dollar*rate
      self.USD -= dollar
    else:
      raise ValueError

  def profit2deposit(self,rate):
    deposit += self.USD*rate-self.JPY
    self.USD = self.JPY/rate
    if deposit < 0:
      print("保証金が不足したいるため追加します.")
      try:
        self.cash2deposit(abs(deposit))
        deposit = 0
      except ValueError:
        print("破産しました.")
        sys.exit()


  def debug(self,rate):
    print(f"""\
==================================
rate            {rate}
JPY             {self.JPY}
USD             {self.USD}
deposit         {self.deposit}
Market price    {self.get_MP(rate)}
==================================""")

class Exponentiation_strategy:
  def __init__(self,first,max_step):
    self.first = first
    self.max_step = max_step:
    self.step = 0 
  def next_step(self,money,rate):
    step += 1
    return first * 2**(i-1)
  def first_step(self,money,rate):
    step = 0
    step += 1
    return first * 2**(i-1)

def main():
  import pandas_datareader.data as pdr
  import datetime
  import numpy
  start = datetime.datetime(2018,12,19)
  end = datetime.datetime(2020,12,18)
  JPY_USD = pdr.DataReader('DEXJPUS', 'fred', start, end)
  JPY_USD = JPY_USD.dropna(how='any')

  money = Money(cash=1000000)
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
