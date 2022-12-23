import WheelDecide
w = WheelDecide.wheel()
w.setTitle("Input Wheel")
w.setMinsize(800,800)
w.setBtnSize(100)
w.setSelectedBgcolor("yellow")
w.setUnselectedBgcolor("blue")
w.setTimeInterval(0.02)
w.setupwheel(input().split(','))
