package com.sachin.designpattern.demo.decorator;

public class PizzaMachine {
    public static void main(String[] args) {
        Pizza pizza = new ThickCrustPizza();
        pizza = new Cheese(pizza);
        pizza = new Peppers(pizza);
        pizza = new Olives(pizza);
        System.out.println(pizza.getDescription() + " costs Rs"+ pizza.cost());
    }
}
