#include <stdio.h>

int main(){
    char name[10];
    int sensor_ids[10];
    double precision_readings[10];

    printf("The size of name in bytes: %d\n", sizeof(name));
    printf("The size of sensor data in bytes: %d\n", sizeof(sensor_ids));
    printf("The size of precision readings data: %d\n\n", sizeof(precision_readings));

    int count_name = sizeof(name)/sizeof(name[0]);
    int count_sensor_ids = sizeof(sensor_ids)/sizeof(sensor_ids[0]);
    int count_precision_readings = sizeof(precision_readings)/sizeof(precision_readings[0]);

    printf("Name count: %d\n", count_name);
    printf("Sensor data count: %d\n", count_precision_readings);
    printf("Precision data count: %d\n", count_precision_readings);

    return 0;
}