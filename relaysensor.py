 import RPi.GPIO as GPIO
import urllib2
import time
import smbus

time.sleep(5)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(14,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
true = 1

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)

	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

while(true):
    try:
        response = urllib2.urlopen('https://alarmmotoriot.000webhostapp.com/buttonStatus.txt')
        status = response.read()
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.args
    if status=='OFF':
        GPIO.output(14,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(24,GPIO.HIGH)
    if status=='ON1':
        GPIO.output(14,GPIO.LOW)
        time.sleep(3)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        time.sleep(3)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(23,GPIO.HIGH)
    if status=='ON2':
        GPIO.output(14,GPIO.LOW)
        time.sleep(1)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(14,GPIO.HIGH)
        time.sleep(1)
    if status=='ON3':
        gyro_x = read_raw_data(GYRO_XOUT_H)
        Gx = gyro_x/131.0
        if Gx<6.4 or Gx>6.8:
            GPIO.output(14,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(24,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(24,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(24,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(24,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(24,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(24,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(24,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(14,GPIO.HIGH)
        if Gx>6.4 and Gx<6.8:
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(14,GPIO.HIGH)