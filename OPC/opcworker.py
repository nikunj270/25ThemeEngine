from PySide6.QtCore import QThread, QTimer
from Tag.tags import Tags
import time

from Alarm.alarm_db import init_alarm_db
from Alarm.alarms import register_default_alarms, AlarmEngine
# from core.Spare import AlarmController  
from OPC import nodes
from Logger.logger import log_tag
from Logger.csv_logger import log_to_csv
# from Functions import AppFunctions

# class OPCWorker(QThread):
class OPCWorker(QThread):

    def __init__(self, plc_client):

        super().__init__()
        self.plc_client = plc_client
        self.running = True
        #AlarmEngine.check()
        

    def run(self):
        alarm_check_interval = 2.0  # Time in seconds to check alarms
        log_interval = 5.0
        csv_log_interval = 1.0
        last_alarm_check = None
        last_log_check = None
        last_csv_check = None
        if  last_alarm_check is None:
            last_alarm_check = 0.0
        if  last_log_check is None:
            last_log_check = 0.0
        if  last_csv_check is None:
            last_csv_check = 0.0

        #time.sleep(0.1)  # Initial delay to allow PLC connection before starting loop
        self.msleep(5000)  # Sleep to reduce CPU usage, adjust as needed for responsiveness
        print("work Start")

        
        while self.running: # and not self.isInterruptionRequested():
            


            # Read all process tags from OPC server.
            # For future addition, update core/tags.py and OPC/nodes.py, then add reads here.
            # Tags.Motor = self.plc_client.read_bool(nodes.Motor)
            # Tags.Temperature  = self.plc_client.read_real(nodes.Temperature)
            # Tags.Pressure = self.plc_client.read_int16(nodes.Pressure)

            # Tags.Motor = self.plc_client.read_real(nodes.Motor)
            # Tags.Temperature  = self.plc_client.read_real(nodes.Temperature)
            # Tags.Pressure = self.plc_client.read_real(nodes.Pressure)

            Tags.M1bool = self.plc_client.read_bool(nodes.M1_mastered)
            Tags.M2bool = self.plc_client.read_bool(nodes.M2_mastered)  
            Tags.M3bool = self.plc_client.read_bool(nodes.M3_mastered)
            
            Tags.M1real = self.plc_client.read_real(nodes.M1_current_bit)
            Tags.M2real = self.plc_client.read_real(nodes.M2_current_bit)
            Tags.M2int1 = self.plc_client.read_int16(nodes.M2_tag1)
            Tags.M2int2 = self.plc_client.read_int16(nodes.M2_tag2)
           
            current_time = self.get_current_time()
            if current_time - last_alarm_check >= alarm_check_interval:
                # Enable live alarm scanning by uncommenting these lines.
                # AlarmEngine.check_all()  # Core alarm state and DB insert/clear
                # AlarmController.refresh(self)  # UI refresh if using AlarmController directly
                last_alarm_check = current_time
            if current_time - last_log_check >= log_interval:
                self.log_process_dat()
                last_log_check = current_time
            if current_time - last_csv_check >= csv_log_interval:
                log_to_csv()
                last_csv_check = current_time

            self.msleep(100)  # Sleep to reduce CPU usage, adjust as needed for responsiveness
            #time.sleep(0.1)
    
    def stop(self):
        self.running = False
        self.requestInterruption()
        self.quit()
        self.wait(3000)
        
       


    def log_process_dat(self):
        # print("Logging process data")
        temp = Tags.M1real
        motor = Tags.M1bool

        log_tag("TEMP", temp)
        log_tag("MOTOR", motor)

    def get_current_time(self):
        return time.time()
    
    

            
