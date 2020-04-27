package com.sachin.designpattern.demo.decorator;

public class Cheese extends ToppingDecorator {
    public Cheese(Pizza pizza) {
        this.pizza = pizza;
    }

    @Override
    public String getDescription() {
        return this.pizza.getDescription() + " with Cheese";
    }

    @Override
    public double cost() {
        return pizza.cost() + 10.0;
    }
}
