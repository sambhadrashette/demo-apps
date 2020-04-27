package com.sachin.designpattern.demo.factory;

public abstract class Calendar {
    Zone zone;
    public abstract void print();
    public abstract Calendar createCalendar();
}
