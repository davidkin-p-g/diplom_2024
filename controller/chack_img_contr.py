# Create a robot instance and initialize devices.
robot = Robot()
time_step = int(robot.getBasicTimeStep())

# initialize devices
##Motor
front_left_motor = robot.getDevice("fl_wheel_joint")
front_right_motor = robot.getDevice("fr_wheel_joint")
rear_left_motor = robot.getDevice("rl_wheel_joint")
rear_right_motor = robot.getDevice("rr_wheel_joint")
### Set Position
front_left_motor.setPosition(float('inf'))
front_right_motor.setPosition(float('inf'))
rear_left_motor.setPosition(float('inf'))
rear_right_motor.setPosition(float('inf'))
### Set Position
front_left_motor.setPosition(float('inf'))
front_right_motor.setPosition(float('inf'))
rear_left_motor.setPosition(float('inf'))
rear_right_motor.setPosition(float('inf'))
### Set Velocity
front_left_motor.setVelocity(0.0)
front_right_motor.setVelocity(0.0)
rear_left_motor.setVelocity(0.0)
rear_right_motor.setVelocity(0.0)


##Sensor
front_left_position_sensor = robot.getDevice("front left wheel motor sensor")
front_right_position_sensor = robot.getDevice("front right wheel motor sensor")
rear_left_position_sensor = robot.getDevice("rear left wheel motor sensor")
rear_right_position_sensor = robot.getDevice("rear right wheel motor sensor")
###Enable
front_left_position_sensor.enable(time_step)
front_right_position_sensor.enable(time_step)
rear_left_position_sensor.enable(time_step)
rear_right_position_sensor.enable(time_step)


##Camera
camera = robot.getDevice("camera rgb")
#camera_depth = robot.getDevice("camera depth")
rangefinder = robot.getDevice("camera depth")
print(camera.getName)
###Enable
camera.enable(time_step)
#camera_depth.enable(time_step)
rangefinder.enable(time_step)

##Ladar
lidar = robot.getDevice("laser")
lidar.enable(time_step)
lidar.enablePointCloud()
#enable point cloud

## IMU device
accelerometer = robot.getDevice("imu accelerometer")
gyro = robot.getDevice("imu gyro")
compass = robot.getDevice("imu compass")
###Enable
accelerometer.enable(time_step)
gyro.enable(time_step)
compass.enable(time_step)

##Distance sensor
distance_sensors = {}
distance_sensors['fl'] = robot.getDevice("fl_range")
distance_sensors['rl'] = robot.getDevice("rl_range")
distance_sensors['fr'] = robot.getDevice("fr_range")
distance_sensors['rr'] = robot.getDevice("rr_range")
###Enable
distance_sensors['fl'].enable(time_step)
distance_sensors['rl'].enable(time_step)
distance_sensors['fr'].enable(time_step)
distance_sensors['rr'].enable(time_step)
# camera = robot.getDevice('camera rgb')  # Replace 'cameraName' with your camera's name
# rangefinder = robot.getDevice('camera depth')  # Replace 'rangefinderName' with your rangefinder's name

# camera.enable(timestep)
# rangefinder.enable(timestep)
counter = 26
while robot.step(time_step) != -1:
    # Get the images from the camera and the rangefinder.
    rgb_image = np.frombuffer(camera.getImage(), np.uint8).reshape((camera.getHeight(), camera.getWidth(), 4))
    depth_image = np.array(rangefinder.getRangeImageArray(), dtype=np.float32)
    # Convert RGB image from BGRA to RGB
    rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGRA2RGB)

    # Normalize depth image
    depth_normalized = np.clip((depth_image / 10.0) * 255, 0, 255).astype(np.uint8)

    
    # Assuming both images are of the same dimensions.
    rgbd_image = np.dstack((rgb_image, depth_normalized))  
    

    # Save the normalized depth image as a 16-bit PNG.
    cv2.imwrite(f'rgbd_image_{counter}.jpg', rgbd_image)
    cv2.imwrite(f'depth_image_{counter}.jpg', depth_normalized)
    cv2.imwrite(f'rgb_image_{counter}.jpg', rgb_image)
    create_semantic_context(counter)
    counter += 1

    print("RGB-D image saved as rgbd_image.png2.")
    break  # For this example, we break after the first iteration. Remove this line for continuous operation.