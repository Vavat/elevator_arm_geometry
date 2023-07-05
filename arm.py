class Arm():
    
    def __init__(self, shoulder, elbow, origin = (0,0)):
        if shoulder > 0:
            self._shoulder = shoulder
        else:
            raise Exception('Shoulder size cannot be negative.') 
        if elbow > 0:
            self._elbow = elbow
        else:
            raise Exception('Elbow size cannot be negative.') 
        if len(origin) == 2:
            self._origin = origin
        else:
            raise Exception('Origin must be a tuple of size two.') 
        self._b_homed = False
    