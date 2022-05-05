
TIME_STEP = 64;
max_speed=6.28;

left_motor=wb_robot_get_device('left wheel motor');
right_motor=wb_robot_get_device('right wheel motor');
wb_motor_set_position(left_motor,inf);
wb_motor_set_position(right_motor,inf);
wb_motor_set_velocity(left_motor,0.0);
wb_motor_set_velocity(right_motor,0.0);

left_ir=wb_robot_get_device('ir0');
wb_distance_sensor_enable(left_ir,TIME_STEP);
right_ir=wb_robot_get_device('ir1');
wb_distance_sensor_enable(right_ir,TIME_STEP);


while (wb_robot_step(TIME_STEP) ~= -1)
  left_ir_value=wb_distance_sensor_get_value(left_ir);
  right_ir_value=wb_distance_sensor_get_value(right_ir);
  left_speed=max_speed*0.25;
  right_speed=max_speed*0.25;
  if ((left_ir_value > right_ir_value) && (6<left_ir_value<15))
    fprintf("go left");  
    left_speed=left_speed - (max_speed*0.25);
    right_speed=max_speed*0,25;
  else if((left_ir_value < right_ir_value)&&(6<right_ir_value<15)
    fprintf("go right");
    right_speed= right_speed- (max_speed*0.25);
    left_speed=max_speed*0.25;
  end
  wb_motor_set_velocity(left_motor,left_speed);
  wb_motor_set_velocity(right_motor,right_speed);
end
