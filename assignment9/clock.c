/*SIMPLE DIGITAL CLOCK USING MULTITHREADING*/
/*MIS:111803072*/
#include<stdlib.h>
#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<time.h>


pthread_mutex_t lock;
int seconds = 50, minutes = 59, hours = 23;

void* print_hr(void* pString)
{
    pthread_mutex_lock(&lock);
    if(minutes > 59){
        hours++;
        minutes = 0;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

void* print_min(void* pString)
{
    pthread_mutex_lock(&lock);
    if(seconds > 59) {
        minutes++;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

void* print_sec(void* pString)
{
    pthread_mutex_lock(&lock);
    //seconds++;
    if(seconds == 59 && minutes == 59 && hours == 23){
        hours = 0;
        minutes = 0;
        seconds = -1;
    }
    seconds++;
    pthread_mutex_unlock(&lock);
    return 0;
}

int main() {
    printf("Enter the time in HH:MM:SS format.\n");
    scanf("%d%d%d", &hours, &minutes, &seconds);
    pthread_t second_thread, minute_thread, hours_thread;
    printf("HH:MM:SS\n");
    while(1) {
        sleep(1);
        pthread_create(&second_thread, NULL, print_sec, NULL);
        pthread_join(second_thread, NULL);
        pthread_create(&minute_thread, NULL, print_min, NULL);
        pthread_join(minute_thread, NULL);
        pthread_create(&hours_thread, NULL, print_hr, NULL);
        pthread_join(hours_thread, NULL);
        
        
        printf("%2d:%2d:%2d\n", hours, minutes, seconds);
    }
    return 0;
}