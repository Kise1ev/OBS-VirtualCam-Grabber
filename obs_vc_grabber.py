import cv2

class OBSGrabber:
	def __init__(self):
		self.cap_size_set = False
		self.device = self.find_obs_vc()
		if not self.device:
			raise ValueError("OBS Virtual Camera not found")

	def find_obs_vc(self):
		for index in range(10):
			capture = cv2.VideoCapture(index)
			if capture.isOpened():
				return capture
		return None
	
	def set_cap_size(self, width, height):
		self.device.set(cv2.CAP_PROP_FRAME_WIDTH, width)
		self.device.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

	def get_frame(self, grab_area):
		if not self.cap_size_set:
			self.set_cap_size(grab_area["width"], grab_area["height"])
			self.cap_size_set = True
		ret, frame = self.device.read()
		# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		if not ret:
			raise RuntimeError("Failed to read frame from OBS Virtual Camera")
		return frame
		