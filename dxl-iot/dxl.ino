#include <Ethernet.h>
#include <EthernetUdp.h>
#include <EEPROM.h>
#include "DxlMaster.h"

const uint8_t id = 1;
int16_t speed = -512;
const long unsigned int baudrate = 57600;

#define UDP_PORT 8888
IPAddress MyIP(192, 168, 43, 13);

EthernetUDP udp;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
byte mac[6];

bool motorEnabled = false;
DynamixelMotor motor(id);

void setup() {
  Serial.begin(115200);
  
  mac[0] = MyIP[0];
  mac[1] = MyIP[1];
  mac[2] = MyIP[2];
  mac[3] = MyIP[3];
  mac[4] = MyIP[2];
  mac[5] = MyIP[3];
  
  Ethernet.begin(mac, MyIP);
  udp.begin(UDP_PORT);
  
  Serial.println("----------------------");
  Serial.println("UDP connection is at: ");
  Serial.println(Ethernet.localIP());
  Serial.println("----------------------");
  Serial.println("Commands: k:1 - enable motor, k:0 - disable motor");
  Serial.println("----------------------");
  
  DxlMaster.begin(baudrate);
  delay(100);
  
  uint8_t status = motor.init();
  if(status != DYN_STATUS_OK) {
    Serial.println("Motor initialization failed!");
    while(1);
  }
  
  Serial.println("Motor initialized successfully");
  motor.enableTorque();  
  motor.wheelMode();
  motor.speed(0); 
}

void processUdp() {
  int packetSize = udp.parsePacket();
  if (packetSize) {

    Serial.print("From ");
    IPAddress remote = udp.remoteIP();
    for (int i = 0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) Serial.print(".");
    }
    Serial.print(", port ");
    Serial.println(udp.remotePort());
    
    udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE - 1);
    packetBuffer[packetSize] = '\0'; 
    
    Serial.print("Command: ");
    Serial.println(packetBuffer);
    

    if (strncmp(packetBuffer, "k:1", 3) == 0) {
      motorEnabled = true;
      motor.speed(speed);
      Serial.println("Motor ENABLED with speed: " + String(speed));
    }
    else if (strncmp(packetBuffer, "k:0", 3) == 0) {
      motorEnabled = false;
      motor.speed(0);
      Serial.println("Motor DISABLED (speed set to 0)");
    }
    else {
      Serial.println("Unknown command. Use 'k:1' or 'k:0'");
    }
  }
}

void loop() {
  processUdp();
  delay(10); 
}