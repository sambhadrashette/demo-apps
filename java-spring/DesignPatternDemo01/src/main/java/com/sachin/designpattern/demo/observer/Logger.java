package com.sachin.designpattern.demo.observer;

public class Logger implements Observer{
    private int temp;
    private int windSpeed;
    private int pressure;

    @Override
    public void update(int temp, int windSpeed, int pressure) {
        this.temp = temp;
        this.windSpeed = windSpeed;
        this.pressure = pressure;
        log();
    }

    public void log() {
        System.out.println("logging changes temp="+ temp + ", windSpeed="+ windSpeed+", pressure="+pressure);
    }
}
