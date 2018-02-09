Goal:
	学习图像的不用的形态变换，如侵蚀、扩张、打开、关闭等等
	可能将使用到的函数 cv2.erode()	 	cv2.dilate() 	cv2.morphoogyEx()

原理：
	形态转换是基于图形形状的一些简单操作。
	一般情况来说是基于双值图像的。
	需要两个输入，一个输入是源图像，另外一个决定操作本质的输入
	被称为 结构元素(structuring elements) 或者 内核(kernel)

	最基本的两个形态转换时 腐蚀(Erosion) 和 膨胀(Dilation)
	另外还有基于他们的变体模式例如 Opening, Closing, Gradient等