from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the model and place it at the origin (0, 0, 0)
        self.model = self.loader.load_model("Character_Head_Model_OBJ.obj")
        self.model.reparent_to(self.render)
        self.model.set_pos(0, 0, 0)  # Keep the model at the center
        self.model.set_scale(1)      # Use the original size of the model (no scaling)

        # Set initial rotation values: yaw=0, pitch=85
        self.model_yaw = 0    # Horizontal rotation (yaw)
        self.model_pitch = 85  # Vertical tilt (pitch)
        self.model.set_hpr(self.model_yaw, self.model_pitch, 0)  # Apply the rotation

        # Camera settings (Y=0, Z=9)
        self.camera_y_position = 0    # Fixed camera Y position
        self.camera_z_position = 9    # Initial camera Z position (above the model)
        self.update_camera()          # Set initial camera position

        # Movement step size for model pitch (W and S keys)
        self.pitch_step = 5

        # Accept input for zooming (+ and -)
        self.accept("+", self.zoom_camera, [-1])  # Zoom in (move camera closer)
        self.accept("-", self.zoom_camera, [1])   # Zoom out (move camera farther)

        # Accept input for controlling model pitch (W and S keys)
        self.accept("w", self.change_pitch, [-self.pitch_step])  # Increase pitch (tilt up)
        self.accept("s", self.change_pitch, [self.pitch_step])   # Decrease pitch (tilt down)

    # Update the camera position (Y is fixed at 0, Z can change)
    def update_camera(self):
        # Move the camera on the Z axis, keeping X and Y fixed
        base.cam.set_pos(0, self.camera_y_position, self.camera_z_position)
        base.cam.look_at(self.model)  # Ensure camera is always looking at the model

    # Zoom the camera in and out (modifies the Z-axis position for zooming)
    def zoom_camera(self, zoom_delta):
        self.camera_z_position += zoom_delta  # Adjust the Z position for zoom
        self.update_camera()

    # Change the pitch of the model (rotates the model along the X-axis)
    def change_pitch(self, pitch_delta):
        self.model_pitch += pitch_delta  # Adjust the pitch of the model
        self.model.set_hpr(self.model_yaw, self.model_pitch, 0)  # Apply the new pitch

        # Print the current pitch of the model
        print(f"Model Pitch: {self.model_pitch}")

# Run the app
app = MyApp()
app.run()
