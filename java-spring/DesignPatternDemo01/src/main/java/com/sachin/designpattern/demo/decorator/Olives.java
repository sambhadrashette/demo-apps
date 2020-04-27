package com.sachin.designpattern.demo.decorator;

public class Olives extends ToppingDecorator {
    public Olives(Pizza pizza) {
        this.pizza = pizza;
    }

    @Override
    public String getDescription() {
        return this.pizza.getDescription() + " with Olives";
    }

    @Override
    public double cost() {
        return pizza.cost() + 5.0;
    }
}
