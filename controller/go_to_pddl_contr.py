from controller import Robot, Motor, GPS, Compass, InertialUnit
import math

# Определение основных параметров
TIME_STEP = 32
MAX_SPEED = 6.28

# Функция для вычисления угла между текущим направлением робота и целью
def bearing_to_point(current_position, target_position, current_orientation):
    delta_x = target_position[0] - current_position[0]
    delta_z = target_position[2] - current_position[2]
    angle_to_target = math.atan2(delta_z, delta_x)
    return angle_to_target - current_orientation

# Инициализация робота
robot = Robot()

# Получение доступа к моторам
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Инициализация GPS и компаса
gps = robot.getDevice('gps')
gps.enable(TIME_STEP)
compass = robot.getDevice('compass')
compass.enable(TIME_STEP)
imu = robot.getDevice('inertial unit')
imu.enable(TIME_STEP)

# Список целевых координат
waypoints = [(1.0, 0.0, 1.5), (2.0, 0.0, 3.0), (3.0, 0.0, 1.0)]

# Основной цикл управления
current_target = 0
while robot.step(TIME_STEP) != -1 and current_target < len(waypoints):
    current_position = gps.getValues()
    current_orientation = imu.getRollPitchYaw()[2]  # Yaw из IMU (инерциального блока)
    
    if current_target < len(waypoints):
        angle_to_target = bearing_to_point(current_position, waypoints[current_target], current_orientation)
        
        # Проверка, достаточно ли близко робот к цели
        distance_to_target = math.sqrt((current_position[0] - waypoints[current_target][0]) ** 2 +
                                       (current_position[2] - waypoints[current_target][2]) ** 2)
        if distance_to_target < 0.2:  # Робот достиг цели
            current_target += 1
        else:
            if abs(angle_to_target) > 0.1:  # Нужен поворот к цели
                left_motor.setVelocity(-angle_to_target * 0.5 * MAX_SPEED)
                right_motor.setVelocity(angle_to_target * 0.5 * MAX_SPEED)
            else:  # Двигаться вперед
                left_motor.setVelocity(MAX_SPEED)
                right_motor.setVelocity(MAX_SPEED)

robot.cleanup()