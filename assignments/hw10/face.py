from graphics import Circle, Line



class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        head_size = self.head.getRadius()
        head_center = self.head.getCenter()
        mouth_size = 0.8 * head_size
        mouth_off = head_size / 2.0
        point_3 = head_center.clone()
        point_3.move(0, m_off * 1.8)
        point_1 = head_center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = head_center.clone()
        point_2.move(-mouth_size / 2, mouth_off)
        l_l = Line(point_1, point_3)
        r_l = Line(point_2, point_3)
        r_l.draw(self.window)
        l_l.draw(self.window)



    def shock(self):
        size = self.head.getRadius()
        mouth_size = 0.20 * size
        mouth_center = self.mouth.getCenter()
        shkd = Circle(mouth_center, mouth_size)
        self.mouth.undraw()
        self.mouth = shkd
        self.mouth.draw(self.window)

    def wink(self):
        head_size = self.head.getRadius()
        head_center = self.head.getCenter()
        eye = head_size / 3.0
        point_1 = head_center.clone()
        point_1.move(- eye / 1.6, - eye)
        point_2 = head_center.clone()
        point_2.move(eye / 2, - eye)
        n_eye = Line(point_1, point_2)
        n_eye.draw(self.window)
        self.smile()
