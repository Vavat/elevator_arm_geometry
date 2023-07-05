import math

"""
SCARA-like kinematic conversion of geometry for Marlin.

Raises:
    Exception: _description_
    Exception: _description_
    Exception: _description_
    Exception: _description_

Returns:
    _type_: _description_
"""

class Arm():
    
    """Initialise the class with limb lengths and position of static pivot within the coordinate system.
    """
    def __init__(self, shoulder, elbow, origin_x = 0, origin_y = 0):
        if shoulder > 0:
            self.__shoulder_length = shoulder
        else:
            raise Exception('Shoulder size cannot be negative.') 
        if elbow > 0:
            self.__elbow_length = elbow
        else:
            raise Exception('Elbow size cannot be negative.') 
        self.__origin_x = origin_x
        self.__origin_y = origin_y
        self.__b_homed = False
        self.__position_x = 0
        self.__position_y = 0
        self.__angle = 0
        self.__shoulder_angle = 0
        self.__elbow_angle = 0
        self.__wrist_angle = 0
    
    def __str__(self):
        return f'x:{self.__current_position[0]}, y:{self.__current_position[1]}'

    #TODO: find a way to handle situation where arm needs to be completely straight...
    def forwardKinematics(self, x, y, wrist = 0, rate = 0) -> tuple(float, float, float, float):
        if self.isPositionOK(x, y):
            # Calculate elbow angle. Test for correct angle.
            angle = (x^2 + y^2 - self.__shoulder_length^2 - self.__elbow_length^2)
            angle = angle / (2*self.__shoulder_length*self.__elbow_length)
            if (-1 <= angle) & (self.__elbow_length <= 1):
                self.__elbow_angle = math.acos(angle)
            else:
                raise Exception('Target unreachable.')
            # Calculate shoulder angle
            angle = self.__elbow_length * math.sin(self.__elbow_angle)
            angle = angle / (self.__shoulder_length + self.__elbow_length * math.cos(self.__elbow_angle))
            angle = math.atan(angle)
            self.__shoulder_angle = math.atan(y/x) - angle
            # Calculate wrist angle
            self.__wrist_angle = wrist - self.__shoulder_angle - self.__elbow_angle
        return (self.__shoulder_angle, self.__elbow_angle, 0)
    
    def isPositionOK(self, x, y) -> bool:
        reach = self.__shoulder_length + self.__elbow_length
        position = math.sqrt(x^2 + y^2)
        return (reach >= position)
    
    def getPosition(self) -> tuple[float, float]:
        return (self.__
    
    def setPosition(self, x, y, angle) -> bool:
        b_success = False
        if self.isPositionOK(x, y):
            try: 
                self.forwardKinematics(x, y, angle):
            except Exception as e:
                raise e 
            finally:
                self.__position_x = x
                self.__position_y = y
                self.__angle = angle
                b_success = True
        else:
            raise Exception('Position is not reachable.')
        return b_success

