package com.sachin.designpattern.demo.decorator;

public abstract class Pizza {
    private String description = "Unnamed pizza";
    public String getDescription() {
        return this.description;
    }
    public abstract double cost();
}
