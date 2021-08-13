# Name:
# ID:
# Assignment 2 : OOP
# ====================================
import math
class POSE:
	def __init__(self, x,y,angle):
		self.x=x
		self.y=y
		self.angle=angle

	def printPose(self):
		print(self.x, self.y, self.angle)

class TWOWHEELEDROBOT(POSE):	
	def __init__(self, x, y, angle, wL, wR):
		POSE.__init__(self, x, y, angle)
		self._casterDiameter = 0.020 # caster diameter in meters
		self._robotDiameter = 0.080 # L in meters
		self.wL = 0
		self.wR = 0
		self._vl = 0
		self._vr = 0
		self.setWheelSpeed(wL, wR)
	def setPose(self, x, y, angle):
		self.x = x
		self.y = y
		self.angle = angle
		return self.x, self.y, self.angle
	def setWheelSpeed(self, wL, wR):
		self.wL = wL
		self.wR = wR
		self._vl = (self._casterDiameter/2) * self.wL
		self._vr = (self._casterDiameter/2) * self.wR
		return self.wL, self.wR
	def getVL(self): # return left wheel linear velocity
		return self._vl
	def getVR(self):# return right wheel linear velocity
		return self._vr
	def getV(self):# return linear velocity of robot body
		return (self._vr + self._vl) / 2.0
	def getICR(self):# return angular velocity of robot's body and Radius of rotation
		self.radius = self._robotDiameter / 2.0
		self._w  = (self._vr-self._vl) / self.radius
		if self._vr == self._vl :
			self._r = 0.0
		else :
			self._r = self.radius * ((self._vr + self._vl) / (self._vr - self._vl))
		return self._w,  self._r


if __name__ == "__main__":
	case1 = TWOWHEELEDROBOT(0, 0, math.pi/2, 10, 10)
	case2 = TWOWHEELEDROBOT(0, 0, math.pi/2, 10, -10)
	case3 = TWOWHEELEDROBOT(0.5, 0.5, math.pi/2, 10, 20)
	print("---------------------------------------")
	print("case1")
	#print(f"pose={case1.x},{case1.y},{case1.angle}")
	print("pose= {}, {}, {}".format(case1.x, case1.y, case1.angle))
	print("wL = " + str(case1.wL))
	print("wR = " + str(case1.wR))
	print("VL = " + str(case1.getVL()))
	print("VR = " + str(case1.getVR()))
	print("ICR = " + str(case1.getICR()))
	print("---------------------------------------")
	print("case2")
	print("pose= {}, {}, {}".format(case2.x, case2.y, case2.angle))
	print("wL = " + str(case2.wL))
	print("wR = " + str(case2.wR))
	print("VL = " + str(case2.getVL()))
	print("VR = " + str(case2.getVR()))
	print("ICR = " + str(case2.getICR()))
	print("---------------------------------------")
	print("case3")
	print("pose= {}, {}, {}".format(case3.x, case3.y, case3.angle))
	print("wL = " + str(case3.wL))
	print("wR = " + str(case3.wR))
	print("VL = " + str(case3.getVL()))
	print("VR = " + str(case3.getVR()))
	print("ICR = " + str(case3.getICR()))