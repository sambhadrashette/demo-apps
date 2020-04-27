package com.sachin.designpattern.demo.observer;

public class UserInterface implements Observer{
    private int temp;
    private int windSpeed;
    private int pressure;

    @Override
    public void update(int temp, int windSpeed, int pressure) {
        this.temp = temp;
        this.windSpeed = windSpeed;
        this.pressure = pressure;
        display();
    }

    public void display() {
        System.out.println("displaying changes temp="+ temp + ", windSpeed="+ windSpeed+", pressure="+pressure);
    }
}
