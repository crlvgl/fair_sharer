# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:20:32 2023

@author: vogel
"""


from fair_sharer import fair_sharer as fs


def test_fair_sharer():

    assert fs([100, 800, 500, 300]) == [180.0, 640.0, 580.0, 300.0]
    assert fs([100, 800, 500, 300], 2) == [244.0, 512.0, 644.0, 300.0]
    assert fs([100, 800, 500, 300], share=0.2) == [260.0, 480.0, 660.0, 300.0]
    assert fs([100, 800, 500, 300], 2, 0.2) == [260.0, 612.0, 396.0, 432.0]
    
    assert fs([1000, 100, 600, 200]) == [800.0, 200.0, 600.0, 300.0]
    assert fs([1000, 100, 600, 200], 2) == [640.0, 280.0, 600.0, 380.0]
    assert fs([1000, 100, 600, 200], share=0.2) == [600.0, 300.0, 600.0, 400.0]
    assert fs([1000, 100, 600, 200], 2, 0.2) == [360.0, 420.0, 600.0, 520.0]
    assert fs([1000, 100, 600, 200], 3, 0.2) == [360.0, 540.0, 360.0, 640.0]

if __name__ == "__main__":
    test_fair_sharer()
