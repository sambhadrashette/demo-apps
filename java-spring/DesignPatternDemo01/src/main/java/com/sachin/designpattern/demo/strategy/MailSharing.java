package com.sachin.designpattern.demo.strategy;

public class MailSharing implements ShareStrategy {
    @Override
    public void share() {
        System.out.println("Sharing through mail");
    }
}
