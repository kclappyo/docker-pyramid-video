from easytello import tello

# Create drone instance
print("Connecting to tello!")
drone = tello.Tello()
print("Connected!")

print("Turning Stream on")

drone.streamon()
drone.wait(30)

drone.streamoff()
print("Turning Stream off")