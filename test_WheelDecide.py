import WheelDecide
w = WheelDecide.wheel()
w.setMinsize(800,800)
w.setBtnInterval(100)
w.setSelectedBgcolor("yellow")
w.setUnselectedBgcolor("blue")
w.setTimeInterval(0.02)
w.setupwheel(input().split(','))
