from controller import Robot, Motor, DistanceSensor, Accelerometer, Gyro, Compass, Camera, Lidar

# Параметры симуляции
TIME_STEP = 32
MAX_VELOCITY = 26

# Инициализация робота
robot = Robot()

# Получение доступа к моторам
motors = []
motor_names = ["fl_wheel_joint", "fr_wheel_joint", "rl_wheel_joint", "rr_wheel_joint"]
for name in motor_names:
    motor = robot.getDevice(name)
    motor.setPosition(float('inf'))
    motor.setVelocity(0.0)
    motors.append(motor)

# Инициализация датчиков расстояния
distance_sensors = []
distance_sensor_names = ["fl_range", "fr_range", "rl_range", "rr_range"]
for name in distance_sensor_names:
    sensor = robot.getDevice(name)
    sensor.enable(TIME_STEP)
    distance_sensors.append(sensor)

# Инициализация LIDAR
lidar = robot.getDevice("laser")
lidar.enable(TIME_STEP)
lidar.enablePointCloud()

# Инициализация IMU компонентов
accelerometer = robot.getDevice("imu accelerometer")
accelerometer.enable(TIME_STEP)

gyro = robot.getDevice("imu gyro")
gyro.enable(TIME_STEP)

compass = robot.getDevice("imu compass")
compass.enable(TIME_STEP)

# Инициализация камер
camera_rgb = robot.getDevice("camera rgb")
camera_rgb.enable(TIME_STEP)

camera_depth = robot.getDevice("camera depth")
camera_depth.enable(TIME_STEP)

# Эмпирические коэффициенты для избежания столкновений
coefficients = [[15.0, -9.0], [-15.0, 9.0]]

# Основной цикл управления
while robot.step(TIME_STEP) != -1:
    # Чтение значений с датчиков расстояния
    distance_values = [sensor.getValue() for sensor in distance_sensors]

    # Вычисление скоростей для избежания препятствий
    avoidance_speed = [0.0, 0.0]
    base_speed = 6.0
    for i in range(2):
        for j in range(2):
            avoidance_speed[i] += (2.0 - distance_values[j+1]) ** 2 * coefficients[i][j]
    
    motor_speed = [base_speed + avoidance for avoidance in avoidance_speed]
    motor_speed = [min(speed, MAX_VELOCITY) for speed in motor_speed]

    # Установка скоростей моторам
    for i, motor in enumerate(motors):
        if i % 2 == 0:  # Левые моторы
            motor.setVelocity(motor_speed[0])
        else:  # Правые моторы
            motor.setVelocity(motor_speed[1])

# Очистка и завершение работы с роботом
robot.cleanup()