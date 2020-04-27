package com.sachin.designpattern.demo.observer;

public class Alert implements Observer{
    private int temp;
    private int windSpeed;
    private int pressure;

    @Override
    public void update(int temp, int windSpeed, int pressure) {
        this.temp = temp;
        this.windSpeed = windSpeed;
        this.pressure = pressure;
        alert();
    }

    public void alert() {
        System.out.println("Alerting changes temp="+ temp + ", windSpeed="+ windSpeed+", pressure="+pressure);
    }
}
