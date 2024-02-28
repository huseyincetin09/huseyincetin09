import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.SpeedControllerGroup;
import edu.wpi.first.wpilibj.Talon;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;

public class Robot extends IterativeRobot {
    private DifferentialDrive differentialDrive;
    private Joystick joystick;
    private SpeedControllerGroup motor_intake;
    private SpeedControllerGroup motor_elevator;
    private SpeedControllerGroup motor_left;
    private SpeedControllerGroup motor_right;
    private SpeedControllerGroup motor_wrist_left;
    private SpeedControllerGroup motor_wrist_right;

    public void robotInit() {
        motor_elevator = new Talon(0);
        motor_intake = new Talon(1);
        motor_wrist_left = new Talon(2);
        motor_wrist_right = new Talon(3);
        motor_left = new Talon(4);
        motor_right = new Talon(5);
        joystick = new Joystick(0);
        differentialDrive = new DifferentialDrive(motor_right, motor_left);
    }

    public void teleopPeriodic() {
        double right_speed = joystick.getRawAxis(5);
        double left_speed = joystick.getRawAxis(1);
        double elevator_speed = -joystick.getRawAxis(1);
        double intake_speed = joystick.getRawAxis(2);
        double wrist_speed = joystick.getRawAxis(3);
        motor_intake.set(intake_speed);
        motor_wrist_left.set(wrist_speed);
        motor_wrist_right.set(-wrist_speed);
        motor_elevator.set(elevator_speed);
        motor_left.set(left_speed);
        motor_right.set(right_speed);
    }
}
