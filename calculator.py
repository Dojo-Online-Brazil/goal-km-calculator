#!/usr/bin/python

import unittest
from datetime import date

def goalByDay(goal):
	return goal / 365

def goalExpected(goalByDay):
	today = date.today()
        beginningOfYear = date(date.today().year, 1, 1)
	days = today - beginningOfYear
	return goalByDay * days

def goalUntilEndOfYear(goal):
        today = date.today()
        endOfYear = date(date.today().year, 12, 31)
        days = endOfYear - today
	return goal / days.days


class GoalByDayTest(unittest.TestCase):

	def test365(self):
		self.failIf(goalByDay(365) != 1)
	def test730(self):
		self.failIf(goalByDay(730) != 2)
        def test182(self):
		self.failIf(goalByDay(182.5) != 0.5)

class GoalExpected(unittest.TestCase):

	def testOne(self):
		days = getDays()
		self.failIf(goalExpected(1) != days)
     
	def testTwo(self):
                days = getDays()
                self.failIf(goalExpected(2) != days * 2)

class GoalUntilEndOfYear(unittest.TestCase):

	def testOne(self):
                today = date.today()
                endOfYear = date(today.year, 12, 31)
		days = endOfYear - today
		self.failIf(goalUntilEndOfYear(days.days) != days.days / days.days)

def getDays():
        today = date.today()
        beginningOfYear = date(date.today().year, 1, 1)
        return today - beginningOfYear

def main():
	unittest.main()

if __name__ == '__main__':
    main()
