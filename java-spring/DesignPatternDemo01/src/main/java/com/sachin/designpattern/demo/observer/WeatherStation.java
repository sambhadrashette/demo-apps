package com.sachin.designpattern.demo.observer;

import java.util.ArrayList;
import java.util.List;

public class WeatherStation implements Subject {
    private int temp;
    private int windSpeed;
    private int pressure;
    private List<Observer> observers;
    public WeatherStation() {
        this.observers = new ArrayList<>();
    }

    @Override
    public void registerObserver(Observer observer) {
        this.observers.add(observer);
    }

    @Override
    public void removerObserver(Observer observer) {
        this.observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        observers.stream().forEach(observer -> observer.update(temp, windSpeed, pressure));
    }
}
