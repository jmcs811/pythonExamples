#!/usr/bin/env python
 
from collections import Counter
from typing import List
import operator
 
class Type():
 
    ACES = "aces"
    TWOS = "twos"
    THREES = "threes"
    FOURS = "fours"
    FIVES = "fives"
    SIXES = "sixes"
    THREE_OF_A_KIND = "three_of_a_kind"
    FOUR_OF_A_KIND = "four_of_a_kind"
    FULL_HOUSE = "full_house"
    YAHTZEE = "yahtzee"
    SMALL_STRAIGHT = "small_straight"
    LARGE_STRAIGHT = "large_straight"
    CHANCE = "chance"
 
class Roll(Type):
 
    def __init__(self, *args, **kwargs) -> None:
        #try:
            if len(args) == 5:
                self.die1 = args[0]
                self.die2 = args[1]
                self.die3 = args[2]
                self.die4 = args[3]
                self.die5 = args[4]
                self.die_list = [self.die1, self.die2, self.die3, self.die4, self.die5]
            elif len(args) == 1:
                self.die1 = args[0][0]
                self.die2 = args[0][1]
                self.die3 = args[0][2]
                self.die4 = args[0][3]
                self.die5 = args[0][4]
                self.die_list = [self.die1, self.die2, self.die3, self.die4, self.die5]
            elif len(args) < 5:
                raise TypeError("Wrong number of args")
       #except TypeError:
        #    pass
 
    def check_for_nums(self, type_of_check: int) -> int:
        total = 0
        for i in self.die_list:
            if i == type_of_check:
                total += type_of_check
        return total
   
    def multi_of_a_kind(self, num: int) -> int:
        counter = Counter(self.die_list)
        result = [i for i,j in counter.items() if j >= num]
        if len(result) == 1:
            return sum(self.die_list)
        else:
            return 0
 
    # this is because i was getting an odd error on this test:
    # self.assertEqual(Type.FOUR_OF_A_KIND,  Roll(1, 1, 5, 1, 1).best_lower)
    def multi_of_a_kind_alt_version(self, num: int) -> int:
        counter = Counter(self.die_list)
        result = [i for i,j in counter.items() if j == num]
        if len(result) == 1:
            return sum(self.die_list)
        else:
            return 0
 
 
    def is_consecutives(self, num_list_unsorted: List[int], num_of_consecutives: int) -> bool:
        total_consecutive = 1
        num_list = sorted(num_list_unsorted)
        for i in range(4):
            if (num_list[i] + 1) == (num_list[i+1]):
                total_consecutive += 1
        if total_consecutive >= num_of_consecutives:
            return True
        return False
 
    def is_full_house(self, num_list: List[int]) -> bool:
        counter = Counter(num_list)
        if len(counter) > 2:
            return False
        for key, value in counter.items():
            if value == 3 or value == 2:
                return True
        return False
 
    @property
    def aces(self) -> int:
        return self.check_for_nums(1)
       
    @property
    def twos(self) -> int:
       return self.check_for_nums(2)
 
    @property
    def threes(self) -> int:
        return self.check_for_nums(3)
 
    @property
    def fours(self) -> int:
        return self.check_for_nums(4)
 
    @property
    def fives(self) -> int:
        return self.check_for_nums(5)
 
    @property
    def sixes(self) -> int:
        return self.check_for_nums(6)
 
    @property
    def three_of_a_kind(self) -> int:
        return self.multi_of_a_kind(3)
 
    @property
    def four_of_a_kind(self) -> int:
        return self.multi_of_a_kind(4)
 
    @property
    def full_house(self) -> int:
        if self.is_full_house(self.die_list) == True:
            return 25
        else: return 0
 
    @property
    def small_straight(self) -> int:
        if (self.is_consecutives(self.die_list, 4)) == True:
            return 30
        else:
            return 0
 
    @property
    def large_straight(self) -> int:
        if (self.is_consecutives(self.die_list, 5)) == True:
            return 40
        else:
            return 0
 
    @property
    def yahtzee(self) -> int:
        num = self.multi_of_a_kind(5)
        if num > 0:
            return 50
        else:
            return 0
 
    @property
    def chance(self) -> int:
        return sum(self.die_list)
   
    @property
    def best_upper(self) -> str:
        scores = {}
        scores[Type.ACES] = self.aces
        scores[Type.TWOS] = self.twos
        scores[Type.THREES] = self.threes
        scores[Type.FOURS] = self.fours
        scores[Type.FIVES] = self.fives
        scores[Type.SIXES] = self.sixes
        maximum = max(scores, key=scores.get)
        return maximum
   
    @property
    def best_lower(self) -> str:
        scores = {}
        scores[Type.THREE_OF_A_KIND] = self.multi_of_a_kind_alt_version(3)
        scores[Type.FOUR_OF_A_KIND] = self.multi_of_a_kind_alt_version(4)
        scores[Type.FULL_HOUSE] = self.full_house
        scores[Type.SMALL_STRAIGHT] = self.small_straight
        scores[Type.LARGE_STRAIGHT] = self.large_straight
        scores[Type.YAHTZEE] = self.yahtzee
        scores[Type.CHANCE] = self.chance
        maximum = max(scores, key=scores.get)
        return maximum
 
    def score_as(self, the_type: str) -> int:
        if the_type == self.ACES:
            return self.aces
        elif the_type == self.TWOS:
            return self.twos
        elif the_type == self.THREES:
            return self.threes
        elif the_type == self.FOURS:
            return self.fours
        elif the_type == self.FIVES:
            return self.fives
        elif the_type == self.SIXES:
            return self.sixes
        elif the_type == self.THREE_OF_A_KIND:
            return self.three_of_a_kind
        elif the_type == self.FOUR_OF_A_KIND:
            return self.four_of_a_kind
        elif the_type == self.FULL_HOUSE:
            return self.full_house
        elif the_type == self.SMALL_STRAIGHT:
            return self.small_straight
        elif the_type == self.LARGE_STRAIGHT:
            return self.large_straight
        elif the_type == self.YAHTZEE:
            return self.yahtzee
        else:
            return self.chance